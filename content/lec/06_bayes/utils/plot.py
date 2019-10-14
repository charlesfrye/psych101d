import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def plot_raw_data_sentiment(data, ax):

    ax.scatter(data["album_release_date"], data["positive"],
               alpha=0.1, s=144, color="k");
    ax.set_xlabel("Album Release Date")
    ax.set_ylabel("Positive Sentiment About\nTrump in Hip-Hop Lyric")

    
def plot_switchpoint(p1, p2, switch, xs, ax, **plot_kwargs):
    ps = np.where(np.array(xs) < switch, p1, p2)
    ax.plot(xs, ps, **plot_kwargs)
    
    
def plot_MAP(MAP, samples, variable, ax=None, compare_mean=False, **distplot_kwargs):
    if ax is None:
        f, ax = plt.subplots(figsize=(12, 6))
    sns.distplot(samples[variable], **distplot_kwargs, color="C2");
    ymax =  ax.get_ylim()[1]
    ax.vlines(MAP[variable], 0, ymax * 0.5, color="k", lw=4, label="MAP Estimate");
    if compare_mean:
        ax.vlines(samples[variable].mean(), 0, ymax * 0.5,
                  color="C1", lw=4, label="Mean");
    ax.legend()
    return ax