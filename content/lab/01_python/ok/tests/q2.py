test = {
    "name": "Computing depth_null_frac",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## did you define the depth_null_frac?
                    >>> "depth_null_frac" in globals().keys()
                    True
                    >>> ## did you compute the correct depth_null_frac?
                    >>> np.round(depth_null_frac, 2)
                    0.71
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
