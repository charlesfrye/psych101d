test = {
    "name": "1: Priors",
    "points": 2,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Prior 1:
                    >>> # Must be positive and continuous
                    >>> priors[1].__bases__[0]
                    <class 'pymc3.distributions.continuous.PositiveContinuous'>
                    >>> # This distribution has no parameters
                    >>> dist = priors[1].dist()
                    >>> # This distribution has same likelihood for all positive
                    >>> dist.logp(shared_util.to_pymc(np.array([1, 2, -1]))).eval()
                    array([  0.,   0., -inf])
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Prior 2:
                    >>> # Must be bounded and continuous
                    >>> priors[2].__bases__[0]
                    <class 'pymc3.distributions.continuous.BoundedContinuous'>
                    >>> # This distribution has parameters upper and lower
                    >>> dist = priors[2].dist(lower=0, upper=math.e)
                    >>> # This distribution has same likelihood for all in bounds
                    >>> dist.logp([1, 2, -1]).eval()
                    array([ -1.,  -1., -inf])
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Prior 3:
                    >>> # Must be continuous
                    >>> priors[3].__bases__[0]
                    <class 'pymc3.distributions.distribution.Continuous'>
                    >>> # This distribution has no parameters
                    >>> dist = priors[3].dist()
                    >>> # This distribution has same likelihood for all values
                    >>> dist.logp(shared_util.to_pymc(np.array([1, 2, -1]))).eval()
                    array([0, 0, 0])
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Prior 4:
                    >>> # Must be discrete
                    >>> priors[4].__bases__[0]
                    <class 'pymc3.distributions.distribution.Discrete'>
                    >>> # This distribution has parameters upper and lower
                    >>> dist = priors[4].dist(lower=0, upper=3)
                    >>> # This distribution has same likelihood for all in bounds
                    >>> np.round(dist.logp([1, 3, -1]).eval())
                    array([ -1.,  -1., -inf])
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Prior 5:
                    >>> # Must be continuous
                    >>> priors[5].__bases__[0]
                    <class 'pymc3.distributions.distribution.Continuous'>
                    >>> # This distribution has parameters mu and sd
                    >>> dist = priors[5].dist(mu=0, sd=1/np.sqrt(2*np.pi))
                    >>> # Which distribution specifies up to a center and a spread?
                    >>> np.round(dist.logp(0).eval())
                    -0.0
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": """
            """,
            "teardown": "",
            "type": "doctest"}]
        }
