test = {
    "name": "2: Computing t from a dataframe",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # If this test returns False, you might've switched
                    >>> # the order of the arguments to compute_t
                    >>> compute_t_attention(test_df, num_solutions=3) > 0
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # the value of t on this dataframe is sqrt(2) / 2,
                    >>> # as can be verified by hand
                    >>> np.isclose(compute_t_attention(test_df, num_solutions=3), np.sqrt(2) / 2)
                    True
                    >>> # the value of t shouldn't change if you add a row with solutions != 3
                    >>> np.isclose(compute_t_attention(solution_check_df, 3), np.sqrt(2) / 2)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # if you fail this test, you might have switched easy and hard
                    >>> not np.isclose(hard_t_byhand, -0.6)
                    True
                    >>> # check easy_t_byhand is close to correct value
                    >>> np.round(easy_t_byhand, 4)
                    -0.6
                    >>> # check hard_t_byhand is close to correct value
                    >>> np.round(hard_t_byhand, 4)
                    -4.8321
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": """
            >>> test_df = pd.DataFrame(
                {"attention": ["divided", "divided", "focused", "focused"],
                "score": [3, 5, 2, 4],
                "solutions": [3, 3, 3, 3]}
                )
            >>> solution_check_df = test_df.append(
                {"attention": "focused", "score": 6, "solutions": 1}, ignore_index=True)
            """,
            "teardown": "",
            "type": "doctest"}]
        }
