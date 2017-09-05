"""
Created by Tom Cuypers
"""

import logging
import unittest


def load_suites():
    """
    Find all test cases
    :return:
    """
    loader = unittest.TestLoader()
    suite1 = loader.discover('playlistbuilder', pattern="*_test.py")
    return unittest.TestSuite((suite1))

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(levelname)-7s [%(module)-15s] %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)
    suites = load_suites()
    unittest.TextTestRunner(verbosity=2).run(suites)
