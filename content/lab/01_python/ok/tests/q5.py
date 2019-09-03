test = {
    "name": "Defining clean_beach",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## did you define clean_beach?
                    >>> "clean_beach" in globals().keys()
                    True
                    >>> ## did you define all of the columns?
                    >>> list(sorted(clean_beach.columns))
                    ['log10_turbidity', 'name', 'time', 'turbidity', 'water_temp', 'year']
                    >>> ## are the year values correct?
                    >>> np.nanmin(clean_beach.year) > 2013
                    True
                    >>> np.nanmax(clean_beach.year) < 2016
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""""",
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
