test = {
    "name": "2: Verifying t and p with scipy",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # if you fail this test, you might have switched easy and hard
                    >>> not hard_p_byhand > 0.1
                    True
                    >>> # check hard_p_byhand is close to correct value
                    >>> np.round(hard_p_byhand, 4)
                    0.0001
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # if you fail this test, you might have switched easy and hard
                    >>> not hard_p_scipy > 0.1
                    True
                    >>> # check hard_p_byhand and _scipy are close to each other
                    >>> np.round(hard_p_byhand, 5) == np.round(hard_p_scipy, 5)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # if you fail this test, you might have switched easy and hard
                    >>> not np.isclose(hard_t_scipy, -0.6)
                    True
                    >>> # check hard_t_scipy is close to correct value
                    >>> np.round(hard_t_scipy, 4)
                    -4.8321
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # check easy_t_scipy is close to correct value
                    >>> np.round(easy_t_scipy, 4)
                    -0.6
                    >>> # check easy_p_scipy is close to correct value
                    >>> np.round(easy_p_scipy, 4)
                    0.556
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": """
            """,
            "teardown": "",
            "type": "doctest"}]
        }
