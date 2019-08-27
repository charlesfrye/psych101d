test = {
    "name": "greatsword stats",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## This checks your computed statistics: mean hits, chance zero, etc.
                    >>> ## If you fail this test,
                    >>> ## you're computing the statistics incorrectly.
                    >>> np.abs(gs_hit_chance - gs_hit) <= 5 * gs_hit_sem
                    True
                    >>> np.abs(gs_avg_dmg - gs_avg_estimate) <= 0.55
                    True
                    >>> np.abs(gs_avg_dmg_crit - gs_avg_crit) <= 4.5 * gs_avg_crit_sem
                    True
                    >>> np.abs(gs_std_dmg - gs_std_estimate) <= 0.5
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> gs_hit = 0.30
            >>> gs_crit_chance = gs_hit * 0.1
            >>> gs_hit_sem = np.sqrt(.3 * .7 / 1000)
            >>> gs_avg_estimate = 2.366
            >>> gs_avg_crit = 4 * 3.5
            >>> gs_crit_var = 4 * ((6 - 1  + 1)  ** 2 - 1) / 12
            >>> gs_avg_crit_sem = np.sqrt(gs_crit_var / gs_crit_chance * 1000)
            >>> gs_std_estimate = 4
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
