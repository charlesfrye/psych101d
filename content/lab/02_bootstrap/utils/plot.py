import matplotlib.pyplot as plt

def add_vertical_line(value, h=0.5, color="black", ax=None, label=None, lw=4, **kwargs):
    """Adds a vertical line to the axis ax of height h times the height of the plot,
    starting from the x-axis.
    Optionally colors it with color, adds a legend label with label, sets the width
    with lw, and passes any additional keyword arguments to matplotlibs' vlines function.
    """
    
    if hasattr(value, "__len__"):
        if len(value) > 1:
            raise ValueError(
                "value must be single number, but is a {} of length {}"
                .format(type(value).__name__, len(value)))
    
    if ax is None:
        ax = plt.gca()
        
    ylim = ax.get_ylim()
    
    ax.vlines(value, 0, ylim[1]  * h, color=color, label=label, lw=lw, **kwargs)