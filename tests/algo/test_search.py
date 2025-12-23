from algo.search import binary_search


def test_binary_search():
    arr = [i for i in range(10)]
    assert binary_search(arr=arr, val=7) is True
    assert not binary_search(arr=arr, val=32)
    assert not binary_search(arr=arr, val=5.5)
