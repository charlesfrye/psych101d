test = {
    "name": "Bootstrapping 1: bootstrap_stat",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define the right variable?
                    >>> "bootstrap_stat" in globals().keys()
                    True
                    >>> ## Does it have the right type?
                    >>> callable(bootstrap_stat)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> bootstrap_means = bootstrap_stat(sample, np.mean, n_boots)
                    >>> ## Did you forget to put replace=False?
                    >>> not np.allclose(bootstrap_means, sample.mean())
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> bootstrap_means = bootstrap_stat(sample, np.mean, n_boots)
                    >>> ## Is the mean of your bootstrap means within reason?
                    >>> mean_bootstrap_means = np.mean(bootstrap_means)
                    >>> np.abs(mean_bootstrap_means - true_mean_bsm) / boot_sem < 4
                    True
                    >>> ## Is the variance of your bootstrap means within reason?
                    >>> variance_bootstrap_means = np.var(bootstrap_means)
                    >>> np.abs(variance_bootstrap_means - true_variance_bsm) / boot_sev < 4
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> n, n_boots = 100, 1000
            >>> sample = pd.Series(np.random.normal(size=n))
            >>> true_mean_bsm = sample.mean()
            >>> true_variance_bsm = (n - 1) / (n ** 2) * sample.var(ddof=1)
            >>> boot_sem = np.sqrt(true_variance_bsm / n_boots)
            >>> boot_sev = true_variance_bsm * np.sqrt(2 / (n_boots - 1))
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
