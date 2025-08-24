import pytest
from src.sorting import BubbleSort

# ------------------------------------------------------

@pytest.mark.parametrize("input_array, expected_array", [
    ([3, 2, 1], [1, 2, 3]),
    ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
    ([], []),
    ([1], [1]),
    ([2, 2, 2], [2, 2, 2]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
])
def test_simpleBubble_sort(input_array, expected_array):
    sorter = BubbleSort()
    sorter.simpleBubble(input_array)
    assert input_array == expected_array

# ------------------------------------------------------

@pytest.mark.parametrize("num_processes", [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
@pytest.mark.parametrize("input_array, expected_array", [
    ([3, 2, 1], [1, 2, 3]),
    ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
    ([], []),
    ([1], [1]),
    ([2, 2, 2], [2, 2, 2]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    (list(range(100, 0, -1)), list(range(1, 101)))
])
def test_oddevenBubble_sort(input_array, expected_array, num_processes):
    array_to_sort = input_array.copy()
    sorter = BubbleSort()
    sorter.oddEvenBubble(array_to_sort, num_processes=num_processes)
    assert array_to_sort == expected_array

# ------------------------------------------------------

@pytest.mark.parametrize("input_array, expected_array", [
    ([3, 2, 1], [1, 2, 3]),
    ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
    ([], []),
    ([1], [1]),
    ([2, 2, 2], [2, 2, 2]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
])
def test_oddevenBubbleSingleThread_sort(input_array, expected_array):
    sorter = BubbleSort()
    sorter.oddEvenBubbleSingleThread(input_array)
    assert input_array == expected_array

# ------------------------------------------------------
