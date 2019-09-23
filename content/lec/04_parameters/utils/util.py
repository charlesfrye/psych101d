from itertools import product

import numpy as np
import pandas as pd


def approx_mle(params, log_p, values):
    """Given a dictionary of lists of parameters, a log probability function, and values
    return the parameters that maximize log_p on values.
    """
    lls = []

    param_choices = product(*params.values())
    for param in param_choices:
        kwargs = {key: val for key, val in zip(params.keys(), param)}
        loglikelihood = np.mean(log_p(values, **kwargs))
        kwargs.update({"ll": loglikelihood})
        lls.append(kwargs)
        
    ll_df = pd.DataFrame(lls)
    sorted_ll_df = ll_df.sort_values(by="ll", ascending=False)
    param_cols = sorted_ll_df[[key for key in params.keys()]]
    mle_params = param_cols.iloc[0]
    return dict(mle_params)


def to_image(noise):
    sz = int(np.sqrt(len(noise)))
    noise = 256 * (noise - min(noise)) / (max(noise) - min(noise))
    return np.array(noise).reshape(sz, sz).astype(np.uint8)