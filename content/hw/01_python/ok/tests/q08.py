test = {
    "name": "For 2: Slicing",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variable?
                    >>> "first1k" in globals().keys()
                    True
                    >>> ## Make sure it's not a range!
                    >>> isinstance(first1k, range)
                    False
                    >>> ## Does it have the right type?
                    >>> isinstance(first1k, list)
                    True
                    >>> ## Does it have enough entries?
                    >>> len(first1k)
                    1001
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Does the variable have the right value
                    >>> all([soln == answr for soln, answr in zip(first1k_soln, first1k)])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> first1k_soln = list(range(2001))[:1001]
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
