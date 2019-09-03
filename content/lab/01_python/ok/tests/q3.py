test = {
    "name": "Cleaning the Temp and Turbidity columns",
    "points": 2,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## did you define the water_temp column?
                    >>> "water_temp" in beach.columns
                    True
                    >>> ## are all of the 0s gone from water_temp?
                    >>> np.nanmin(beach.water_temp) > 0
                    True
                    >>> ## are all of the 0s gone from turbidity?
                    >>> np.nanmin(beach.turbidity) > 0
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
