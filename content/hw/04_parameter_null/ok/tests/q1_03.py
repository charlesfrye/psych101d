test = {
    "name": "1: linear_signal_model",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Checking Model
                    >>> # Are Measurement and Signal present?
                    >>> "M" in lsm_sample_df.columns
                    True
                    >>> "S" in lsm_sample_df.columns
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Checking Samples
                    >>> # Is the mean reasonable?
                    >>> np.abs(np.mean(lsm_sample_df["M"]) - true_mu_M) < sem_bound
                    True
                    >>> # Is the variance reasonable?
                    >>> np.abs(np.var(lsm_sample_df["M"]) - true_var_M) < sev_bound
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": """
            >>> lsm_sample_df = linear_signal_model_samples_df
            >>> n_samples = len(lsm_sample_df)
            >>> assert n_samples >= 4000
            >>> true_mu_M = 0.0
            >>> true_var_M = 1.25
            >>> sem = bound.compute_sem(true_var_M, n_samples)
            >>> sem_bound = 5 * sem
            >>> sev = bound.compute_sev(true_var_M, n_samples)
            >>> sev_bound = 6 * sev   # variance of variance estimator oddly high
            """,
            "teardown": "",
            "type": "doctest"}]
        }
