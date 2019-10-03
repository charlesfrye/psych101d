test = {
    "name": "2: Computing t from a series",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # check whether you're using the built-in scipy f'n
                    >>> utils.util.check_for_scipy(compute_t)
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # the value of t on two series with the same mean is 0
                    >>> np.isclose(compute_t(simple_series, simple_series), 0)
                    True
                    >>> # the value of t on these series is sqrt(2) / 2,
                    >>> # as can be verified by hand
                    >>> np.isclose(compute_t(known_val_series[0], known_val_series[1]), np.sqrt(2) / 2)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": """
            >>> simple_series = pd.Series([1, 2, 3])
            >>> known_val_series = (pd.Series([3, 5]), pd.Series([2, 4]))
            """,
            "teardown": "",
            "type": "doctest"}]
        }
