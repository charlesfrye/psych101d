import numpy as np
import pandas as pd

def check_for_scipy(compute_t):
    """Loose test for the use of scipy
    inside of the student-defined compute_t function
    """
    try:
        if np.isnan(compute_t(pd.Series(), pd.Series())):
            raise ValueError
    except ValueError:
        print("Do Not Use SciPy")
    except Exception:
        pass


def flatten_samples(series_of_arrays):
    """Converts a pandas series of numpy arrays
    into a single, flattened array"""
    return np.array(series_of_arrays.tolist()).flatten()
