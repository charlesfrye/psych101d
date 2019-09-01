test = {
    "name": "The Office 4: Applying",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define all of the variables?
                    >>> "office_data" in globals().keys()
                    True
                    >>> "Air Year" in office_data.columns
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## are the first and last entries correct?
                    >>> office_data.sort_values("Air Year", ascending=False)["Air Year"].iloc[[0, -1]]
                    187    2013
                    0      2005
                    Name: Air Year, dtype: object
                    >>> ## does it have the right mean?
                    >>> np.round(np.mean(np.array(office_data["Air Year"], dtype=np.int)), decimals=4)
                    2009.0372
                    >>> ## and standard deviation?
                    >>> np.round(np.std(np.array(office_data["Air Year"], dtype=np.int)), decimals=4)
                    2.4197
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
