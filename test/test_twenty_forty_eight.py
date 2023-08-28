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
