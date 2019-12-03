test = {
    "name": "One-way 2: encode_data_oneway_model",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> encoded_data = encode_data_oneway_model(test_data, 3)
                    >>> # There should be one row for each observation
                    >>> len(encoded_data)
                    4
                    >>> len(encoded_data.columns)
                    3
                    >>> # The first column is all 1s
                    >>> all(encoded_data.iloc[:, 0] == 1)
                    True
                    >>> # Checking that the number of 1s in each column is correct
                    >>> encoded_data.apply(sum).equals(pd.Series([4, 2, 1]))
                    True
                    >>> # Checking that the number of 1s in each row is correct
                    >>> all(encoded_data.apply(sum, axis=1) == pd.Series([1, 2, 2, 2]))
                    True
                    >>> # Checking whether the second data point, from index 2, is coded correctly
                    >>> all(encoded_data.iloc[1] == [1, 0, 1])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": """
            >>> test_data = pd.Series([0, 2, 1, 1])
            """,
            "teardown": "",
            "type": "doctest"}]
        }
