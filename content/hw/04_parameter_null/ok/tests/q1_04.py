test = {
    "name": "1: nhst_model",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Checking Model
                    >>> # Are null_true and result_positive present?
                    >>> "null_true" in nhst_sample_df.columns
                    True
                    >>> "positive_result" in nhst_sample_df.columns
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Checking Samples: Null Component
                    >>> null_true = nhst_sample_df["null_true"]
                    >>> p_est = null_true.mean()
                    >>> var_p_est = null_true.var()
                    >>> # Is the fraction of nulls reasonable?
                    >>> np.abs(p_est - true_p) < sem_p_bound
                    True
                    >>> # Is the variance of the null reasonable?
                    >>> np.abs(var_p_est -  true_var_p) < sev_p_bound
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Checking Samples: Likelihood Component
                    >>> results_column = nhst_sample_df["positive_result"]
                    >>> null_true_selector = nhst_sample_df["null_true"].astype(bool)
                    >>> false_positives = results_column[null_true_selector]
                    >>> eff_n = len(false_positives)
                    >>> sem_alpha_bound = 5 * bound.compute_sem(true_var_alpha, eff_n)
                    >>> sev_alpha_bound = 5 * bound.compute_sev(true_var_alpha, eff_n)
                    >>> # Are the false positives reasonable?
                    >>> np.abs(false_positives.mean() - true_alpha) < sem_alpha_bound
                    True
                    >>> # Is the variance of the false positives reasonable?
                    >>> np.abs(false_positives.var() - true_var_alpha) < sev_alpha_bound
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }

            ],
            "setup": """
            >>> nhst_sample_df = nhst_model_samples_df
            >>> n_samples = len(nhst_sample_df)
            >>> assert n_samples >= 2000
            >>> true_p = 0.2
            >>> true_var_p = (1 - true_p) * true_p
            >>> sem_p_bound = 5 * bound.compute_sem(true_var_p, n_samples)
            >>> sev_p_bound = 5 * bound.compute_sev(true_var_p, n_samples)
            >>> true_alpha = 0.1
            >>> true_var_alpha = (1 - true_alpha) * true_alpha
            """,
            "teardown": "",
            "type": "doctest"}]
        }
