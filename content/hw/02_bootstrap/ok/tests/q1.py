test = {
    "name": "Descriptive Stats 1: Mean",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variable?
                    >>> "mean" in globals().keys()
                    True
                    >>> ## Does it have the right type?
                    >>> callable(mean)
                    True
                    >>> ## Did you avoid calling built-in .mean functions?
                    >>> all([pattern not in inspect.getsource(mean) for pattern in patterns])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Does it give the right answer on random inputs?
                    >>> all([np.isclose(mean(sample), sample.mean()) for sample in random_samples])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> patterns = [".mean", "np.mean"]
            >>> random_sample_sizes = [random.randint(2, 100) for _ in range(20)]
            >>> random_samples = [[random.randint(-100, 100) for _ in range(size)] for size in random_sample_sizes]
            >>> random_samples = [pd.Series(random_sample) for random_sample in random_samples]
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
