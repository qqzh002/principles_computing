"""
This is a simpler one-player version of Mancala called Tchoukaillon.
http://mancala.wikia.com/wiki/Tchoukaillon
Since this name is rather unwieldy, we refer to this game as Solitaire Mancala.
"""

class SolitaireMancala(object):
    """
    Create a Solitaire Mancala game model.
    """

    def __init__(self):
        self.configuration = [0]

    def set_board(self, configuration):
        """
        Set the board to be a copy of the supplied configuration.
        """
        self.configuration = configuration[:]

    def __str__(self):
        return str(self.configuration[::-1])

    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in the house with index house_num.
        """
        if house_num >= 0 and house_num < len(self.configuration):
            return self.configuration[house_num]

    def is_legal_move(self, house_num):
        """
        Return True if moving the seeds from house[house_num] is legal.
        """
        if house_num >= 1 and house_num < len(self.configuration):
            return house_num == self.configuration[house_num]
        else:
            return False

    def apply_move(self, house_num):
        """
        Apply a legal move for house[house_num] to the board.
        """
        if not self.is_legal_move(house_num):
            return
        for i in range(0, house_num):
            self.configuration[i] += 1
        self.configuration[house_num] = 0

    def choose_move(self):
        """
        Return the index for the legal move whose house is closest to the store.
        If no legal move is available, return 0.
        """
        for i in range(1, len(self.configuration)):
            if self.is_legal_move(i):
                return i
        return 0

    def is_game_won(self):
        """
        Return True if all houses contain no seeds.
        """
        for i in range(1, len(self.configuration)):
            if self.configuration[i] > 0:
                return False
        return True

    def plan_moves(self):
        """
        Given a Mancala game,
        return a list of legal moves computed to win the game if possible.
        """
        simulated_game = SolitaireMancala()
        simulated_game.set_board(self.configuration)
        plan = []
        while simulated_game.choose_move() != 0:
            plan.append(simulated_game.choose_move())
            simulated_game.apply_move(simulated_game.choose_move())
        return plan
