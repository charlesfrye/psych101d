test = {
    "name": "root",
    "points": 2,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## This checks to make sure your variables are named correctly.
                    >>> "attacker" in root_names
                    True
                    >>> "defender" in root_names
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## This checks your model statistics to determine if they're close to correct.
                    >>> ## If you fail this test, your model is almost definitely wrongly specified.
                    >>> np.abs((root_df["attacker"].mean() - root_mean_estimates[0]) / root_sem_estimate) < sd_cutoff
                    True
                    >>> np.abs((root_df["defender"].mean() - root_mean_estimates[1]) / root_sem_estimate) < sd_cutoff
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> root_samples = util.sample_from(root_model, draws=500, chains=1, progressbar=False)
            >>> root_df = util.samples_to_dataframe(root_samples)
            >>> root_mean_estimates = [2.13, 0.88]
            >>> root_sem_estimate = np.sqrt(0.86 / 500)
            >>> sd_cutoff = 6
            >>> root_names = [deterministic.name for deterministic in root_model.deterministics]
            """,
            "teardown": r"""""",
            "type": "doctest"}]
        }
