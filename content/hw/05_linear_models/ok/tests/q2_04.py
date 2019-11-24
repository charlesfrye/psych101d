test = {
    "name": "One-way 4: Minimizing Prediction Error",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # Is your variance_explained above the criterion?
                    >>> oneway_preds = make_predictions_linear_model(encoded_data, oneway_parameters)
                    >>> variance_explained(oneway_preds, oneway_df["y"]) >= 0.0
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": """
            >>> encoded_data = encode_data_oneway_model(oneway_df["factor1"], 2)
            """,
            "teardown": "",
            "type": "doctest"}]
        }
