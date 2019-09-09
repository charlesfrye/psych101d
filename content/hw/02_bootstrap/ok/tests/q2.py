test = {
    "name": "Descriptive Stats 2: Variance",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variable?
                    >>> "var" in globals().keys()
                    True
                    >>> ## Does it have the right type?
                    >>> callable(var)
                    True
                    >>> ## Did you avoid calling built-in .var functions?
                    >>> all([pattern not in inspect.getsource(var) for pattern in patterns])
                    True
                    >>> ## Did you call your mean function?
                    >>> "mean(" in inspect.getsource(var)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Does it give the right answer on random inputs?
                    >>> all([np.isclose(var(sample), sample.var(ddof=0)) for sample in random_samples])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> patterns = [".var", "np.var"]
            >>> random_sample_sizes = [random.randint(2, 100) for _ in range(20)]
            >>> random_samples = [[random.randint(-100, 100) for _ in range(size)] for size in random_sample_sizes]
            >>> random_samples = [pd.Series(random_sample) for random_sample in random_samples]
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
