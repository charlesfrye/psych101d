test = {
    "name": "Multiway 3: encode_parameters_twobytwo_model",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## These tests check your code on the example given
                    >>> encoded_test_means = encode_parameters_twobytwo_model(test_means)
                    >>> # The first parameter is equal to the test mean
                    >>> encoded_test_means.iloc[0]
                    1
                    >>> # If you fail this test, you might have rows and columns switched
                    >>> encoded_test_means.iloc[1] != 1
                    True
                    >>> # The second parameter is the difference between 0,0 and 1,0
                    >>> encoded_test_means.iloc[1] == 0
                    True
                    >>> # If you fail this test, you've calculated the interaction parameter incorrectly
                    >>> encoded_test_means[3]
                    2
                    >>> ## These tests check your code on a random example
                    >>> encoded_random = encode_parameters_twobytwo_model(random_means)
                    >>> # The first parameter is just the first mean
                    >>> np.isclose(encoded_random.iloc[0], random_means[0, 0])
                    True
                    >>> # If you fail this test, you might have the rows and columns switched
                    >>> not np.isclose(encoded_random[1], random_means[0, 1] - random_means[0, 0])
                    True
                    >>> # The second parameter is the difference between 0,0 and 1,0
                    >>> np.isclose(encoded_random.iloc[1], random_means[1, 0] - random_means[0, 0])
                    True
                    >>> # If you fail this test, you've calculated the interaction parameter incorrectly
                    >>> np.isclose(encoded_random.iloc[3], random_means[1, 1] - encoded_random[2] - encoded_random[1] - encoded_random[0])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": """
            >>> test_means = np.array([[1, 2], [1, 4]])
            >>> random_means = np.random.standard_normal(size=(2, 2))
            """,
            "teardown": "",
            "type": "doctest"}]
        }
