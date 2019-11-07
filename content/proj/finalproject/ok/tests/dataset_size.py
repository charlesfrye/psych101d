test = {
    "name": "Dataset Size Check",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # IF YOU FAIL THIS TEST, YOUR DATASET IS TOO BIG
                    >>> # Consider removing unused columns or
                    >>> # reducing the number of rows.
                    >>> os.path.getsize(data_path) / 1024 / 1024 < 1
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> import os
            >>> data_path = "data/data.csv"
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
