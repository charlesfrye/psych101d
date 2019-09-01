test = {
    "name": "If 5: An Ideal Answer",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variable?
                    >>> "divisible_seventeen" in globals().keys()
                    True
                    >>> ## Note that the solution in this test file is the wrong type!
                    >>> isinstance(divisible_seventeen, type(divisible_seventeen_soln))
                    False
                    >>> ## Does it have the right type?
                    >>> isinstance(divisible_seventeen, list)
                    True
                    >>> ## Do its contents have the right type?
                    >>> isinstance(divisible_seventeen[0], int)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Note that 0 is divisible by 17
                    >>> divisible_seventeen[0]
                    0
                    >>> ## The first thing after 0 is 17
                    >>> divisible_seventeen[1]
                    17
                    >>> ## Does the variable have the right value
                    >>> all([soln == answr for soln, answr in zip(divisible_seventeen_soln, divisible_seventeen)])
                    True
                    >>> ## Don't go beyond what was asked for
                    >>> divisible_seventeen[-1] < 1000
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> divisible_seventeen_soln = (ii for ii in range(987) if not ii % 17)
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
