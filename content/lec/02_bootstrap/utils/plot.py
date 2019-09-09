import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def skewness_comparison_plot(df, keys, axs):
    skews = df.groupby(["dataset"]).skew()
    for ii, (key, ax) in enumerate(zip(keys, axs)):
        sns.distplot(
            df["value"][df["dataset"] == key], ax=ax, color="C"+str(ii),
            label=f"skew: {rounded_skew(skews, key)}")
        ax.set_title(key, fontsize="small")
        ax.legend(); ax.set_xlabel("")
    ax.set_xlabel("value")
    plt.tight_layout(); 
    
    
def plot_score_comparison(data, guesses, first_game_scores, second_game_scores, axs):
    first_game_ylims = [-30, 0]
    second_game_ylims = [-3, 0]
    
    sns.distplot(data, ax=axs[0], label="data", kde_kws={"lw": 6}, bins=100);
    add_mean_median(data.mean(), data.median(), pd.Series(axs[0].get_ylim()) * 0.5, axs[0])
    axs[0].set_xlim([0, 10]); axs[0].legend()
    axs[0].set_title("Data and Summary Statistics")
    
    axs[1].plot(guesses, first_game_scores, lw=6, color="C1");
    axs[2].plot(guesses, second_game_scores, lw=6, color="C0");
    axs[1].set_title("Score on First Game"); axs[2].set_title("Score on Second Game");

    add_mean_median(data.mean(), data.median(), first_game_ylims, axs[1])
    add_mean_median(data.mean(), data.median(), second_game_ylims, axs[2])

    axs[1].set_ylim(*first_game_ylims); axs[2].set_ylim(*second_game_ylims);
    axs[2].set_xlabel("Guess");
    axs[1].set_ylabel("Score"); axs[2].set_ylabel("Score");
    
    
def add_mean_median(mean, median, lims, ax, mean_color="C1", median_color="C0"):
    ax.vlines(mean, *lims, lw=4, color=mean_color, label="mean");
    ax.vlines(median, *lims, lw=4, color=median_color, label="median");
    
    
def rounded_skew(skews, key, k=2):
    return round(float(skews.loc[key]), k)