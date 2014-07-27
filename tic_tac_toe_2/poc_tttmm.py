"""
Mini-max Tic-Tac-Toe Player
"""

# import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
# import codeskulptor
# codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    result = board.check_win()
    if result is provided.PLAYERX:
        return SCORES[provided.PLAYERX], (-1, -1)
    if result is provided.PLAYERO:
        return SCORES[provided.PLAYERO], (-1, -1)
    if result is provided.DRAW:
        return SCORES[provided.DRAW], (-1, -1)
    if player is provided.PLAYERX:
        best_score = -2, (-1, -1)
    else:
        best_score = 2, (-1, -1)
    for square in board.get_empty_squares():
        clone_board = board.clone()
        clone_board.move(square[0], square[1], player)
        score = mm_move(clone_board, provided.switch_player(player))
        if player is provided.PLAYERX and score[0] > best_score[0]:
            best_score = score[0], square
        elif player is provided.PLAYERO and score[0] < best_score[0]:
            best_score = score[0], square
    return best_score

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
