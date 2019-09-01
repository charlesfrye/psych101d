test = {
    "name": "Lists 2: Addresses on Conch St",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variable?
                    >>> "conch_st_addresses" in globals().keys()
                    True
                    >>> ## Does it have the right type?
                    >>> isinstance(conch_st_addresses, list)
                    True
                    >>> ## Does it have the right number of entries?
                    >>> len(conch_st_addresses)
                    3
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Does the variable have the right value
                    >>> all([soln == answr for soln, answr in zip(conch_st_addresses_soln, conch_st_addresses)])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> conch_st_addresses_soln = utils.json_ok.load("conch_st_addresses")
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
