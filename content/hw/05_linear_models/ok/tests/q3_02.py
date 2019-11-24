test = {
    "name": "Multiway 2: encode_data_twobytwo_model",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## These tests check whether your code works on the example given
                    >>> encoded_data = encode_data_twobytwo_model(test_factor1_idxs, test_factor2_idxs)
                    >>> # There should be one row for each observation
                    >>> len(encoded_data)
                    3
                    >>> # And four columns: baseline, effect 1, effect 2, interaction
                    >>> len(encoded_data.columns)
                    4
                    >>> # The first column is all 1s
                    >>> all(encoded_data.iloc[:, 0] == 1)
                    True
                    >>> # Checking that the number of 1s in each column is correct
                    >>> encoded_data.apply(sum).equals(pd.Series([3, 2, 1, 1]))
                    True
                    >>> # Checking that the number of 1s in each row is correct
                    >>> all(encoded_data.apply(sum, axis=1) == pd.Series([1, 4, 2]))
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": """
            >>> test_factor1_idxs, test_factor2_idxs = pd.Series([0, 1, 1]), pd.Series([0, 1, 0])
            >>> test_data = pd.Series([0, 2, 1, 1])
            """,
            "teardown": "",
            "type": "doctest"}]
        }
