test = {
    "name": "groupby 2: multiple grouping",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variables?
                    >>> "expt_groupby_atten_solu" in globals().keys()
                    True
                    >>> "atten_solu_group_means" in globals().keys()
                    True
                    >>> ## Do they have the right types?
                    >>> isinstance(expt_groupby_atten_solu, pd_groupby.DataFrameGroupBy)
                    True
                    >>> isinstance(atten_solu_group_means, pd.DataFrame)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Are the correct keys present?
                    >>> ("divided", 1) in expt_groupby_atten_solu.groups.keys()
                    True
                    >>> ("focused", 3) in expt_groupby_atten_solu.groups.keys()
                    True
                    >>> ## Are the values approximately correct?
                    >>> list(sorted(atten_solu_group_means["score"]))
                    [4.0, 4.95, 6.4, 6.7, 6.7, 7.0]
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> import pandas.core.groupby.groupby as pd_groupby
            >>> sample = pd.Series(np.random.normal(size=250))
            >>> left_side, right_side = sample.quantile([0.05, 0.95])
            >>> # the above interval will contain 0 with probability one in 4e11
            >>> eps = 1e-5
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
