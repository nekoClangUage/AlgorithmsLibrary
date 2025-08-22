import pytest
from src.sorting import BubbleSort

@pytest.mark.parametrize("input_array, expected_array", [
    ([3, 2, 1], [1, 2, 3]),
    ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
    ([], []),
    ([1], [1]),
    ([2, 2, 2], [2, 2, 2]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
])
def test_bubble_sort(input_array, expected_array):
    sorter = BubbleSort()
    sorter.simpleBubble(input_array)
    assert input_array == expected_array