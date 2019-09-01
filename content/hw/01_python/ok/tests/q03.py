test = {
    "name": "Dictionaries: An Address Book",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variable?
                    >>> "conch_st_address_bk" in globals().keys()
                    True
                    >>> ## Does it have the right type?
                    >>> isinstance(conch_st_address_bk, dict)
                    True
                    >>> ## Does it have the right number of entries?
                    >>> len(conch_st_address_bk)
                    3
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Does the variable have the right value
                    >>> all([soln == answr for soln, answr in zip(conch_st_address_bk_soln.items(), conch_st_address_bk.items())])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> conch_st_address_bk_soln = utils.json_ok.load("conch_st_address_bk")
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
