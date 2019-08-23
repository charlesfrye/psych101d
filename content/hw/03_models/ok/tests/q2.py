test = {
    "name": "1 + 1",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> adding_model.logp({"X": 0, "Y": 1}) == -np.inf
                    True
                    >>> adding_model.logp({"X": 1, "Y": 1}) == 0
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
