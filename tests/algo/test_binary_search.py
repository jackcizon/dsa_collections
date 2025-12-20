def test_main():
    arr = [i for i in range(10)]
    from algo.search.binary_search import BinarySearch

    assert BinarySearch.main(arr=arr, val=7)

    assert not BinarySearch.main(arr=arr, val=32)

    assert not BinarySearch.main(arr=arr, val=5.5)
