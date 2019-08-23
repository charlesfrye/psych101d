test = {
    "name": "caffeine",
    "points": 2,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## This checks your model statistics to determine if they're close to correct.
                    >>> ## If you fail this test, your model is almost definitely wrongly specified.
                    >>> all(np.abs(z_means) < 7) # sample means are plausible
                    True
                    >>> all(np.abs(z_vars) < 7) # sample variances are plausible
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> sec_caff_samples = util.sample_from(second_caffeine_model, draws=1000, chains=1, progressbar=False)
            >>> sec_caff_df = util.samples_to_dataframe(sec_caff_samples)
            >>> alertness = sec_caff_df["alertness_score"]
            >>> no_caff_selector = sec_caff_df["has_caffeine"] == 0.0
            >>> caff_selector = ~no_caff_selector
            >>> selectors = [no_caff_selector, caff_selector]
            >>> true_mus, true_sds = [10, 12], [0.5, 2]
            >>> true_vars = np.square(true_sds)
            >>> sem_values = util.compute_sem(true_sds, selectors)
            >>> sev_values = util.compute_sev(true_sds, selectors)
            >>> z_means = util.standardize_all(alertness, selectors, true_mus, sem_values)
            >>> z_vars = util.standardize_all(alertness, selectors, true_vars, sev_values, lambda d: d.var())
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
