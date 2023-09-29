import pytest

from src.miniproject2.twenty_forty_eight import TwentyFortyEight


@pytest.mark.parametrize(
    "height, width, expected_height_and_width", [
        (1, 1, (1, 1)),
        (3, 3, (3, 3)),
        (1, 4, (1, 4)),
        (4, 1, (4, 1)),
    ]
)
def test_build_a_board(height, width, expected_height_and_width):
    twenty_forty_eight = TwentyFortyEight(height, width)
    # twenty_forty_eight.reset()
    assert twenty_forty_eight.get_grid_height() == expected_height_and_width[0]
    assert twenty_forty_eight.get_grid_width() == expected_height_and_width[1]


def test_get_random_index_from_board():
    twenty_forty_eight = TwentyFortyEight(2, 3)
    row_index, column_index = twenty_forty_eight.get_random_board_indexes()
    assert row_index in list(range(twenty_forty_eight.get_grid_height()))
    assert column_index in list(range(twenty_forty_eight.get_grid_width()))
