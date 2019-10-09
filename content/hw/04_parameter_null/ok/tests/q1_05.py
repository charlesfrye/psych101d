test = {
    "name": "1: neurotransmitter_model",
    "points": 2,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Checking Model
                    >>> # Are N vesicles and Voltage present?
                    >>> "N" in ntm_sample_df.columns
                    True
                    >>> "V" in ntm_sample_df.columns
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Checking Samples: Poisson Component
                    >>> # Is the fraction of 0s reasonable?
                    >>> is_0 = ntm_sample_df["V"] == 0
                    >>> p_0 = is_0.mean()
                    >>> var_p_0 = is_0.var()
                    >>> np.abs(p_0 - true_p_0) < sem_p_0_bound
                    True
                    >>> # Is the variance of the 0s reasonable?
                    >>> np.abs(var_p_0 - true_var_p_0) < sev_p_0_bound
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Checking Samples: Normal Component
                    >>> # Is the average reasonable?
                    >>> np.abs(np.mean(ntm_sample_df["V"]) - MC_mean_V) < sem_V_bound
                    True
                    >>> # Is the variance of the 0s reasonable?
                    >>> np.abs(np.var(ntm_sample_df["V"]) - MC_var_V) < sev_V_bound
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }

            ],
            "setup": """
            >>> ntm_sample_df = neurotransmitter_model_samples_df
            >>> n_samples = len(ntm_sample_df)
            >>> assert n_samples >= 4000
            >>> true_p_0 = np.exp(pm.Poisson.dist(mu=2.25).logp(0).eval())
            >>> true_var_p_0 = true_p_0 * (1 - true_p_0)
            >>> sem_p_0 = bound.compute_sem(true_var_p_0, n_samples)
            >>> sem_p_0_bound = 5 * sem_p_0
            >>> sev_p_0 = bound.compute_sev(true_var_p_0, n_samples)
            >>> sev_p_0_bound = 10 * sev_p_0
            >>> MC_mean_V = 0.907 # MC estimated mean
            >>> MC_var_V = 0.377 # MC estimated variance
            >>> sem_V = bound.compute_sem(MC_var_V, n_samples)
            >>> sem_V_bound = 6 * sem_V
            >>> sev_V = bound.compute_sev(MC_var_V, n_samples)
            >>> sev_V_bound = 6 * sev_V
            """,
            "teardown": "",
            "type": "doctest"}]
        }
