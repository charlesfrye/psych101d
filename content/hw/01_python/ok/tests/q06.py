test = {
    "name": "Functions 3: Functions Making Functions",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variable?
                    >>> "make_times_k" in globals().keys()
                    True
                    >>> ## Make sure it's a function
                    >>> callable(make_times_k)
                    True
                    >>> ## Make sure it returns a function
                    >>> callable(make_times_k(random_ints[0]))
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Does the variable have the right value
                    >>> all([make_times_k(k)(x) == k * x for k, x in zip(2 * random_ints, random_inputs)])
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
