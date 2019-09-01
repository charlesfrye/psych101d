test = {
    "name": "The Office 2: Selection",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define all of the variables?
                    >>> "highly_voted" in globals().keys()
                    True
                    >>> "seasons_2_through_5" in globals().keys()
                    True
                    >>> isinstance(seasons_2_through_5, pd.DataFrame)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## do you have the highly voted episodes correct?
                    >>> len(highly_voted) == 15
                    True
                    >>> list(sorted(highly_voted.index))
                    [0, 1, 4, 6, 17, 27, 28, 50, 59, 64, 77, 94, 132, 137, 187]
                    >>> ## did you select only episodes in season 2 or later
                    >>> all(seasons_2_through_5["Season"] >= 2)
                    True
                    >>> ## did you select only episodes in season 5 or earlier
                    >>> all(seasons_2_through_5["Season"] <= 5)
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
