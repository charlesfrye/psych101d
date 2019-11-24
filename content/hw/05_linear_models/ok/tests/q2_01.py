test = {
    "name": "One-way 1: make_predictions_oneway",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # If the means are all 0, all predictions are 0
                    >>> all(make_predictions_oneway(pd.Series(np.random.randint(10)), pd.Series([0] * 10)) == 0)
                    True
                    >>> # The predictions should be equal to the means
                    >>> all(make_predictions_oneway(pd.Series(range(10)), random_means) == random_means)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": """
            >>> random_means = pd.Series(np.random.randint(30, size=10))
            """,
            "teardown": "",
            "type": "doctest"}]
        }
