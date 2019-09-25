test = {
    "name": "sampling from posteriors",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## First, testing the samples from agnostic_posterior
                    >>> ## Is the mean of the posterior close to what was expected?
                    >>> np.abs(agnostic_posterior_mean - agnostic_target) <= agnostic_bound
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Second, testing the samples from wrong_posterior
                    >>> ## Is the mean of the posterior close to what was expected?
                    >>> np.abs(wrong_posterior_mean - wrong_target) <= wrong_bound
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> agnostic_posterior_mean = agnostic_samples["mu"].mean()
            >>> agnostic_target = 1.75
            >>> agnostic_bound = 0.7
            >>> wrong_posterior_mean = wrong_samples["mu"].mean()
            >>> wrong_target = 0.65
            >>> wrong_bound = 0.4
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
