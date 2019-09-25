test = {
    "name": "computing surprise",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Is the surprise for the agnostic_model close to correct?
                    >>> np.abs(agnostic_surprise - agnostic_target) <= agnostic_bound
                    True
                    >>> ## Is the surprise for the wrong_model close to correct?
                    >>> np.abs(wrong_surprise - wrong_target) <= wrong_bound
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> agnostic_target = 530
            >>> agnostic_bound = 30
            >>> wrong_target = 30
            >>> wrong_bound = 20
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
