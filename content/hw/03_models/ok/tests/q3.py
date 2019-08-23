test = {
    "name": "maximum",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> max_model.logp({"X": 0, "Y": 1}) == 0
                    True
                    >>> max_model.logp({"X": 1, "Y": 1}) == -np.inf
                    True
                    >>> all([max_sample["Z"] == 1 for max_sample in max_samples])
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> max_samples = util.sample_from(max_model, draws=2, n_init=0, tune=0, chains=1, progressbar=False)""",
            "teardown": r"""
            >>> del max_samples""",
            "type": "doctest"}]
        }
