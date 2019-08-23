import math

import numpy as np
import pandas as pd
import pymc3 as pm
import statsmodels.api as sm
import statsmodels.formula.api as smf
import theano.tensor as tt

import shared.src.utils.util as util

def specify_caffeine_ground_truth(effect_size_caffeine, num_subjects=100, subject_split=0.5,
                                  heteroscedasticity=0, outliers=False):
    """Specifies a model for the effect of caffeine on alertness.
    If heteroscedasticity is 0 and outliers is False, it is an ANOVA model.
    
    Arguments
    ---------
    effect_size_caffeine : int, size of the effect of caffeine on alertness. In z-scored units.
    num_subjects : int, number of subjects in the experiment.
    subject_split : float, fraction of subjects who are given caffeine. 0 < subject_split < 1.
                    Default is 0.5.
    heteroscedasticity: float, exponent controlling ratio of variance between subjects with
                        and without caffeine. Default is 0, for no difference in variance.
    outliers: bool, flag controlling whether the subjects' alertness scores are drawn from a
              distribution with outliers (the Multivariate Student's T) or not (Gaussian).
              Default is False.
    
    Returns
    -------
    true_model : pm.Model, a data model for the effect of caffeine on alertness
    """
    true_model = pm.Model()

    baseline_alertness = 10.
    baseline_sigma = 1.
    
    caffeinated_sigma = (2 ** heteroscedasticity) * baseline_sigma

    num_had_caffeine = math.floor(num_subjects * subject_split)
    num_no_caffeine = num_subjects - num_had_caffeine
    
    with true_model:
        had_caffeine = np.hstack([np.zeros(num_had_caffeine), np.ones(num_no_caffeine)])
        had_caffeine = pm.Deterministic("had_caffeine",
                                       tt.as_tensor_variable(had_caffeine))

        mus = baseline_alertness + effect_size_caffeine * had_caffeine
        cov = np.diag(
            np.hstack([np.ones(num_had_caffeine) * caffeinated_sigma, np.ones(num_no_caffeine) * baseline_sigma]))
        
        args = {"mu": mus, "cov": cov, "shape": (1, num_subjects)}
        if outliers:
            distribution = pm.MvStudentT
            args["nu"] = 1
        else:
            distribution = pm.MvNormal
            
        alertness_scores = distribution("alertness_scores", **args)
            
    return true_model

def simulate_experiments_and_run_anovas(model, num_experiments=100):
    sample_kwargs = {"chains": 1, "tune": 500, "progressbar": False}
    anova_formula = "alertness_scores ~ C(had_caffeine)"
    
    samples = util.samples_to_dataframe(sample_from(model, num_experiments, **sample_kwargs))
    
    data_dfs = []
    for ii, sample_row in samples.iterrows():
        data_dfs.append(sample_to_df(sample_row))
    
    anova_tables = [run_anova(data_df, formula=anova_formula) for data_df in data_dfs]
    
    return data_dfs, anova_tables

def sample_from(model, n, filt=10, **sample_kwargs):
    with model:
        samples = pm.sample(draws=n * filt, compute_convergence_checks=False, **sample_kwargs)[::filt]
    [samples.remove_values(name) for name in samples.varnames if "_log__" in name]
    
    return samples

def sample_to_df(sample):
    dct = {}
    for idx_str in sample.index:
        dct.update({idx_str: np.squeeze(sample[idx_str])})
    return pd.DataFrame(dct)

def run_anova(data_df, formula):

    ols_lm = smf.ols(formula, data=data_df)

    fit = ols_lm.fit()

    table = sm.stats.anova_lm(fit, typ=2)
    
    return table