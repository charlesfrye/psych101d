"""Updates the matplotlib.rc to the course's style"""
import matplotlib as mpl
from cycler import cycler

cal_colors = ['#003262', '#FDB515']
default_colors = [color["color"] for color in mpl.rcParamsDefault["axes.prop_cycle"][2:]]

mpl.rcParams['axes.prop_cycle'] = cycler(color=cal_colors + default_colors)
