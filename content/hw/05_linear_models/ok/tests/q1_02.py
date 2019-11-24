test = {
    "name": "Regression 2: encode_data_linear_regression",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # The first column is all 1s
                    >>> all(encoded_random_series.iloc[:, 0] == 1)
                    True
                    >>> # The second column is equal to the input
                    >>> all(encoded_random_series.iloc[:, 1] == random_series)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": """
            >>> random_series = pd.Series(np.random.standard_normal(size=10))
            >>> encoded_random_series = encode_data_linear_regression(random_series)
            """,
            "teardown": "",
            "type": "doctest"}]
        }
