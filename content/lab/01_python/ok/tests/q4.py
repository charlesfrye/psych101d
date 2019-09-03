test = {
    "name": "Adding time and year columns",
    "points": 2,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## did you define a time column?
                    >>> "time" in beach.columns
                    True
                    >>> ## is the time column of the correct type?
                    >>> isinstance(beach.time.iloc[0], pd.datetime)
                    True
                    >>> ## does a randomly chosen row have the correct value?
                    >>> random_time = random_row.time.iloc[0]
                    >>> random_time == pd.to_datetime(beach_raw["Measurement Timestamp"].loc[random_index])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> random_row = beach.sample(1)
            >>> random_index = random_row.index[0]
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
