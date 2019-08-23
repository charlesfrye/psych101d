"""Utility for setting the same shared random seed for all notebooks.
WARNING: On import, executes global state-changing functions.
"""
import random

import numpy as np

SHARED_SEED = 14


def set_seeds():
    random.seed(14)
    np.random.seed(14)


set_seeds()
