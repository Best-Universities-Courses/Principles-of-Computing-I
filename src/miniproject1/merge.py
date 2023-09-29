"""
Merge function for 2048 game.
"""


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
            # summed_tiles_list.append(0)
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
    Function that merges a single row or column in 2048.
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

    # print(out_list)
    return sum_tiles(out_list)


def main():
    """
    Generic function to execute this script
    :return:
    """
    print(merge([8, 8]))
    print(merge([4]))
    print(merge([8, 4]))
    print()
    print(merge([2, 0, 2, 4]))
    print(merge([0, 0, 2, 2]))
    print(merge([2, 2, 0, 0]))
    print(merge([2, 2, 2, 2, 2]))
    print(merge([8, 16, 16, 8]))


main()
