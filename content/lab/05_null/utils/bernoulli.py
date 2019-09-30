import numpy as np


def check_samples(samples, true_p, n_sigma=8):
    """Check whether samples, a Series of 0,1 values, is plausibly
    from a Bernoulli with probability true_p, using a normal approximation
    and a bound in terms of n_sigma multiples of the standard error of the mean
    """
    var = (true_p) * (1 - true_p)  # variance of a bernoulli
    sem = np.sqrt(var / len(samples))  # standard error of the mean, normal approximation
    bound = n_sigma * sem  # size of largest expected error

    error = np.abs(samples.mean() - true_p)

    return error < bound


def posterior_p(alpha, prior, power, positive_result=True):
    """Compute the true posterior probability of the null hypothesis
    given the false positive rate alpha, the true positive rate power,
    and a boolean indicating whether the observed result was positive or negative.
    """
    if positive_result:
        return alpha * prior / (alpha * prior + power * (1 - prior))
    else:
        return (1 - alpha) * prior / ((1 - alpha) * prior + (1 - power) * (1 - prior))
