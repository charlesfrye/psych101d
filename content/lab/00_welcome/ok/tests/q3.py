test = {
    "name": "hello there",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Does your code give the right output?
                    >>> "hello there" == return_hello_there()
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""""",
            "teardown": r"""""",
            "type": "doctest"}]
        }
