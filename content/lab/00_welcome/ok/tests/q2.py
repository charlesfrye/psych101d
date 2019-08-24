test = {
    "name": "+ 1",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Check the outputs of add_one on
                    >>> ## a bunch of randomly chosen numbers?
                    >>> random_numbers = [random.randint(-100, 100) for _ in range(100)]
                    >>> ## If you fail this test, add_one is still adding 2
                    >>> not all([add_one(num) == (num + 2) for num in random_numbers])
                    True
                    >>> ## If you fail this test, add_one is not adding 1
                    >>> all([add_one(num) == (num + 1) for num in random_numbers])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> import random""",
            "teardown": r"""""",
            "type": "doctest"}]
        }
