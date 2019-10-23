from random import shuffle
from itertools import accumulate
from operator import add

import scipy.stats

from matplotlib import pyplot as plt
import seaborn as sns

import numpy as np
import pandas as pd


def produce_dog_dataframe(N, weight_effect = 5):
    breeds = [0]*N + [1]*N
    hair_lengths = np.random.permutation(breeds)
    weights = [np.random.standard_normal() + 10 + weight_effect * breed for breed in breeds]
    dogs = pd.DataFrame.from_dict({"breed": breeds,
                                   "weight": weights,
                                   "hair_length": hair_lengths})
    return dogs


def plot_data(dataframe, observation_name, ax=None):
    if ax is None:
        f, ax, = plt.subplots(figsize=(12, 6))
    data = dataframe[observation_name]
    sns.distplot(dataframe[observation_name], color = "gray", ax=ax)
    ax.set_xlim(5, 20);
    plot_mean(data, "all observations", ax=ax)
    ax.legend(loc=(1,0.8))
    plt.tight_layout()
    print_mean_square(data, "all observations")
    
    
def plot_mean(data, name, ax, color="gray", ):
    mean = np.mean(data)
    
    ylim = ax.set_ylim()
    ax.vlines(mean, *ylim,
              colors=color, linestyle='--', linewidth=4,
              label = 'mean for \n' + name )

    
def print_mean_square(array, name):
    print("For "+ name + ", mean squared difference is {:.2f}".format(np.var(array)))

    
def plot_partition(dataframe, group_name, observation_name, ax=None):
    
    if ax is None:
        f, ax, = plt.subplots(figsize=(12, 6))
    
    group_values = dataframe[group_name]
    group_indices = group_values.unique()
    
    observations = dataframe[observation_name]
    
    colors = ["C0", "C1"]
    
    name_string = ' '.join(word.capitalize() for word in group_name.split("_"))

    print_mean_square(dataframe[observation_name], "all data")
    
    group_means = []
    
    for group_idx in group_indices:
        partitioned_observations = observations[group_values == group_idx]
        
        group_means.append(np.mean(partitioned_observations))

        sns.distplot(partitioned_observations, label=name_string + " " + str(group_idx),
                    color=colors[group_idx], ax=ax)
        print_mean_square(partitioned_observations, name_string + " " + str(group_idx))

    print_mean_square(group_means, "group means")
        
    plot_mean(observations, "all observations", ax)
        
    for group_idx in group_indices:
        partitioned_observations = observations[group_values == group_idx]
        plot_mean(partitioned_observations, name_string + " " + str(group_idx),
                  color = colors[group_idx], ax=ax)
        
    ax.set_xlim(5, 20)
    ax.set_title("Data Partitioned According to " + name_string)
    ax.legend(loc=(1, 0.1))
    plt.tight_layout()
    

def group_data(data,measure,difficulties):
    grouped_data = [data[measure,difficulty]
                        for difficulty in difficulties]
    return grouped_data


def anova_by_hand(dataframe, measure):

    N = len(dataframe[measure])
    groups = dataframe["difficulty"].unique()
    k = len(groups)
    group_size = N/k

    anova_frame = make_anova_frame(dataframe, measure, groups)

    sum_of_squares, dof, mean_square = make_anova_dicts(anova_frame, measure, N, k)

    F = mean_square["explained"] / mean_square["residual"]

    return anova_frame, sum_of_squares, dof, mean_square, F


def make_anova_frame(dataframe, measure, groups):
    anova_frame = dataframe.copy()
    anova_frame["grand_mean"] = anova_frame[measure].mean()

    group_means = anova_frame.groupby("difficulty")[measure].mean()

    for group in groups:
        anova_frame.loc[anova_frame.difficulty==group,"group_mean"] = group_means[group]

    anova_frame["explained"] = anova_frame["group_mean"]-anova_frame["grand_mean"]

    anova_frame["residual"] = anova_frame[measure]-anova_frame["group_mean"]

    return anova_frame


def make_anova_dicts(anova_frame, measure, N, k):

    sum_of_squares = {}

    keys = [measure, "grand_mean", "explained", "residual"]

    for key in keys:
        sum_of_squares[key] = np.sum(np.square(anova_frame[key]))

    sum_of_squares["explainable"] = sum_of_squares[measure] - sum_of_squares["grand_mean"]

    dof = {}
    dof_vals = [N, 1, k-1, N-1]

    for key, dof_val in zip(keys, dof_vals):
        dof[key] = dof_val

    mean_square = {}

    for key in ["explained", "residual"]:
        mean_square[key] = sum_of_squares[key]/dof[key]

    return sum_of_squares, dof, mean_square