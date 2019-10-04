import numpy as np


def get_bound_t_mean(n, df=18, n_sigma=8):
    true_var_t = compute_var_t(df)
    sem = compute_sem(true_var_t, n)

    return n_sigma * sem


def get_bound_t_variance(n, df=18, n_sigma=8):
    """Based on Gaussian approximation to Student.
    More accurate as df and n increase.
    """
    true_var_t = compute_var_t(df)
    sev = compute_sev(true_var_t, n)

    return n_sigma * sev


def compute_var_t(df):
    return df / (df - 2)


def compute_sem(var, n):
    return np.sqrt(var / n)


def compute_sev(var, n):
    return var * np.sqrt(2 / (n - 1))
