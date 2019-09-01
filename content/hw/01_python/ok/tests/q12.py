test = {
    "name": "If 2: I Say ayy, You Say lmao",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variable?
                    >>> "ayy_lmao" in globals().keys()
                    True
                    >>> ## Make sure it's a function
                    >>> callable(ayy_lmao)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Does it work on the special input?
                    >>> ayy_lmao("ayy")
                    lmao
                    >>> ## Does it work on other, similar inputs?
                    >>> ayy_lmao("aYy")
                    >>> ayy_lmao("ayy ")
                    >>> ## Does it work on random inputs?
                    >>> all([ayy_lmao(rand) is None for rand in random_inputs])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> random_ints = [random.randint(-100, 100) for _ in range(20)]
            >>> random_strs = [random.choice(string.ascii_letters) for _ in range(20)]
            >>> random_inputs = random_ints + random_strs
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
