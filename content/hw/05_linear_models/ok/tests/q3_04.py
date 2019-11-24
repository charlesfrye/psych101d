test = {
    "name": "Multiway 4: Minimizing Prediction Error",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # Is your variance_explained above the criterion?
                    >>> twobytwo_preds = make_predictions_linear_model(encoded_data, twobytwo_parameters)
                    >>> variance_explained(twobytwo_preds, twobytwo_df["y"]) >= 0.3
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": """
            >>> encoded_data = encode_data_twobytwo_model(twobytwo_df["factor1"], twobytwo_df["factor2"])
            """,
            "teardown": "",
            "type": "doctest"}]
        }
