from algo.search.binary_search import BinarySearch


def test_main():
    arr = [i for i in range(10)]
    assert BinarySearch.main(arr=arr, val=7) is True
    assert not BinarySearch.main(arr=arr, val=32)
    assert not BinarySearch.main(arr=arr, val=5.5)
