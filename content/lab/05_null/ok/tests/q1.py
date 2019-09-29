test = {
    "name": "Sampling from the Prior",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## This function checks whether the samples from the prior
                    >>> ## are behaving as expected under the prior.
                    >>> ## If you fail this test because it returns False,
                    >>> ## your model is probably mis-specified.
                    >>> utils.bernoulli.check_samples(prior_samples["null_true"], prior)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
