test = {
    "name": "If 1: is b or not is b",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variable?
                    >>> "is_letter_a" in globals().keys()
                    True
                    >>> ## Make sure it's a function
                    >>> callable(is_letter_a)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Did you change the code at all?
                    >>> is_letter_a("b")
                    >>> ## Does it work on the special input?
                    >>> is_letter_a("a")
                    yup, that's an 'a'
                    >>> ## Does it work on other inputs?
                    >>> is_letter_a(["a"])
                    >>> is_letter_a("A")
                    >>> is_letter_a(" a ")
                    >>> ## Does it work on random inputs?
                    >>> all([is_letter_a(rand) is None for rand in random_inputs if rand != "a"])
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
