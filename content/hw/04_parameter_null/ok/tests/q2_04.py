test = {
    "name": "2: Verifying make_null_model_t",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Checking model specification
                    >>> # is there a variable for scores?
                    >>> "scores" in named_RVs.keys()
                    True
                    >>> # is that variable unobserved?
                    >>> "scores" in free_RV_names
                    True
                    >>> # is that variable a Normal variable?
                    >>> score_distribution = named_RVs["scores"].distribution
                    >>> isinstance(score_distribution, pm.Normal)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## Checking sample values
                    >>> # Drawing samples
                    >>> null_samples = shared_util.sample_from(null_model_t_check, chains=4)
                    >>> null_sample_df = shared_util.samples_to_dataframe(null_samples)
                    >>> flat_samples = utils.util.flatten_samples(null_sample_df["scores"])
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
            >>> true_mean, true_sd = 0, 1
            >>> true_var = true_sd ** 2
            >>> group_size = 20
            >>> null_model_t_check = make_null_model_t(
                true_mean, true_sd, group_size=group_size)
            >>> named_RVs = null_model_t_check.named_vars
            >>> free_RVs = null_model_t_check.free_RVs
            >>> free_RV_names = [RV.name for RV in free_RVs]
            >>> sem = bound.compute_sem(true_var, 2 * group_size * 2000)
            >>> sem_bound = 8 * sem
            >>> sev = bound.compute_sev(true_var, 2 * group_size * 2000)
            >>> sev_bound = 8 * sev
            """,
            "teardown": "",
            "type": "doctest"}]
        }
