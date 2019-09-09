test = {
    "name": "Descriptive Stats 4: Median",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variable?
                    >>> "median" in globals().keys()
                    True
                    >>> ## Does it have the right type?
                    >>> callable(median)
                    True
                    >>> ## Did you avoid calling built-in functions?
                    >>> all([pattern not in inspect.getsource(median) for pattern in patterns])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Does it give the right answer on random inputs?
                    >>> all([median(sample) == sample.median() for sample in random_samples])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> patterns = [".median", "np.median", ".quantile", "np.percentile"]
            >>> random_sample_sizes = [random.randint(2, 100) for _ in range(20)]
            >>> random_samples = [[random.randint(-100, 100) for _ in range(size)] for size in random_sample_sizes]
            >>> random_samples = [pd.Series(random_sample) for random_sample in random_samples]
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
