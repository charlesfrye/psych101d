test = {
    "name": "1: Likelihoods",
    "points": 2,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Likelihood 1:
                    >>> # Must be continuous
                    >>> likelihoods[1].__bases__[0]
                    <class 'pymc3.distributions.distribution.Continuous'>
                    >>> # This distribution has parameters mu and sd
                    >>> dist = likelihoods[1].dist(mu=0, sd=1/np.sqrt(2*np.pi))
                    >>> # Which distribution specifies up to a center and a spread?
                    >>> np.round(dist.logp(0).eval())
                    -0.0
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Likelihood 2:
                    >>> # Must be discrete
                    >>> likelihoods[2].__bases__[0]
                    <class 'pymc3.distributions.distribution.Discrete'>
                    >>> # This distribution has parameter mu
                    >>> dist = likelihoods[2].dist(mu=1)
                    >>> # And its likelihood at 1 is mu / e ^ mu
                    >>> dist.logp(1.).eval()
                    array(-1., dtype=float32)
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Likelihood 3:
                    >>> # Must be continuous and positive
                    >>> likelihoods[3].__bases__[0]
                    <class 'pymc3.distributions.continuous.PositiveContinuous'>
                    >>> # This distribution has parameter lam
                    >>> dist = likelihoods[3].dist(lam=1)
                    >>> # And it has likelihood lam at 0
                    >>> dist.logp(0).eval()
                    array(0., dtype=float32)
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Likelihood 4:
                    >>> # Must be discrete
                    >>> likelihoods[4].__bases__[0]
                    <class 'pymc3.distributions.distribution.Discrete'>
                    >>> # This distribution has parameters n and p
                    >>> dist = likelihoods[4].dist(n=1, p=0.5)
                    >>> # This distribution has probability p for 0 when n=1
                    >>> np.exp(dist.logp(0).eval())
                    0.5
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
