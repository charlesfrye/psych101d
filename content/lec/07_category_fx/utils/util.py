import numpy as np


def make_mixture_d(weights, params, funks):
    n_components = len(weights)
    if callable(funks):
        funks = n_components * [funks]
        
    def mixture_d(x):
        return np.dot(weights, [funk(x, *param)
                                for funk, param in zip(funks, params)])
    return mixture_d


def get_smallest_difference(samples, idx_0=0, idx_1=2):
    return samples[
        samples.apply(lambda mus: mus[idx_1] > mus[idx_0])].apply(lambda mus: mus[idx_1] - mus[idx_0]).min()