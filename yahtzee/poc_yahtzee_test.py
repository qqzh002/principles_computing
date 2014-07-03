"""
Test suite for Yahtzee.
"""

from poc_simpletest import TestSuite
import poc_yahtzee_template as yahtzee

def run_test():
    """
    Run test for Yahtzee.
    """

    suite = TestSuite()

    suite.run_test(yahtzee.score((1, 2, 3, 4, 5)), 5, "Test #1a: score")
    suite.run_test(yahtzee.score((1, 1, 1, 1, 5)), 5, "Test #1b: score")
    suite.run_test(yahtzee.score((2, 2, 2, 2, 5)), 8, "Test #1c: score")
    suite.run_test(yahtzee.score((2, 2, 2, 3, 3)), 6, "Test #1d: score")
    suite.run_test(yahtzee.score((2, 2, 2, 4, 4)), 8, "Test #1e: score")
    suite.run_test(yahtzee.score((5, 5, 6, 6, 6)), 18, "Test #1f: score")

    suite.run_test(yahtzee.expected_value((6, 6, 6, 6), 6, 1), 25.0, \
        "Test #2a: expected_value")
    suite.run_test(yahtzee.expected_value((1, 1, 1, 1), 5, 1), 4.4, \
        "Test #2b: expected_value")
    suite.run_test(yahtzee.expected_value((1, 1, 1, 1), 4, 1), 4.25, \
        "Test #2c: expected_value")
    suite.run_test(yahtzee.expected_value((6, 6, 6), 6, 2), 20.0, \
        "Test #2d: expected_value")
    suite.run_test(yahtzee.expected_value((2, 2, 2), 6, 2), 7.0, \
        "Test #2e: expected_value")
    suite.run_test(yahtzee.expected_value((3, 3), 8, 5), 11.3590087891, \
        "Test #2f: expected_value")

    suite.run_test(yahtzee.gen_all_holds((1, 1, 1, 1, 1)), \
        set([(), (1,), (1, 1), (1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1, 1)]), \
        "Test #3a: gen_all_holds")
    suite.run_test(yahtzee.gen_all_holds((1, 1, 1, 1, 6)), \
        set([(), (1,), (1, 1), (1, 1, 1), (1, 1, 1, 1), \
            (6,), (1, 6), (1, 1, 6), (1, 1, 1, 6), (1, 1, 1, 1, 6)]), \
        "Test #3b: gen_all_holds")
    suite.run_test(yahtzee.gen_all_holds((1, 2, 3)), \
        set([(), (1,), (1, 2), (1, 2, 3), (1, 3), (2,), (2, 3), (3,)]), \
        "Test #3c: gen_all_holds")

    suite.run_test(yahtzee.strategy((6, 6, 6, 6, 1), 6), \
        (yahtzee.expected_value((6, 6, 6, 6), 6, 1), (6, 6, 6, 6)), \
        "Test #4: strategy")

    suite.report_results()

run_test()
