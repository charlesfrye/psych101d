test = {
    "name": "Bootstrapping 2: inside_95CI",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variable?
                    >>> "inside_95CI" in globals().keys()
                    True
                    >>> ## Does it have the right type?
                    >>> callable(inside_95CI)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Simple check: is 0 inside this interval?
                    >>> inside_95CI(sample, 0)
                    True
                    >>> ## Is the left side approximately correct?
                    >>> inside_95CI(sample, left_side - eps)
                    False
                    >>> inside_95CI(sample, left_side + eps)
                    True
                    >>> ## Is the right side approximately correct?
                    >>> inside_95CI(sample, right_side - eps)
                    True
                    >>> inside_95CI(sample, right_side + eps)
                    False
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> sample = pd.Series(np.random.normal(size=250))
            >>> left_side, right_side = sample.quantile([0.05, 0.95])
            >>> ## the above interval will contain 0 with probability one in 4e11
            >>> eps = 1e-5
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
