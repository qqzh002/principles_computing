"""
Test suite for Solitaire Mancala.
"""

import poc_simpletest
import solitaire_mancala

def run_test():
    """
    Run test for SolitaireMancala class.
    """

    suite = poc_simpletest.TestSuite()
    game = solitaire_mancala.SolitaireMancala()

    suite.run_test(game.configuration, [0], "Test __init__:")

    game.set_board([0, 1, 1, 3, 0, 0, 0])
    suite.run_test(game.configuration, [0, 1, 1, 3, 0, 0, 0], "Test set_board:")

    suite.run_test(str(game), "[0, 0, 0, 3, 1, 1, 0]", "Test __str__:")

    suite.run_test(game.get_num_seeds(-1), None, "Test get_num_seeds #-1:")
    suite.run_test(game.get_num_seeds(0), 0, "Test get_num_seeds #0:")
    suite.run_test(game.get_num_seeds(1), 1, "Test get_num_seeds #1:")
    suite.run_test(game.get_num_seeds(2), 1, "Test get_num_seeds #2:")
    suite.run_test(game.get_num_seeds(3), 3, "Test get_num_seeds #3:")
    suite.run_test(game.get_num_seeds(4), 0, "Test get_num_seeds #4:")
    suite.run_test(game.get_num_seeds(5), 0, "Test get_num_seeds #5:")
    suite.run_test(game.get_num_seeds(6), 0, "Test get_num_seeds #6:")
    suite.run_test(game.get_num_seeds(7), None, "Test get_num_seeds #7:")

    suite.run_test(game.is_legal_move(-1), False, "Test is_legal_move #-1:")
    suite.run_test(game.is_legal_move(0), False, "Test is_legal_move #0:")
    suite.run_test(game.is_legal_move(1), True, "Test is_legal_move #1:")
    suite.run_test(game.is_legal_move(2), False, "Test is_legal_move #2:")
    suite.run_test(game.is_legal_move(3), True, "Test is_legal_move #3:")
    suite.run_test(game.is_legal_move(4), False, "Test is_legal_move #4:")
    suite.run_test(game.is_legal_move(5), False, "Test is_legal_move #5:")
    suite.run_test(game.is_legal_move(6), False, "Test is_legal_move #6:")
    suite.run_test(game.is_legal_move(7), False, "Test is_legal_move #7:")

    suite.run_test(game.plan_moves(), [1, 3, 1, 2, 1], "Test plan_moves:")

    suite.run_test(game.choose_move(), 1, "Test choose_move #1:")
    game.apply_move(1)
    suite.run_test(game.configuration, [1, 0, 1, 3, 0, 0, 0], \
        "Test apply_move #1:")

    suite.run_test(game.choose_move(), 3, "Test choose_move #2:")
    game.apply_move(2)
    suite.run_test(game.configuration, [1, 0, 1, 3, 0, 0, 0], \
        "Test apply_move #2:")
    game.apply_move(3)
    suite.run_test(game.configuration, [2, 1, 2, 0, 0, 0, 0], \
        "Test apply_move #3:")

    suite.run_test(game.is_game_won(), False, "Test is_game_won #1:")
    game.apply_move(1)
    game.apply_move(2)
    game.apply_move(1)
    suite.run_test(game.is_game_won(), True, "Test is_game_won #2:")

    suite.report_results()

run_test()
