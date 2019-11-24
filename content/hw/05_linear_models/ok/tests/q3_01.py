test = {
    "name": "Multiway 1: make_predictions_twoway",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # This test checks to see if your code works on the example given
                    >>> predictions_on_example = make_predictions_twoway(example_factor1_idxs, example_factor2_idxs, test_means)
                    >>> all(predictions_on_example == [0, 1, 5])
                    True
                    >>> # This test checks to see if you code works for random indices on the same example
                    >>> all(make_predictions_twoway(random_factor1_idxs, random_factor2_idxs, test_means) == test_means[random_factor1_idxs, random_factor2_idxs])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": """
            >>> test_means = np.array([[0, 1, 2], [3, 4, 5]])
            >>> random_factor1_idxs, random_factor2_idxs = np.random.randint(2, size=(2, 5))
            >>> random_factor1_idxs, random_factor2_idxs = pd.Series(random_factor1_idxs), pd.Series(random_factor2_idxs)
            >>> example_factor1_idxs, example_factor2_idxs = pd.Series([0, 0, 1]), pd.Series([0, 1, 2])
            """,
            "teardown": "",
            "type": "doctest"}]
        }
