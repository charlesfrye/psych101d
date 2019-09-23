import cycler
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d  # noqa: F401
import numpy as np
import seaborn as sns


def add_interval(ax, bounds, lw=10, color="C1", label=""):
    ylims = ax.get_ylim();
    ax.hlines(0, *bounds, color=color, label=label, lw=lw);
    ax.set_ylim(*ylims);


def add_cbar(f, label="count"):
    plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2)  # shrink fig so cbar is visible
    # make new ax object for the cbar
    cbar_ax = f.add_axes([.85, .2, .05, .5])  # x, y, width, height
    plt.colorbar(cax=cbar_ax, label=label);


def create_cycler(cm, n):
    color = cm(np.linspace(0, 1, n))
    return cycler.cycler('color', color)


def histogram3d(x, y, labels=["", ""],
                bins=10, cm=lambda x: "C0", colorby="x"):
    # based off of recipe at https://matplotlib.org/3.1.0/gallery/mplot3d/hist3d.html
    _ = plt.figure(figsize=(8, 8)); ax = plt.axes(projection='3d')

    hist, xedges, yedges = np.histogram2d(x, y, bins=bins, density=True)
    xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
    xpos = xpos.ravel()
    ypos = ypos.ravel()
    zpos = 0

    # Construct arrays with the dimensions for the 16 bars.
    dx = dy = 0.5 * np.ones_like(zpos)
    dz = hist.ravel()
    if colorby == "x":
        colorpos = xpos
    elif colorby == "y":
        colorpos = ypos
    elif colorby == "z":
        colorpos = dz
    elif callable(colorby):
        colorpos = colorby(xpos, ypos, dz)
    else:
        raise ValueError(f"colorby must be 'x', 'y', 'z', or callable, but was {colorby}")
    colors = cm((colorpos - min(colorpos)) / (max(colorpos) - min(colorpos)));

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz,
             zsort='average', color=colors);
    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    ax.set_zlabel("Freq.")


def jointgrid_effort(data):
    g = sns.JointGrid(x="attempts", y="successes", data=data, height=8)
    mx = max(data["attempts"].max(), data["successes"].max())
    g.plot_joint(plt.hist2d, bins=np.arange(-0.5, mx + 1.5),
                 cmap="Blues", density=True, data=data)
    g.plot_marginals(sns.distplot, bins=range(0, 12), kde=False, hist_kws={"align": "left"});
    g.ax_joint.set_xticks(range(0, mx+1, 2))
    add_cbar(g.fig, label="frequency");
