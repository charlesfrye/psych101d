test = {
    "name": "Sampling from the Posterior",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## This function checks whether the samples from the posterior
                    >>> ## are behaving as expected, using the analytic value of the posterior.
                    >>> ## If you fail this test because it returns False,
                    >>> ## your model is mis-specified or you are sampling incorrectly.
                    >>> ## If you have passed the tests in q1, then your setting of the observed
                    >>> ## value or the manner you are drawing samples is likely incorrect.
                    >>> utils.bernoulli.check_samples(posterior_samples["null_true"], posterior)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> # First, use Bayes' Rule to calculate the posterior p
            >>> posterior = utils.bernoulli.posterior_p(alpha, prior, power)
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
