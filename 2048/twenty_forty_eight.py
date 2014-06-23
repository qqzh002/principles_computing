"""
Clone of 2048 game.
"""

import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0), DOWN: (-1, 0), LEFT: (0, 1), RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    result = [0 for index in range(len(line))]
    merge_index = 0
    has_first_value = False
    for index in range(len(line)):
        if line[index] == 0:
            continue
        if has_first_value:
            if result[merge_index] == line[index]:
                result[merge_index] += line[index]
                merge_index += 1
                has_first_value = False
            else:
                merge_index += 1
                result[merge_index] = line[index]
        else:
            result[merge_index] = line[index]
            has_first_value = True
    return result

class TwentyFortyEight(object):
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.rows = grid_height
        self.columns = grid_width
        self.grid = None
        self.initial_tiles = {
            UP: [(0, col) for col in range(self.columns)],
            DOWN: [(self.rows - 1, col) for col in range(self.columns)],
            LEFT: [(row, 0) for row in range(self.rows)],
            RIGHT: [(row, self.columns - 1) for row in range(self.rows)]
        }
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self.grid = [[0 for dummy_col in range(self.columns)] \
            for dummy_row in range(self.rows)]

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self.grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.rows

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.columns

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        for initial_tile in self.initial_tiles[direction]:
            line = []
            self.iterate_line(initial_tile, OFFSETS[direction], line, \
                lambda row, col, index, line: \
                line.append(self.get_tile(row, col)))
            line = merge(line)
            self.iterate_line(initial_tile, OFFSETS[direction], line, \
                lambda row, col, index, line: \
                self.set_tile(row, col, line[index]))
        self.new_tile()

    def iterate_line(self, initial_tile, offset, args, function):
        """
        Iterate over a line and execute function.
        """
        row = initial_tile[0]
        col = initial_tile[1]
        index = 0
        while row >= 0 and row < self.rows and col >= 0 and col < self.columns:
            function(row, col, index, args)
            row += offset[0]
            col += offset[1]
            index += 1

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        empty_tiles = [(row, col) for row in range(self.rows) \
            for col in range(self.columns) if self.get_tile(row, col) == 0]
        if len(empty_tiles) == 0:
            return
        tile = random.choice(empty_tiles)
        value = 2 if random.random() < 0.9 else 4
        self.set_tile(tile[0], tile[1], value)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]
