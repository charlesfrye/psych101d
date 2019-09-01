test = {
    "name": "If 3: The Loneliest Number",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variable?
                    >>> "is_number_one" in globals().keys()
                    True
                    >>> ## Make sure it's a function
                    >>> callable(is_number_one)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Does it work on the special input?
                    >>> is_number_one(1)
                    1
                    >>> ## Does it work on other, similar inputs?
                    >>> is_number_one("1")
                    >>> is_number_one("one")
                    >>> ## Does it work on random inputs?
                    >>> all([is_number_one(rand) is None for rand in random_inputs if rand != 1])
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
