test = {
    "name": "Else 1: Lonely or Not?",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variable?
                    >>> "is_one_or_not" in globals().keys()
                    True
                    >>> ## Is that variable a function?
                    >>> callable(is_one_or_not)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Does it work on special inputs?
                    >>> is_one_or_not(1)
                    1
                    >>> is_one_or_not("1")
                    '1'
                    >>> ## Does it work on random inputs?
                    >>> all([is_one_or_not(rand) == "not_one" for rand in random_inputs if rand != 1])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> random_ints = [random.randint(-100, 100) for _ in range(20)]
            >>> random_strs = [random.choice(string.ascii_letters) for _ in range(20)]
            >>> random_inputs = random_ints + random_strs
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
