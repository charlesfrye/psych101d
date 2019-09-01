test = {
    "name": "For 4: Letters Pyramid",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variable?
                    >>> "letters_pyramid" in globals().keys()
                    True
                    >>> ## Does it have the right type?
                    >>> isinstance(letters_pyramid, list)
                    True
                    >>> ## Do its contents have the right type?
                    >>> isinstance(letters_pyramid[0], str)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## The first entry should be the empty string
                    >>> letters_pyramid[0]
                    ''
                    >>> ## The last entry should not end with 'z', but with 'y'
                    >>> letters_pyramid[-1][-1]
                    'y'
                    >>> ## Does the variable have the right value
                    >>> all([soln == answr for soln, answr in zip(letters_pyramid_soln, letters_pyramid)])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> letters_pyramid_soln = utils.json_ok.load("letters_pyramid")
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
