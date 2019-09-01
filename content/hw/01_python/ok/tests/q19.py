test = {
    "name": "Pandas 1: A Better Address Book",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variable?
                    >>> "conch_st_df" in globals().keys()
                    True
                    >>> isinstance(conch_st_df, pd.DataFrame)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## does your dataframe have the right columns?
                    >>> conch_st_df.columns.tolist()
                    ['address', 'housetype', 'resident']
                    >>> ## does your dataframe have the right index?
                    >>> conch_st_df.index.tolist()
                    [0, 1, 2]
                    >>> ## Who lives in a pineapple under the sea?
                    >>> conch_st_df[conch_st_df.housetype == "Pineapple"].resident.iloc[0]
                    'SpongeBob SquarePants'
                    >>> ## Is the "address" column correct?
                    >>> conch_st_df["address"]
                    0    124 Conch Street
                    1    122 Conch Street
                    2    120 Conch Street
                    Name: address, dtype: object
                    >>> ## Is the "Squidward Tentacles" row present and correct?
                    >>> conch_st_df[conch_st_df.resident == "Squidward Tentacles"].iloc[0]
                    address         122 Conch Street
                    housetype                   Head
                    resident     Squidward Tentacles
                    Name: 1, dtype: object
                    >>> ## Are all of the values correct?
                    >>> np.all(conch_st_df_soln == conch_st_df)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> conch_st_df_soln = pd.read_json(utils.json_ok.ROOT / "conch_st_df.json")
            >>> ## NOTE: your DataFrame is sorted so that the columns are in alphabetical order
            >>> conch_st_df = conch_st_df.sort_index(axis=1)
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
