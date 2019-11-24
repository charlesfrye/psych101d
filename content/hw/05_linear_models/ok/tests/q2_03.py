test = {
    "name": "One-way 3: encode_parameters_oneway_model",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # If all means are 0, all parameters should be 0
                    >>> all(encode_parameters_oneway_model(zero_means) == 0)
                    True
                    >>> encoded_random_means = encode_parameters_oneway_model(random_means)
                    >>> # The first parameter is just the first mean
                    >>> np.isclose(encoded_random_means.iloc[0], random_means[0])
                    True
                    >>> # The second parameter is the difference between the first two means
                    >>> np.isclose(encoded_random_means.iloc[1], random_means[1] - random_means[0])
                    True
                    >>> # That holds for all parameters except the first
                    >>> np.isclose(encoded_random_means.iloc[random_index], random_means[random_index] - random_means[0])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": """
            >>> zero_means = pd.Series([0] * 5)
            >>> random_length = np.random.randint(2, 5)
            >>> random_means = pd.Series(np.random.standard_normal(size=random_length))
            >>> random_index = np.random.randint(1, random_length)
            """,
            "teardown": "",
            "type": "doctest"}]
        }
