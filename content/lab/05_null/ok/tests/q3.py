test = {
    "name": "Sampling from the Replication Failure Model",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## This function checks whether the samples from the posterior
                    >>> ## are behaving as expected, using the analytic value of the posterior.
                    >>> ## If you fail this test because it returns False,
                    >>> ## your model is mis-specified or you are sampling incorrectly.
                    >>> utils.bernoulli.check_samples(replication_failure_samples["null_true"], final_posterior)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""
            >>> # First, use Bayes' Rule to calculate the prior for the replicaiton failure
            >>> new_prior = utils.bernoulli.posterior_p(alpha, prior, power)
            >>> # Then, use Bayes' Rule again to calculate the posterior, having observed the replication expt
            >>> final_posterior = utils.bernoulli.posterior_p(alpha, new_prior, power, positive_result=False)
            """,
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
