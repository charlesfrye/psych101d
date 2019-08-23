"""Utility for hiding warnings and messages that students don't need to see.
WARNING: On import, executes global state-changing functions.
"""
import logging
import warnings


def quiet_pymc3():
    logger = logging.getLogger("pymc3")
    logger.setLevel(logging.ERROR)


def quiet_theano():
    logger = logging.getLogger("theano.tensor.blas")
    logger.setLevel(logging.ERROR)


def quiet_warnings():
    warnings.filterwarnings("ignore", category=FutureWarning)
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    warnings.filterwarnings("ignore", category=UserWarning)


quiet_warnings()
quiet_theano()

import pymc3  # noqa: F401

quiet_pymc3()
