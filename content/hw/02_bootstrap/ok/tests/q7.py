test = {
    "name": "groupby 1: single grouping",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variables?
                    >>> "expt_groupby_atten" in globals().keys()
                    True
                    >>> "atten_group_means" in globals().keys()
                    True
                    >>> ## Do they have the right types?
                    >>> isinstance(expt_groupby_atten, pd_groupby.DataFrameGroupBy)
                    True
                    >>> isinstance(atten_group_means, pd.Series)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Are the correct keys present?
                    >>> "divided" in expt_groupby_atten.groups.keys()
                    True
                    >>> "focused" in expt_groupby_atten.groups.keys()
                    True
                    >>> ## Are the values approximately correct?
                    >>> np.round(atten_group_means["divided"], 3)
                    5.117
                    >>> np.round(atten_group_means["focused"], 3)
                    6.8
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
