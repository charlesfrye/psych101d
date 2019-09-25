test = {
    "name": "bootstrap sampling",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Is the mean of your bootstrapped means close to the truth?
                    >>> np.abs(np.mean(boot_mus) - true_mu) <= 5 * true_sem
                    True
                    >>> ## Is the spread of your bootstrapped means about waht we'd expect?
                    >>> np.abs(np.std(boot_mus) - true_sem) <= 0.2
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> true_sem = true_sigma / np.sqrt(N)
            >>> bound = 5 * true_sem
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
