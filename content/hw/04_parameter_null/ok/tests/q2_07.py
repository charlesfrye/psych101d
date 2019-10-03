test = {
        "name": "2: Estimating p and the null distribution of t, easy task",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # Is the center of the distribution plausible?
                    >>> np.abs(null_samples.mean() - true_mu_t) < sem_bound
                    True
                    >>> # Is the spread of the distribution reasonable?
                    >>> np.abs(null_samples.var() - true_var_t) < sev_bound
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Is the value of p reasonable?
                    >>> 0.5 < easy_p_pymc < 0.6
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": """
            >>> null_samples = pd.Series(pymc_null_ts_easy)
            >>> n_samples = len(null_samples)
            >>> df = 18
            >>> true_mu_t = 0
            >>> true_var_t = bound.compute_var_t(df)
            >>> sem_bound = bound.get_bound_t_mean(n_samples, df=df)
            >>> sev_bound = bound.get_bound_t_variance(n_samples, df=df)
            """,
            "teardown": "",
            "type": "doctest"}]
        }
