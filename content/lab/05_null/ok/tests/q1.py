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
                    >>> ## your prior is probably mis-specified.
                    >>> utils.bernoulli.check_samples(prior_samples["null_true"], prior)
                    True
                    >>> ## If you fail this test because it returns False,
                    >>> ## your likelihood is probably mis-specified, and alpha is wrong.
                    >>> null_true_results = prior_samples["positive_result"].loc[null_true_selector]
                    >>> utils.bernoulli.check_samples(null_true_results, alpha)
                    True
                    >>> ## If you fail this test because it returns False,
                    >>> ## your prior is probably mis-specified, and the power is wrong.
                    >>> null_false_results = prior_samples["positive_result"].loc[-null_true_selector]
                    >>> utils.bernoulli.check_samples(null_false_results, power)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> null_true_selector = prior_samples["null_true"].astype(bool)
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
