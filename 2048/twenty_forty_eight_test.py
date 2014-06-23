"""
Test suite for 2048.
"""

import poc_simpletest
import twenty_forty_eight

def run_test():
    """
    Run test for TwentyFortyEight class.
    """

    suite = poc_simpletest.TestSuite()

    suite.run_test(twenty_forty_eight.merge([2, 0, 2, 4]), [4, 4, 0, 0], \
        "Test #1a: merge")
    suite.run_test(twenty_forty_eight.merge([0, 0, 2, 2]), [4, 0, 0, 0], \
        "Test #1b: merge")
    suite.run_test(twenty_forty_eight.merge([2, 2, 0, 0]), [4, 0, 0, 0], \
        "Test #1c: merge")
    suite.run_test(twenty_forty_eight.merge([2, 2, 2, 2]), [4, 4, 0, 0], \
        "Test #1d: merge")
    suite.run_test(twenty_forty_eight.merge([8, 16, 16, 8]), [8, 32, 8, 0], \
        "Test #1e: merge")

    game = twenty_forty_eight.TwentyFortyEight(4, 5)

    suite.run_test(str(game), \
        "[[0, 0, 0, 0, 0], " + \
        "[0, 0, 0, 0, 0], " + \
        "[0, 0, 0, 0, 0], " + \
        "[0, 0, 0, 0, 0]]", \
        "Test #2: __init__")

    suite.run_test(game.get_grid_height(), 4, "Test #3a: get_grid_height")
    suite.run_test(game.get_grid_width(), 5, "Test #3b: get_grid_width")

    suite.run_test(game.get_tile(0, 0), 0, "Test #4a: get_tile and set_tile")
    game.set_tile(0, 0, 1)
    suite.run_test(game.get_tile(0, 0), 1, "Test #4b: get_tile and set_tile")
    game.set_tile(2, 3, 4)
    suite.run_test(game.get_tile(2, 3), 4, "Test #4b: get_tile and set_tile")

    game.reset()
    suite.run_test(str(game), \
        "[[0, 0, 0, 0, 0], " + \
        "[0, 0, 0, 0, 0], " + \
        "[0, 0, 0, 0, 0], " + \
        "[0, 0, 0, 0, 0]]", \
        "Test #5: reset")

    # TODO: Test new_tile and move

    suite.report_results()

run_test()
