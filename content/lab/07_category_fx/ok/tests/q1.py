test = {
    "name": "ANOVA with scipy",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## is the value for F approximately correct?
                    >>> np.isclose(reaction_F, 95.147)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## is the value for p approximately correct?
                    >>> np.greater(reaction_p, 5.0e-39)
                    True
                    >>> np.less(reaction_p, 5.1e-39)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
