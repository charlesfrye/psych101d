import daft
import matplotlib.pyplot as plt
import seaborn as sns


def compare_bernoullis(bernoulli_samples, colors=None, titles=None):
    """Given a list of Series representing samples from a Bernoulli variable,
    plot histograms of each Series in the list.
    Optionally, provide a color and/or title for each histogram.
    
    Parameters
    ==========
    bernoulli_samples: list of Series or list of arrays. Each element in
                       this list is passed to sns.distplot
    colors : list of strings or None. If not None, use to color the histograms.
    titles : list of strings or None. If not None, use to title the axes.
    
    Returns
    =======
    f : matplotlib Figure containing axs with histograms plotted in
    axs : array of matplotlib Axes
    """
    n_bernoullis = len(bernoulli_samples)
    
    f, axs = plt.subplots(figsize=(6 * n_bernoullis, 6),
                          ncols=n_bernoullis,  sharex=True, sharey=True)
    if n_bernoullis == 1:
        axs = np.array([axs])
    if colors is None:
        colors = [None] * n_bernoullis
    if titles is None:
        titles = [""] * n_bernoullis
        
    assert len(colors) == n_bernoullis, f"provide the same number of colors as bernoulli_samples: {n_bernoullis}"
    assert len(titles) == n_bernoullis, f"provide the same number of titles as bernoulli_samples: {n_bernoullis}"
    
    bins = [-0.5, 0.5, 1.5]
    kwargs = {"kde": False, "bins": bins,
              "norm_hist": True, "hist_kws": {"alpha": 1, "ec": "k", "lw": 4}}
    for ax, bernoulli, color, title in zip(axs, bernoulli_samples, colors, titles):
        sns.distplot(bernoulli, **kwargs, color=color, ax=ax);
        ax.set_xlabel("")
        ax.set_title(title)
        ax.set_ylim(0, 1.1)

    [ax.set_xticks([0, 1]) for ax in axs]
    [ax.set_xticklabels(["0", "1"]) for ax in axs];
    return f, axs


def make_science_model_graph(observed=True, plate=False):

    arrow_params = {"linewidth": 2,
                    "head_width": 0.25}
    label_params = {"fontsize": "small"}

    hypothesis_node = daft.Node("hypothesis", r"$H_0$", 1.5, 2.5, scale=2.2, #aspect=1.5,
                                label_params=label_params)
    result_node = daft.Node("result", "Result", 4, 2.5, scale=2.2,
                            observed=observed, label_params=label_params)

    result_plate = daft.Plate([2.5, 1.5, 2, 2],
                         label=r"$N$", position="bottom right")

    science_model_graph = daft.PGM([5, 5], line_width=2,
                                  label_params={"fontsize": 32})

    science_model_graph.add_node(hypothesis_node)
    science_model_graph.add_node(result_node)

    science_model_graph.add_edge("hypothesis", "result", **arrow_params)

    if plate:
        science_model_graph.add_plate(result_plate)

        # Avoid fill with blue in newer versions of matplotlib
        science_model_graph._plates[0].bbox["fc"] = "white"

    science_model_graph.render()
    plt.tight_layout();
    return science_model_graph