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
                    >>> isinstance(atten_solu_group_means, pd.Series)
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
                    >>> list(sorted(atten_solu_group_means.values))
                    [4.0, 4.95, 6.4, 6.7, 6.7, 7.0]
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> import pandas.core.groupby.groupby as pd_groupby
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
