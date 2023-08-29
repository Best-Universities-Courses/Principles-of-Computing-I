import pytest

from miniproject2.twenty_forty_eight import TwentyFortyEight


@pytest.mark.parametrize(
    "height, width, expected_result", [
        (1, 1, [[0]]),
        (3, 3, [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        (1, 4, [[0, 0, 0, 0]]),
        (4, 1, [[0], [0], [0], [0]]),
    ]
)
def test_build_a_board(height, width, expected_result):
    twenty_forty_eight = TwentyFortyEight(height, width)
    my_new_board = twenty_forty_eight.reset()
    assert my_new_board == expected_result


def test_get_random_index_from_board():
    twenty_forty_eight = TwentyFortyEight(2, 3)
    row_index, column_index = twenty_forty_eight.get_random_board_indexes()
    assert row_index in list(range(twenty_forty_eight.get_grid_height()))
    assert column_index in list(range(twenty_forty_eight.get_grid_width()))
