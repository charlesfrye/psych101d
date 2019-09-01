test = {
    "name": "For 1: Numbers",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variable?
                    >>> "first2k" in globals().keys()
                    True
                    >>> ## Make sure it's not a range!
                    >>> isinstance(first2k, range)
                    False
                    >>> ## Does it have the right type?
                    >>> isinstance(first2k, list)
                    True
                    >>> ## Does it have enough entries?
                    >>> len(first2k)
                    2001
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Does the variable have the right value
                    >>> all([soln == answr for soln, answr in zip(first2k_soln, first2k)])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> first2k_soln = range(2001)
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
