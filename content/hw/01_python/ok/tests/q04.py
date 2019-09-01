test = {
    "name": "Functions 1: times_ten",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Check on random inputs
                    >>> all([times_ten(rand) == 10 * rand for rand in random_inputs])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> random_inputs = [random.randint(-100, 100) for _ in range(20)]
            >>> random_inputs += [random.choice(string.ascii_letters) for _ in range(20)]
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
