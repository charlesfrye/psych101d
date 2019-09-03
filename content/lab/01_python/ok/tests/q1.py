test = {
    "name": "Adding the Name Column",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## does the name exist?
                    >>> "name" in beach.columns
                    True
                    >>> ## does the name column have the right values?
                    >>> list(sorted(beach.name.unique()))
                    ['63rd Street', 'Calumet', 'Montrose', 'Ohio Street', 'Osterman', 'Rainbow']
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
