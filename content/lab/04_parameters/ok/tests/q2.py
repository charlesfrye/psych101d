test = {
    "name": "sampling from priors",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## First, testing the samples from agnostic_prior
                    >>> ## Is the mean of the prior close to the truth?
                    >>> np.abs(agnostic_prior_mus.mean() - agnostic_model_prior_mu) <= 5 * agnostic_sem
                    True
                    >>> ## Is the spread of the prior close to the truth?
                    >>> np.abs(agnostic_prior_mus.std() - agnostic_model_prior_sd) <= 1.0
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Second, testing the samples from wrong_prior
                    >>> ## Is the mean of the prior close to the truth?
                    >>> np.abs(wrong_prior_mus.mean() - wrong_model_prior_mu) <= 5 * wrong_sem
                    True
                    >>> # Is the spread of the prior close to the truth?
                    >>> np.abs(wrong_prior_mus.std() - wrong_model_prior_sd) <= 0.1
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> agnostic_sem = agnostic_model_prior_sd / np.sqrt(num_prior_samples)
            >>> wrong_sem = wrong_model_prior_sd / np.sqrt(num_prior_samples)
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
