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

ROW_IND = 0
COL_IND = 1


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
        self._board = []
        if grid_height < 1 or grid_width < 1:
            raise ValueError
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()
        self._initial_tiles = {
            UP: [(0, j) for j in range(self._grid_width)],
            DOWN: [(self._grid_height - 1, j) for j in range(self._grid_width)],
            LEFT: [(i, 0) for i in range(self._grid_height)],
            RIGHT: [(i, self._grid_width - 1) for i in range(self._grid_height)],
        }

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._board = [[0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        out = ''
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                out += str(self.get_tile(row, col)) + ' '
            out += '\n'
        return out

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        line = []
        new_line = []
        has_board_changed = False
        for board_tuple in self._initial_tiles[direction]:
            line = []
            aux_tuple = board_tuple
            retries = 20
            while (aux_tuple[ROW_IND] in range(self._grid_height)
                    and aux_tuple[COL_IND] in range(self._grid_width) and retries > 0):
                tile = self.get_tile(aux_tuple[ROW_IND], aux_tuple[COL_IND])
                line.append(tile)
                new_row = aux_tuple[ROW_IND] + OFFSETS[direction][ROW_IND]
                new_col = aux_tuple[COL_IND] + OFFSETS[direction][COL_IND]
                aux_tuple = (new_row, new_col)
                retries -= 1

            new_line = merge(line)

            if line != new_line:
                has_board_changed = True

            aux_tuple = board_tuple
            retries = 20
            while (aux_tuple[ROW_IND] in range(self._grid_height)
                    and aux_tuple[COL_IND] in range(self._grid_width) and retries > 0):
                tile = new_line.pop(0)
                self.set_tile(aux_tuple[ROW_IND], aux_tuple[COL_IND], tile)
                new_row = aux_tuple[ROW_IND] + OFFSETS[direction][ROW_IND]
                new_col = aux_tuple[COL_IND] + OFFSETS[direction][COL_IND]
                aux_tuple = (new_row, new_col)
                retries -= 1

        if has_board_changed:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        pseudo_random_number = random.random()
        random_row = random_column = None
        try:
            random_row, random_column = self.get_random_board_indexes()
        except ValueError:
            return

        if pseudo_random_number < 0.9:
            self.set_tile(random_row, random_column, 2)
        else:
            self.set_tile(random_row, random_column, 4)

    def get_random_board_indexes(self):
        """
        Gets the row and column indexes of the board matrix which
        contain a cell address with a value equal to 0
        :return:
        """
        random_row = random.randint(0, self._grid_height - 1)
        random_col = random.randint(0, self._grid_width - 1)

        retries = 20
        while self._board[random_row][random_col] != 0 and retries > 0:
            random_row = random.randint(0, self._grid_height - 1)
            random_col = random.randint(0, self._grid_width - 1)
            retries -= 1

        if retries == 0:
            raise ValueError
        return random_row, random_col

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._board[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        if row not in range(self._grid_height) or col not in range(self._grid_width):
            raise IndexError
        return self._board[row][col]


# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
