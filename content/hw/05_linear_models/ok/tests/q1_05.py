test = {
    "name": "Regression 5: Minimizing Prediction Error",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # Is your variance_explained above the criterion?
                    >>> linear_reg_preds = make_predictions_linear_model(encoded_data, regression_parameters)
                    >>> variance_explained(linear_reg_preds, regression_df["y"]) > 0.4
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": """
            >>> encoded_data = encode_data_linear_regression(regression_df["x"])
            """,
            "teardown": "",
            "type": "doctest"}]
        }
