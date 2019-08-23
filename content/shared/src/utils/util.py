import numpy as np
import pandas as pd
import pymc3 as pm
import theano.tensor as tt

def samples_to_dataframe(samples):
    return pd.DataFrame([sample for sample in samples])


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


def sample_from(model, **kwargs):
    with model:
        samples = pm.sample(**kwargs)
    return samples


def to_pymc(var):
    return tt.as_tensor_variable(var)
