test = {
    "name": "Else 2: X Out",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variable?
                    >>> "divisible_seventeen_with_xs" in globals().keys()
                    True
                    >>> ## Note that the solution in this test file is the wrong type!
                    >>> isinstance(divisible_seventeen_with_xs, type(divisible_seventeen_with_xs_soln))
                    False
                    >>> ## Does it have the right type?
                    >>> isinstance(divisible_seventeen_with_xs, list)
                    True
                    >>> ## Do its contents have the right type?
                    >>> isinstance(divisible_seventeen_with_xs[0], int)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Note that 0 is divisible by 17
                    >>> divisible_seventeen_with_xs[0]
                    0
                    >>> ## The first thing after 0 should be an 'x'
                    >>> divisible_seventeen_with_xs[1]
                    'x'
                    >>> ## The result should have a specific length. Don't forget Python indexing!
                    >>> len(divisible_seventeen_with_xs) == 1001
                    True
                    >>> ## Does the variable have the right value
                    >>> all([soln == answr for soln, answr in zip(divisible_seventeen_with_xs_soln, divisible_seventeen_with_xs)])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> divisible_seventeen_with_xs_soln = (ii if not ii % 17 else "x" for ii in range(1001))
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
