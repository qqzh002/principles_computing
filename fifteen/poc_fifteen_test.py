"""
Test suite for Fifteen puzzle.
"""

from poc_simpletest import TestSuite
from poc_fifteen import Puzzle

def test_lower_row_invariant(suite):
    """
    Test lower_row_invariant method.
    """
    puzzle = Puzzle(2, 2)
    suite.run_test(puzzle.lower_row_invariant(0, 0), True, \
        "Test #1a: It should return True when initialized with default grids.")

    puzzle = Puzzle(2, 2, [[1, 2], [0, 3]])
    suite.run_test(puzzle.lower_row_invariant(1, 1), False, \
        "Test #1b: It should return False when target tile is not zero.")

    puzzle = Puzzle(2, 2, [[2, 0], [1, 3]])
    suite.run_test(puzzle.lower_row_invariant(0, 1), False, \
        "Test #1c: It should return False when below rows are not solved.")

    puzzle = Puzzle(3, 3, [[1, 2, 3], [5, 0, 4], [6, 7, 8]])
    suite.run_test(puzzle.lower_row_invariant(1, 1), False, \
        "Test #1d: It should return False when right tiles are not solved.")


def test_solve_interior_tile(suite):
    """
    Test solve_interior_tile method.
    """
    puzzle = Puzzle(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    puzzle.solve_interior_tile(2, 2)
    suite.run_test(puzzle.lower_row_invariant(2, 1), True, \
        "Test #2a: It should solve the tile " + \
        "when tile is on the left of the position " + \
        "by a distance of 1.")

    puzzle = Puzzle(4, 4, [[1, 2, 3, 4], [5, 6, 7, 8], \
        [9, 10, 11, 12], [15, 13, 14, 0]])
    puzzle.solve_interior_tile(3, 3)
    suite.run_test(puzzle.lower_row_invariant(3, 2), True, \
        "Test #2b: It should solve the tile " + \
        "when tile is on the left of the position " + \
        "by a distance of 2 or more.")

    puzzle = Puzzle(3, 3, [[1, 2, 3], [4, 5, 8], [6, 7, 0]])
    puzzle.solve_interior_tile(2, 2)
    suite.run_test(puzzle.lower_row_invariant(2, 1), True, \
        "Test #2c: It should solve the tile " + \
        "when tile is on the top of the position " + \
        "by a distance of 1.")

    puzzle = Puzzle(4, 4, [[1, 2, 3, 4], [5, 6, 7, 15], \
        [8, 9, 10, 11], [12, 13, 14, 0]])
    puzzle.solve_interior_tile(3, 3)
    suite.run_test(puzzle.lower_row_invariant(3, 2), True, \
        "Test #2d: It should solve the tile " + \
        "when tile is on the top of the position " + \
        "by a distance of 2 or more.")

    puzzle = Puzzle(3, 3, [[1, 2, 3], [4, 8, 5], [6, 7, 0]])
    puzzle.solve_interior_tile(2, 2)
    suite.run_test(puzzle.lower_row_invariant(2, 1), True, \
        "Test #2e: It should solve the tile " + \
        "when tile is on the left and top of the position " + \
        "by a distance of 1x1.")

    puzzle = Puzzle(4, 4, [[1, 2, 3, 4], [5, 6, 7, 8], \
        [14, 9, 10, 11], [12, 13, 0, 15]])
    puzzle.solve_interior_tile(3, 2)
    suite.run_test(puzzle.lower_row_invariant(3, 1), True, \
        "Test #2f: It should solve the tile " + \
        "when tile is on the left and top of the position " + \
        "by a distance of (2 or more)x1")

    puzzle = Puzzle(4, 4, [[13, 1, 2, 3], [4, 5, 6, 7], \
        [8, 9, 10, 11], [12, 0, 14, 15]])
    puzzle.solve_interior_tile(3, 1)
    suite.run_test(puzzle.lower_row_invariant(3, 0), True, \
        "Test #2g: It should solve the tile " + \
        "when tile is on the left and top of the position " + \
        "by a distance of 1x(2 or more)")

    puzzle = Puzzle(4, 4, [[11, 1, 2, 3], [4, 5, 6, 7], \
        [8, 9, 10, 0], [12, 13, 14, 15]])
    puzzle.solve_interior_tile(2, 3)
    suite.run_test(puzzle.lower_row_invariant(2, 2), True, \
        "Test #2h: It should solve the tile " + \
        "when tile is on the left and top of the position " + \
        "by a distance of (2 or more)x(2 or more)")

    puzzle = Puzzle(3, 3, [[1, 2, 3], [4, 5, 7], [6, 0, 8]])
    puzzle.solve_interior_tile(2, 1)
    suite.run_test(puzzle.lower_row_invariant(2, 0), True, \
        "Test #2i: It should solve the tile " + \
        "when tile is on the right and top of the position " + \
        "by a distance of 1x1")

    puzzle = Puzzle(4, 4, [[1, 2, 3, 4], [5, 6, 7, 9], \
        [8, 0, 10, 11], [12, 13, 14, 15]])
    puzzle.solve_interior_tile(2, 1)
    suite.run_test(puzzle.lower_row_invariant(2, 0), True, \
        "Test #2j: It should solve the tile " + \
        "when tile is on the right and top of the position " + \
        "by a distance of (2 or more)x1")

    puzzle = Puzzle(4, 4, [[1, 2, 13, 3], [4, 5, 6, 7], \
        [8, 9, 10, 11], [12, 0, 14, 15]])
    puzzle.solve_interior_tile(3, 1)
    suite.run_test(puzzle.lower_row_invariant(3, 0), True, \
        "Test #2k: It should solve the tile " + \
        "when tile is on the right and top of the position " + \
        "by a distance of 1x(2 or more)")

    puzzle = Puzzle(4, 4, [[1, 2, 3, 13], [4, 5, 6, 7], \
        [8, 9, 10, 11], [12, 0, 14, 15]])
    puzzle.solve_interior_tile(3, 1)
    suite.run_test(puzzle.lower_row_invariant(3, 0), True, \
        "Test #2l: It should solve the tile " + \
        "when tile is on the right and top of the position " + \
        "by a distance of 1x(2 or more)")


def test_solve_col0_tile(suite):
    """
    Test solve_col0_tile method.
    """
    puzzle = Puzzle(3, 3, [[1, 2, 3], [6, 4, 5], [0, 7, 8]])
    puzzle.solve_col0_tile(2)
    suite.run_test(puzzle.lower_row_invariant(1, 2), True, \
        "Test #3a: It should solve the tile " + \
        "when tile is on the top of the position " + \
        "by a distance of 1")

    puzzle = Puzzle(3, 3, [[6, 1, 2], [3, 4, 5], [0, 7, 8]])
    puzzle.solve_col0_tile(2)
    suite.run_test(puzzle.lower_row_invariant(1, 2), True, \
        "Test #3b: It should solve the tile " + \
        "when tile is on the top of the position " + \
        "by a distance of 2")

    puzzle = Puzzle(4, 4, [[12, 1, 2, 3], [4, 5, 6, 7], \
        [8, 9, 10, 11], [0, 13, 14, 15]])
    puzzle.solve_col0_tile(3)
    suite.run_test(puzzle.lower_row_invariant(2, 3), True, \
        "Test #3c: It should solve the tile " + \
        "when tile is on the top of the position " + \
        "by a distance of 3 or more")

    puzzle = Puzzle(3, 3, [[1, 2, 3], [4, 6, 5], [0, 7, 8]])
    puzzle.solve_col0_tile(2)
    suite.run_test(puzzle.lower_row_invariant(1, 2), True, \
        "Test #3d: It should solve the tile " + \
        "when tile is on the right and top of the position " + \
        "by a distance of 1x1")

    puzzle = Puzzle(3, 3, [[1, 2, 3], [4, 5, 6], [0, 7, 8]])
    puzzle.solve_col0_tile(2)
    suite.run_test(puzzle.lower_row_invariant(1, 2), True, \
        "Test #3e: It should solve the tile " + \
        "when tile is on the right and top of the position " + \
        "by a distance of (2 or more)x1")

    puzzle = Puzzle(3, 3, [[1, 6, 2], [3, 4, 5], [0, 7, 8]])
    puzzle.solve_col0_tile(2)
    suite.run_test(puzzle.lower_row_invariant(1, 2), True, \
        "Test #3f: It should solve the tile " + \
        "when tile is on the right and top of the position " + \
        "by a distance of 1x2")

    puzzle = Puzzle(4, 4, [[1, 2, 3, 8], [4, 5, 6, 7], \
        [0, 9, 10, 11], [12, 13, 14, 15]])
    puzzle.solve_col0_tile(2)
    suite.run_test(puzzle.lower_row_invariant(1, 3), True, \
        "Test #3g: It should solve the tile " + \
        "when tile is on the right and top of the position " + \
        "by a distance of (2 or more)x2")

    puzzle = Puzzle(4, 4, [[1, 12, 2, 3], [4, 5, 6, 7], \
        [8, 9, 10, 11], [0, 13, 14, 15]])
    puzzle.solve_col0_tile(3)
    suite.run_test(puzzle.lower_row_invariant(2, 3), True, \
        "Test #3h: It should solve the tile " + \
        "when tile is on the right and top of the position " + \
        "by a distance of 1x(3 or more)")

    puzzle = Puzzle(4, 4, [[1, 2, 12, 3], [4, 5, 6, 7], \
        [8, 9, 10, 11], [0, 13, 14, 15]])
    puzzle.solve_col0_tile(3)
    suite.run_test(puzzle.lower_row_invariant(2, 3), True, \
        "Test #3i: It should solve the tile " + \
        "when tile is on the right and top of the position " + \
        "by a distance of (2 or more)x(3 or more)")


def test_row0_invariant(suite):
    """
    Test row0_invariant method.
    """
    puzzle = Puzzle(3, 3, [[1, 2, 0], [3, 4, 5], [6, 7, 8]])
    suite.run_test(puzzle.row0_invariant(2), True, \
        "Test #4a: It should return True when invariant")

    puzzle = Puzzle(3, 3, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    suite.run_test(puzzle.row0_invariant(2), False, \
        "Test #4b: It should return False " + \
        "when tile[0][target_col] is not zero.")

    puzzle = Puzzle(4, 4, [[1, 2, 0, 3], [4, 13, 6, 7], \
        [8, 9, 10, 11], [12, 5, 14, 15]])
    suite.run_test(puzzle.row0_invariant(2), False, \
        "Test #4c: It should return False " + \
        "when below rows are not solved.")

    puzzle = Puzzle(4, 4, [[1, 2, 0, 3], [4, 6, 5, 7], \
        [8, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzzle.row0_invariant(2), False, \
        "Test #4d: It should return False " + \
        "when right tiles of row 1 are not solved.")

    puzzle = Puzzle(4, 4, [[1, 2, 0, 5], [4, 3, 6, 7], \
        [8, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzzle.row0_invariant(2), False, \
        "Test #4e: It should return False " + \
        "when right tiles of row 0 are not solved.")


def test_row1_invariant(suite):
    """
    Test row0_invariant method.
    """
    puzzle = Puzzle(3, 3, [[1, 2, 3], [4, 5, 0], [6, 7, 8]])
    suite.run_test(puzzle.row1_invariant(2), True, \
        "Test #5a: It should return True when invariant")

    puzzle = Puzzle(3, 3, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    suite.run_test(puzzle.row1_invariant(2), False, \
        "Test #5b: It should return False " + \
        "when tile[0][target_col] is not zero.")

    puzzle = Puzzle(4, 4, [[1, 2, 3, 4], [5, 13, 0, 7], \
        [8, 9, 10, 11], [12, 6, 14, 15]])
    suite.run_test(puzzle.row1_invariant(2), False, \
        "Test #5c: It should return False " + \
        "when below rows are not solved.")

    puzzle = Puzzle(4, 4, [[1, 2, 4, 3], [5, 7, 0, 6], \
        [8, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzzle.row1_invariant(2), False, \
        "Test #5d: It should return False " + \
        "when right tiles of row 1 are not solved.")

    puzzle = Puzzle(4, 4, [[1, 2, 3, 4], [5, 6, 0, 7], \
        [8, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzzle.row1_invariant(2), False, \
        "Test #5d: It should return False " + \
        "when right tiles of row 0 are not solved.")


def test_solve_row0_tile(suite):
    """
    Test solve_row0_tile function.
    """
    puzzle = Puzzle(3, 3, [[1, 2, 0], [3, 4, 5], [6, 7, 8]])
    puzzle.solve_row0_tile(2)
    suite.run_test(puzzle.row1_invariant(1), True, \
        "Test #6a: It should solve the tile " + \
        "when tile is on the left of the position " + \
        "by a distance of 1.")

    puzzle = Puzzle(4, 4, [[3, 1, 2, 0], [4, 5, 6, 7], \
        [8, 9, 10, 11], [12, 13, 14, 15]])
    puzzle.solve_row0_tile(3)
    suite.run_test(puzzle.row1_invariant(2), True, \
        "Test #6b: It should solve the tile " + \
        "when tile is on the left of the position " + \
        "by a distance of 2 or more.")

    puzzle = Puzzle(4, 4, [[1, 4, 0, 3], [5, 2, 6, 7], \
        [8, 9, 10, 11], [12, 13, 14, 15]])
    puzzle.solve_row0_tile(2)
    suite.run_test(puzzle.row1_invariant(1), True, \
        "Test #6c: It should solve the tile " + \
        "when tile is on the left and bottom of the position " + \
        "by a distance of 1x1.")

    puzzle = Puzzle(4, 4, [[1, 2, 3, 0], [4, 5, 6, 7], \
        [8, 9, 10, 11], [12, 13, 14, 15]])
    puzzle.solve_row0_tile(3)
    suite.run_test(puzzle.row1_invariant(2), True, \
        "Test #6d: It should solve the tile " + \
        "when tile is on the left and bottom of the position " + \
        "by a distance of (2 or more)x1.")


def test_solve_row1_tile(suite):
    """
    Test solve_row1_tile function.
    """
    puzzle = Puzzle(3, 3, [[1, 2, 5], [3, 4, 0], [6, 7, 8]])
    puzzle.solve_row1_tile(2)
    suite.run_test(puzzle.row0_invariant(2), True, \
        "Test #7a: It should solve the tile " + \
        "when tile is on the top of the position " + \
        "by a distance of 1.")

    puzzle = Puzzle(3, 3, [[1, 2, 3], [4, 5, 0], [6, 7, 8]])
    puzzle.solve_row1_tile(2)
    suite.run_test(puzzle.row0_invariant(2), True, \
        "Test #7b: It should solve the tile " + \
        "when tile is on the left of the position " + \
        "by a distance of 1.")

    puzzle = Puzzle(4, 4, [[1, 2, 3, 4], [7, 5, 6, 0], \
        [8, 9, 10, 11], [12, 13, 14, 15]])
    puzzle.solve_row1_tile(3)
    suite.run_test(puzzle.row0_invariant(3), True, \
        "Test #7c: It should solve the tile " + \
        "when tile is on the left of the position " + \
        "by a distance of 2 or more.")

    puzzle = Puzzle(3, 3, [[1, 5, 2], [3, 4, 0], [6, 7, 8]])
    puzzle.solve_row1_tile(2)
    suite.run_test(puzzle.row0_invariant(2), True, \
        "Test #7b: It should solve the tile " + \
        "when tile is on the top and left of the position " + \
        "by a distance of 1x1.")

    puzzle = Puzzle(3, 3, [[5, 1, 2], [3, 4, 0], [6, 7, 8]])
    puzzle.solve_row1_tile(2)
    suite.run_test(puzzle.row0_invariant(2), True, \
        "Test #7b: It should solve the tile " + \
        "when tile is on the top and left of the position " + \
        "by a distance of 1x(2 or more).")


def test_solve_2x2(suite):
    """
    Test solve_2x2 function.
    """
    puzzle = Puzzle(2, 2, [[2, 1], [3, 0]])
    puzzle.solve_2x2()
    suite.run_test(str(puzzle), "[0, 1]\n[2, 3]\n", \
        "Test #8a: Case 1 for 2x2.")

    puzzle = Puzzle(2, 2, [[1, 3], [2, 0]])
    puzzle.solve_2x2()
    suite.run_test(str(puzzle), "[0, 1]\n[2, 3]\n", \
        "Test #8b: Case 2 for 2x2.")

    puzzle = Puzzle(2, 2, [[3, 2], [1, 0]])
    puzzle.solve_2x2()
    suite.run_test(str(puzzle), "[0, 1]\n[2, 3]\n", \
        "Test #8c: Case 3 for 2x2.")


def run_test():
    """
    Run test suite for Fifteen puzzle.
    """
    suite = TestSuite()
    test_lower_row_invariant(suite)
    test_solve_interior_tile(suite)
    test_solve_col0_tile(suite)
    test_row0_invariant(suite)
    test_row1_invariant(suite)
    test_solve_row0_tile(suite)
    test_solve_row1_tile(suite)
    test_solve_2x2(suite)
    suite.report_results()


run_test()
