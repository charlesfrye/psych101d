import numpy as np
import pandas as pd
import pymc3 as pm
import theano.tensor as tt

def samples_to_dataframe(samples, drop_internal=False):
    chains = samples.chains
    chainwise_dfs = [pd.DataFrame([sample for sample in samples._straces[chain]])
                     for chain in chains]
    full_df = pd.concat(chainwise_dfs)
    if drop_internal:
        internal_vars = [column for column in full_df.columns
                         if column.startswith("_") or column.endswith("__")]
        full_df = full_df.drop(columns=internal_vars)

    return full_df


def standardize(data, true_stat, standard_error, stat_func):
    """For a given dataset, compare its value on the data to the true value,
    in units of standard error."""
    return (stat_func(data) - true_stat) / standard_error


def standardize_all(data, selectors, stat_values, standard_errors, stat_func=lambda d: d.mean()):
    """For a collection of subsets of data given by selectors, compare the values computed by stat_func
    to their true values, in units of standard error."""
    return np.array([standardize(data[selector], stat_value, std_err, stat_func)
                    for selector, stat_value, std_err
                    in zip(selectors, stat_values, standard_errors)])


def compute_sem(true_sds, selectors):
    """Compute the true standard errors of the means of datasets defined by selectors,
    given the true standard deviations"""
    return np.divide(true_sds, np.sqrt([sum(selector) for selector in selectors]))


def compute_sev(true_sds, selectors):
    """Compute the true standard errors of the variances of datasets defined by selectors,
    given the true standard deviations, under a Gaussian assumption"""
    return np.sqrt(2 * np.power(true_sds, 4)) / np.sqrt([sum(selector) for selector in selectors])


def sample_from(model, draws=500, chains=2, progressbar=False, compute_convergence_checks=False,
                **kwargs):
    """Wrapper for pm.sample to avoid "with" and set a few reasonable defaults for our case."""
    sample_kwargs = set_sample_kwargs(draws, chains, progressbar, compute_convergence_checks,
                                      kwargs)

    with model:
        samples = pm.sample(**sample_kwargs)

    return samples


def set_sample_kwargs(draws, chains, progressbar, compute_convergence_checks, kwargs):
    """Override values given in kwargs by values given as keyword arguments, for sample_from"""
    vars = [draws, chains, progressbar, compute_convergence_checks]
    varnames = ["draws", "chains", "progressbar", "compute_convergence_checks"]

    for var, varname in zip(vars, varnames):
        if varname not in kwargs.keys():
            kwargs[varname] = var
    return kwargs


def to_pymc(var, **kwargs):
    """Thin wrapper for theano.tensor.as_tensor_variable.

    Used to avoid imports of theano.tensor in student-facing notebooks."""
    return tt.as_tensor_variable(var, **kwargs)
