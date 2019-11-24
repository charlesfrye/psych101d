test = {
    "name": "Regression 3: make_predictions_linear_model",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # When the parameters are all 0, the predictions are 0
                    >>> all(make_predictions_linear_model(encoded_data, pd.Series([0, 0])) == 0)
                    True
                    >>> # If you fail this test, you may have the order backwards
                    >>> all(make_predictions_linear_model(encoded_data, pd.Series([1, 0])) != random_values)
                    True
                    >>> # If the slope is 0, the predictions are always equal to the intercept
                    >>> all(make_predictions_linear_model(encoded_data, pd.Series([1, 0])) == 1)
                    True
                    >>> # If the slope is 1 and the intercept 0, the predictions are always equal to the input
                    >>> all(make_predictions_linear_model(encoded_data, pd.Series([0, 1])) == random_values)
                    True
                    >>> # If the slope is -1 and the intercept 0, the predictions are always equal to the negative input
                    >>> all(make_predictions_linear_model(encoded_data, pd.Series([0, -1])) == -1 * random_values)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## These tests check to make sure you handle the case of more than two parameters correctly
                    >>> all(make_predictions_linear_model(more_than_two_columns, more_than_two_parameters) == additional_column)
                    True
                    >>> all(make_predictions_linear_model(more_than_two_columns, -1 * more_than_two_parameters) == -1 * additional_column)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": """
            >>> random_values = pd.Series(np.random.standard_normal(size=10))
            >>> encoded_data = pd.DataFrame({0: 1, 1: pd.Series(random_values)})
            >>> additional_column = encoded_data[1].apply(lambda x: int(x > 0))
            >>> more_than_two_columns = encoded_data.copy()
            >>> more_than_two_columns[2] = additional_column
            >>> more_than_two_parameters = pd.Series([0, 0, 1])
            """,
            "teardown": "",
            "type": "doctest"}]
        }
