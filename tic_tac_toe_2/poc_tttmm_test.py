"""
Test suite for Tic-Tac-Toe.
"""

from poc_simpletest import TestSuite
import poc_tttmm as tic_tac_toe
import poc_ttt_provided as provided

PLAYERX = provided.PLAYERX
PLAYERO = provided.PLAYERO
EMPTY = provided.EMPTY
DRAW = provided.DRAW

def run_single_test(suite, board, player, expect, description):
    """
    Test single mm_move function.
    """
    board = provided.TTTBoard(3, False, board)
    suite.run_test(tic_tac_toe.mm_move(board, player), expect, description)

def run_case_test(suite):
    """
    Run a complicated case to test mm_move.
    """
    board = provided.TTTBoard(3, False, \
        [[PLAYERO, PLAYERX, EMPTY], \
        [PLAYERO, PLAYERX, EMPTY], \
        [EMPTY, PLAYERO, PLAYERX]])

    suite.run_test(tic_tac_toe.mm_move(board, PLAYERX), \
        (tic_tac_toe.SCORES[DRAW], (2, 0)), "Case Test Step 1.")

    board.move(2, 0, PLAYERX)

    suite.run_test(tic_tac_toe.mm_move(board, PLAYERO), \
        (tic_tac_toe.SCORES[DRAW], (0, 2)), "Case Test Step 2.")

    board.move(0, 2, PLAYERO)

    suite.run_test(tic_tac_toe.mm_move(board, PLAYERX), \
        (tic_tac_toe.SCORES[DRAW], (1, 2)), "Case Test Step 3.")

def run_test():
    """
    Run the test suite for Tic-Tac-Toe.
    """

    suite = TestSuite()

    run_single_test(suite, \
        [[PLAYERX, PLAYERO, EMPTY], \
        [PLAYERO, PLAYERX, PLAYERO], \
        [EMPTY, EMPTY, PLAYERX]], \
        PLAYERX, (tic_tac_toe.SCORES[PLAYERX], (-1, -1)), \
        "Test #1: When PlayerX wins.")

    run_single_test(suite, \
        [[PLAYERX, PLAYERO, EMPTY], \
        [PLAYERX, PLAYERO, PLAYERX], \
        [EMPTY, PLAYERO, EMPTY]], \
        PLAYERX, (tic_tac_toe.SCORES[PLAYERO], (-1, -1)), \
        "Test #2: When PlayerO wins.")

    run_single_test(suite, \
        [[PLAYERO, PLAYERX, PLAYERO], \
        [PLAYERO, PLAYERX, PLAYERX], \
        [PLAYERX, PLAYERO, PLAYERX]], \
        PLAYERX, (tic_tac_toe.SCORES[DRAW], (-1, -1)), \
        "Test #3: When the game draws.")

    run_single_test(suite, \
        [[PLAYERO, PLAYERX, PLAYERO], \
        [PLAYERO, PLAYERX, PLAYERX], \
        [PLAYERX, EMPTY, PLAYERO]], \
        PLAYERX, (tic_tac_toe.SCORES[PLAYERX], (2, 1)), \
        "Test #4: When PlayerX moves to win.")

    run_single_test(suite, \
        [[PLAYERO, PLAYERX, PLAYERO], \
        [PLAYERO, PLAYERX, PLAYERX], \
        [PLAYERX, PLAYERO, EMPTY]], \
        PLAYERX, (tic_tac_toe.SCORES[DRAW], (2, 2)), \
        "Test #5: When PlayerX moves to draw.")

    run_single_test(suite, \
        [[PLAYERO, PLAYERX, PLAYERX], \
        [PLAYERO, PLAYERX, PLAYERX], \
        [EMPTY, PLAYERO, EMPTY]], \
        PLAYERO, (tic_tac_toe.SCORES[PLAYERO], (2, 0)), \
        "Test #6: When PlayerO moves to win or lose.")

    run_single_test(suite, \
        [[PLAYERO, PLAYERX, EMPTY], \
        [PLAYERO, PLAYERX, PLAYERX], \
        [PLAYERX, PLAYERO, EMPTY]], \
        PLAYERO, (tic_tac_toe.SCORES[DRAW], (0, 2)), \
        "Test #7: When PlayerO moves to draw or lose.")

    run_case_test(suite)

    suite.report_results()

run_test()
