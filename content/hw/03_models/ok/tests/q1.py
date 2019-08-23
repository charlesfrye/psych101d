test = {
    "name": "coin toss",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> "coin" == coin_toss_model.vars[0].name # did you define coin?
                    True
                    >>> coin_toss_model.logp({"coin": 0}) == coin_toss_model.logp({"coin": 1})
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
