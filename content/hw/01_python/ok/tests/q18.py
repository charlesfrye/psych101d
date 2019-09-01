test = {
    "name": "With 1: Safe Sandwich",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variable?
                    >>> "safely_make_sandwich" in globals().keys()
                    True
                    >>> ## Make sure it's a function
                    >>> callable(safely_make_sandwich)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Does it work on the provided case?
                    >>> sandwicher = Sandwicher()
                    >>> safely_make_sandwich(sandwicher, ["peanut butter", "jelly", "peanut butter"])
                    bread
                    peanut butter
                    jelly
                    peanut butter
                    bread
                    >>> safely_make_sandwich(sandwicher, ["toast"])
                    bread
                    toast
                    bread
                    >>> safely_make_sandwich(sandwicher, [])
                    bread
                    bread
                    >>> ## Did you use the sandwicher?
                    >>> sandwicher.entrances
                    3
                    >>> sandwicher.entrances == sandwicher.exits
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""""",
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
