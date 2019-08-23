test = {
    "name": "root stats",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Attacker never rolls lower than defender
                    >>> all((roll_df.attacker - roll_df.defender)  >= 0)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## This checks your model statistics to determine if they're close to correct.
                    >>> ## If you fail this test, your model is almost definitely wrongly specified.
                    >>> np.abs(deltas.mean() - delta_mean_estimate) <= 0.15
                    True
                    >>> deltas.median() == delta_median
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## This checks your computed statistics: mean hits, chance zero, etc.
                    >>> ## If you fail this test but pass the others,
                    >>> ## you're computing the statistics incorrectly.
                    >>> np.abs(attacker_mean - attacker_mean_estimate) <= 0.12
                    True
                    >>> np.abs(defender_mean - defender_mean_estimate) <= 0.1
                    True
                    >>> np.abs(attacker_chance_zero - chance_zero_estimate) <= 0.04
                    True
                    >>> np.abs(mean_difference - delta_mean_estimate) <= 0.15
                    True
                    >>> median_difference == delta_median
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> root_samples = util.sample_from(root_model, draws=1000, chains=1, progressbar=False)
            >>> root_df = util.samples_to_dataframe(root_samples)
            >>> attacker_mean_estimate = 2.12
            >>> defender_mean_estimate = 0.87
            >>> chance_zero_estimate = 0.06
            >>> delta_mean_estimate = 1.25
            >>> delta_median = 1.0
            >>> deltas = (root_df["attacker"] - root_df["defender"])
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
