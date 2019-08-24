test = {
    "name": "sort",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## is numbers_in_order defined?
                    >>> "numbers_in_order" in globals()
                    True
                    >>> ## is numbers_in_order a list?
                    >>> isinstance(numbers_in_order, list)
                    True
                    >>> ## does it have the numbers in order?
                    >>> numbers_in_order == [1, 2, 3]
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": "",
            "teardown": "",
            "type": "doctest"}]
        }
