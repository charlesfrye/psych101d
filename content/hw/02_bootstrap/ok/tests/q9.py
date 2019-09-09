test = {
    "name": "Putting It All Together",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variables?
                    >>> "easy_boot_delta_means" in globals().keys()
                    True
                    >>> "hard_boot_delta_means" in globals().keys()
                    True
                    >>> "no_difference_easy" in globals().keys()
                    True
                    >>> "no_difference_hard" in globals().keys()
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Are the left sides located in the right spot relative to 0?
                    >>> np.percentile(easy_boot_delta_means, 5) < 0
                    True
                    >>> np.percentile(hard_boot_delta_means, 5) < 0
                    False
                    >>> ## Are the means reasonable?
                    >>> np.mean(easy_boot_delta_means) > 0.15
                    True
                    >>> np.mean(hard_boot_delta_means) > 1.5
                    True
                    >>> ## Are the final inferences correct?
                    >>> no_difference_easy, no_difference_hard
                    (True, False)
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> eps = 1e-5
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
