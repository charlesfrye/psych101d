test = {
    "name": "The Office 1: Basics and Indexing",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> ## Did you define all of the variables?
                    >>> "num_episodes" in globals().keys()
                    True
                    >>> "episode_102" in globals().keys()
                    True
                    >>> "on_air_between" in globals().keys()
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> ## do you have the number of episodes correct?
                    >>> num_episodes == len(office_data)
                    True
                    >>> ## did you select episode 102?
                    >>> episode_102
                    Season                    6
                    Episode                  12
                    Title          Scott's Tots
                    IMDB Rating             8.3
                    Total Votes            1981
                    Air Date         3 Dec 2009
                    Name: 102, dtype: object
                    >>> ## are your air dates correct?
                    >>> on_air_between
                    ['24 Mar 2005', '16 May 2013']
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "setup": r"""""",
            "teardown": r"""
            """,
            "type": "doctest"}]
        }
