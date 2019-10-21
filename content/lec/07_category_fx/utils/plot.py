import matplotlib.pyplot as plt
import numpy as np

from .util import make_mixture_d
    
def comparative_mixture_plot(weights, params, funks, labels=None, xs=None, weighted=False):
    f, axs = plt.subplots(figsize=(12, 12), nrows=2, sharex=True)
    if xs is None:
        xs = np.linspace(-10, 10, num=10000)
        
    plot_mixture_marginal(weights, params, funks, axs[0], xs)
    axs[0].set_title("Mixture Distribution"); axs[1].set_title("Mixture Components")
    plot_mixture_componentwise(weights, params, funks, labels, ax=axs[1], xs=xs, weighted=weighted)
    return f, axs


def plot_mixture_componentwise(weights, params, funks, labels=None, ax=None, xs=None, weighted=False):
    n_components = len(weights)
    if callable(funks):
        funks = n_components * [funks]
    if labels is None:
        labels = n_components * [None]
        
    if ax is None:
        f, ax = plt.subplots(figsize=(12, 6))
    if xs is None:
        xs = np.linspace(-10, 10, num=10000)
        
    for weight, param, funk, label in zip(weights, params, funks, labels):
        raw_ps = funk(xs, *param)
        if weighted:
            ps = weight * raw_ps
        else:
            ps = raw_ps
        plt.plot(xs, ps, lw=4, label=label);

        
def plot_mixture_marginal(weights, params, funks, ax=None, xs=None):
    if ax is None:
        f, ax = plt.subplots(figsize=(12, 6))
    if xs is None:
        xs = np.linspace(-10, 10, num=10000)
        
    ax.plot(xs, make_mixture_d(weights, params, funks)(xs), lw=6, color="k");