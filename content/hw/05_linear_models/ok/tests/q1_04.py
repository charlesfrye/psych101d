test = {
    "name": "Regression 4: mse_predictions and variance_explained",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Checking mse_predictions
                    >>> # If the predictions are equal to the values, mse is 0
                    >>> np.isclose(mse_predictions(random_values, random_values), 0)
                    True
                    >>> # Be careful if you're using .var method -- the ddof kwarg defaults to 1
                    >>> not np.isclose(mse_predictions(all_mean_prediction, random_values), random_values.var())
                    True
                    >>> # Test values and predictions differ by exactly one, so mse is 1
                    >>> np.isclose(mse_predictions(test_predictions, test_values), 1)
                    True
                    >>> # If the mean is used as predictor, mse is the same as variance
                    >>> np.isclose(mse_predictions(all_mean_prediction, random_values), random_values.var(ddof=0))
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Checking variance_explained
                    >>> # If the predictions are equal to the values, result is 1
                    >>> np.isclose(variance_explained(random_values, random_values), 1)
                    True
                    >>> # If the mean is used as predictor, result is 0
                    >>> np.isclose(variance_explained(all_mean_prediction, random_values), 0)
                    True
                    >>> # Check that the value is correct on the specific test values
                    >>> np.isclose(variance_explained(test_predictions, test_values), test_true_variance_explained)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }

            ],
            "setup": """
            >>> random_values = pd.Series(np.random.standard_normal(size=10))
            >>> all_mean_prediction = pd.Series([random_values.mean()] * len(random_values))
            >>> test_values = pd.Series([2, 4, 6, 8])
            >>> test_predictions = test_values - 1
            >>> test_true_variance_explained = 0.8
            """,
            "teardown": "",
            "type": "doctest"}]
        }
