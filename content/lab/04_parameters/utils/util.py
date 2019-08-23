import daft
import matplotlib.lines
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

dummy_line = lambda color: matplotlib.lines.Line2D([0], [0], color=color, lw=4)


def compare_multiple_postpreds_to_observed(postpreds, observed_data, titles):
    height = 6
    n_postpreds = len(postpreds)

    f, axs = plt.subplots(figsize=(n_postpreds * height, height),
                          ncols=n_postpreds,
                          sharex=True, sharey=True)
    if n_postpreds == 1:
        axs = [axs]

    [compare_postpred_to_observed(postpred_vals, observed_data, ax=ax, title=title)
     for postpred_vals, title, ax in zip(postpreds, titles, axs)]

    return


def compare_postpred_to_observed(postpred_vals, observed_data, ax=None, title=None):
    collapsed_postpred = np.ravel(postpred_vals)
    if ax is None:
        f, ax = plt.subplots(figsize=(8, 8))

    ax.hist(collapsed_postpred, color="C1", alpha=1., lw=4, histtype="step", normed=True,
            bins=25)
    ax.hist(collapsed_postpred, color="C1", alpha=0.5, histtype="stepfilled", normed=True,
            bins=25)
    sns.rugplot(observed_data, height=0.5, ax=ax)
    ax.legend([dummy_line("C1"), dummy_line("C0")],
              ["Sampled data", "Observed data"])
    if title is not None:
        ax.set_title(title, fontsize="xx-large")
    ax.set_xlabel("x", fontsize="x-large")


def elementwise_compare_multiple_postpreds_to_observed(postpreds, df,
                                                       titles=None, max_display=100):
    n_postpreds = len(postpreds)

    if titles is None:
        titles = [None] * len(postpreds)

    f, axs = plt.subplots(figsize=(4 * n_postpreds, 10), ncols=n_postpreds,
                          sharex=True, sharey=True)

    if n_postpreds == 1:
        axs = [axs]

    [elementwise_compare_postpred_to_observed(postpred[:max_display], df, ax=ax, title=title)
     for postpred, title, ax in zip(postpreds, titles, axs)]

    axs[0].set_ylabel("Sample Index", fontsize="x-large")
    axs[0].legend([dummy_line("k"), dummy_line("C0")],
                  ["Posterior Samples", "Observed Data"],
                  loc=(0, -.15))


def tickplot(xs, y_min, y_max, ax, **kwargs):
    ax.vlines(xs, y_min, y_max, **kwargs)


def elementwise_compare_postpred_to_observed(postpred_vals, observed_data, ax=None, title=None):
    num_posterior_samples = postpred_vals.shape[0]

    breaks = np.arange(0, num_posterior_samples + 1)
    if ax is None:
        f, ax = plt.subplots(figsize=(4, 10))

    [tickplot(xs, y_min, y_max, ax=ax) for xs, y_min, y_max
     in zip(postpred_vals, breaks[:-1], breaks[1:])]

    sns.rugplot(observed_data, height=1., ax=ax)

    if title is not None:
        ax.set_title(title, fontsize="xx-large")
    ax.set_xlabel("x", fontsize="x-large")


def generate_normal_data(mu, sigma, N):
    np_data = np.sqrt(sigma) * np.random.standard_normal(size=N) + mu
    df = pd.DataFrame(np_data)
    return df


def make_normal_model_graph():

    arrow_params = {"linewidth": 2,
                    "head_width": 0.25}

    mu_node = daft.Node("mu", r"$\mu$", 1, 2.5, scale=2)
    x_node = daft.Node("x", "x", 3.5, 2.5, scale=2, observed=True)

    x_plate = daft.Plate([2.5, 1.5, 2, 2],
                         label=r"$N$", position="bottom right")

    normal_model_graph = daft.PGM([5, 5], line_width=2,
                                  label_params={"fontsize": 32})

    normal_model_graph.add_node(mu_node)
    normal_model_graph.add_node(x_node)

    normal_model_graph.add_edge("mu", "x", **arrow_params)

    normal_model_graph.add_plate(x_plate)

    normal_model_graph.render()
