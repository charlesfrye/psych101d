test = {
    "name": "2: Converting samples to DataFrames",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # Is the attention column correct?
                    >>> example_df["attention"].value_counts().sort_index()
                    divided    10
                    focused    10
                    Name: attention, dtype: int64
                    >>> # Is the attention column correct?
                    >>> example_df["solutions"].value_counts()
                    3    20
                    Name: solutions, dtype: int64
                    >>> # Is the spread of the values reasonable?
                    >>> example_df["score"].std() > 0
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> divided_selector = example_df["attention"] == "divided"
                    >>> focused_selector = example_df["attention"] == "focused"
                    >>> scores = example_df["score"]
                    >>> divided_scores = scores[divided_selector]
                    >>> focused_scores = scores[focused_selector]
                    >>> t = scipy.stats.ttest_ind(divided_scores, focused_scores)[0]
                    >>> # Can t be calculated correctly from it?
                    >>> np.isclose(compute_t_attention(example_df, 3), t)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": """
            >>> example_sample = null_model_t_easy_samples_df.iloc[0]
            >>> example_df = null_sample_to_dataframe(example_sample, 3)
            """,
            "teardown": "",
            "type": "doctest"}]
        }
