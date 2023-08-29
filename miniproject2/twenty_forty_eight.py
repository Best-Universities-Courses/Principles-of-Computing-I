"""
Clone of 2048 game.
"""
import random

# from miniproject1.merge import sum_tiles
# import poc_2048_gui


# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def sum_tiles(orig_list):
    """
    Sums the tiles (or numbers) of the given list by pair in pair
    :param orig_list:
    :return: a list with the possible additions for every couple of
    equal consecutive numbers in the given list
    """
    summed_tiles_list = []
    length_orig_list = len(orig_list)
    ind_orig_list = 0
    while ind_orig_list < length_orig_list - 1:
        current_tile = orig_list[ind_orig_list]
        next_tile = orig_list[ind_orig_list + 1]
        if current_tile == next_tile:
            summed_tiles_list.append(current_tile + next_tile)
            ind_orig_list += 1
        else:
            summed_tiles_list.append(current_tile)
        ind_orig_list += 1

    while ind_orig_list < length_orig_list:
        summed_tiles_list.append(orig_list[ind_orig_list])
        ind_orig_list += 1

    length_summed_tiles_list = len(summed_tiles_list)
    ind_aux = length_summed_tiles_list
    while ind_aux < length_orig_list:
        summed_tiles_list.append(0)
        ind_aux += 1

    return summed_tiles_list


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    out_list = []
    ind_out_list = 0
    length_line = len(line)
    for ind_line in range(length_line):
        if line[ind_line] != 0:
            out_list.append(line[ind_line])
            ind_out_list += 1

    while ind_out_list < length_line:
        out_list.append(0)
        ind_out_list += 1

    return sum_tiles(out_list)


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        if grid_height < 1 or grid_width < 1:
            raise ValueError
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.board = self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        return [[0] * self.grid_width] * self.grid_height

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        out = ''
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                out += str(self.get_tile(row, col)) + ' '
            out += '\n'
        return out

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        pseudo_random_number = random.random()
        random_row, random_column = self.get_random_board_indexes()
        if pseudo_random_number < 0.9:
            self.set_tile(random_row, random_column, 2)
        else:
            self.set_tile(random_row, random_column, 4)

    def get_random_board_indexes(self):
        return (random.randint(0, self.grid_height - 1),
                random.randint(0, self.grid_width - 1))

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.board[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.board[row][col]


# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
