from algo.sort import heap_sort


def test_heap_sort():
    arr = [1, 2, 3, 4, 5, 6, 7]
    assert heap_sort(arr) == [7, 6, 5, 4, 3, 2, 1]
