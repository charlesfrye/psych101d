test = {
    "name": "The Office 3: Sorting",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define all of the variables?
                    >>> "lowest_rated" in globals().keys()
                    True
                    >>> "highest_rated" in globals().keys()
                    True
                    >>> isinstance(lowest_rated, pd.Series)
                    True
                    >>> isinstance(highest_rated, pd.Series)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## do you have the ratings correct?
                    >>> lowest_rated["IMDB Rating"]
                    6.7
                    >>> highest_rated["IMDB Rating"]
                    9.7
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
