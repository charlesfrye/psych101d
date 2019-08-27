test = {
    "name": "Problem +1",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## This checks whether you included the magic bonus or not
                    >>> ## If you fail this test,
                    >>> ## make sure the magic_bonus is included and equal to 1.
                    >>> damage_on_hits.min() == 3
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## This checks your computed statistics: mean hits, chance zero, etc.
                    >>> ## If you fail this test,
                    >>> ## you're computing the statistics incorrectly.
                    >>> np.abs(gs1_hit_chance - gs1_hit) <= 5 * gs1_hit_sem
                    True
                    >>> np.abs(gs1_avg_dmg - gs1_avg_estimate) <= 0.6
                    True
                    >>> np.abs(gs1_avg_dmg_crit - gs1_avg_crit) <= 4 * gs1_avg_crit_sem
                    True
                    >>> np.abs(gs1_std_dmg - gs1_std_estimate) <= 0.5
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> gs1_samples = util.sample_from(greatsword_plusone_model, draws=100, chains=10)
            >>> gs1_df = util.samples_to_dataframe(gs1_samples)
            >>> damage_on_hits = gs1_df[gs1_df.attack_hit].total_damage
            >>> gs1_hit = 0.35
            >>> gs1_crit_chance = gs1_hit * 0.1
            >>> gs1_hit_sem = np.sqrt(.35 * .65 / 1000)
            >>> gs1_avg_estimate = 3.10
            >>> gs1_avg_crit = 2 * 8
            >>> gs1_crit_var = 4 * ((7 - 2  + 1)  ** 2 - 1) / 12
            >>> gs1_avg_crit_sem = np.sqrt(gs1_crit_var / gs1_crit_chance * 1000)
            >>> gs1_std_estimate = 4.7
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
