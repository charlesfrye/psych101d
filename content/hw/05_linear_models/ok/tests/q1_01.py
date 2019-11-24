test = {
    "name": "Regression 1: make_predictions_linear_regression",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # If slope and intercept are 0, prediction is 0
                    >>> int(make_prediction_linear_regression(random_value, 0, 0))
                    0
                    >>> # If you fail this test, you may have the order of arguments swapped
                    >>> make_prediction_linear_regression(random_value, 0, 1) != 0
                    True
                    >>> # If the slope is 0, then prediction equal to intercept
                    >>> make_prediction_linear_regression(random_value, random_intercept, 0) == random_intercept
                    True
                    >>> # If the slope is 1 and intercept 0, then prediction equal to input
                    >>> make_prediction_linear_regression(random_value, 0, 1) == random_value
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # If slope and intercept are 0, all predictions are 0
                    >>> all(make_predictions_linear_regression(random_observed_values, 0, 0) == 0)
                    True
                    >>> # If you fail this test, you may have the order of arguments swapped
                    >>> all(make_predictions_linear_regression(random_observed_values, 0, 1) != 0)
                    True
                    >>> # If the slope is 0, then all predictions are equal to the intercept
                    >>> all(make_predictions_linear_regression(random_observed_values, random_intercept, 0) == random_intercept)
                    True
                    >>> # If the slope is 1 and intercept 0, then all predictions are equal to the inputs
                    >>> all(make_predictions_linear_regression(random_observed_values, 0, 1) == random_observed_values)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": """
            >>> random_slope, random_intercept = np.random.standard_normal(size=2)
            >>> random_observed_values = pd.Series(np.random.standard_normal(size=10))
            >>> random_value = random_observed_values.iloc[0]
            """,
            "teardown": "",
            "type": "doctest"}]
        }
