test = {
    "name": "For 3: Letters and Numbers",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variable?
                    >>> "letters_and_index" in globals().keys()
                    True
                    >>> ## Does it have the right type?
                    >>> isinstance(letters_and_index, list)
                    True
                    >>> ## Do its contents have the right type?
                    >>> isinstance(letters_and_index[0], list)
                    True
                    >>> ## Do its contents have the right type?
                    >>> isinstance(letters_and_index[0][0], str)
                    True
                    >>> isinstance(letters_and_index[0][1], int)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Does the variable have the right value
                    >>> all([soln == answr for soln, answr in zip(letters_and_index_soln, letters_and_index)])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> letters_and_index_soln = utils.json_ok.load("letters_and_index")
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
