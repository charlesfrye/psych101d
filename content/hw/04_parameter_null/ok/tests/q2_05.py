test = {
    "name": "2: Sampling from null_model_t",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # Is the average of the values reasonable?
                    >>> np.abs(np.mean(flat_samples) - true_mean) < sem_bound
                    True
                    >>> # Is the spread of the values reasonable?
                    >>> np.abs(np.var(flat_samples) - true_var) < sev_bound
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": """
            >>> null_samples = null_model_t_easy_samples_df
            >>> flat_samples = utils.util.flatten_samples(null_samples["scores"])
            >>> easy_obs = atten_df[atten_df["solutions"] == 3]
            >>> true_mean = easy_obs["score"].mean()
            >>> true_sd = easy_obs.groupby("attention")["score"].std().mean()
            >>> true_var = true_sd ** 2
            >>> group_size = 10
            >>> n_samples =  len(flat_samples)
            >>> assert n_samples >=  10000
            >>> sem = bound.compute_sem(true_var, n_samples)
            >>> sem_bound = 5 * sem
            >>> sev = bound.compute_sev(true_var, n_samples)
            >>> sev_bound = 5 * sev
            """,
            "teardown": "",
            "type": "doctest"}]
        }
