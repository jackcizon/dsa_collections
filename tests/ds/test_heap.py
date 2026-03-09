import pytest

from dsa_collections.ds.examples.heap_example import kth_largest
from dsa_collections.ds.heap import MaxHeap


def test_max_heap():
    heap = MaxHeap(capacity=10)

    assert heap.top() is None

    # 测试 push
    print("=== Push ===")
    for val in [5, 3, 8, 1, 6]:
        heap.push(val)
        print(f"Pushed {val}, top now: {heap.top()}, heap: {heap._heap[: heap._size]}")

    print(list(heap))

    # 测试 top
    print("\n=== Top ===")
    print(f"Current top: {heap.top()}")  # 应该是 8

    # 测试 pop
    print("\n=== Pop ===")
    while not heap.is_empty():
        val = heap.pop()
        print(f"Popped {val}, heap now: {heap._heap[: heap._size]}")

    # 测试 pop 空堆
    print("\n=== Pop empty ===")
    print(heap.pop())  # None

    # 测试 push 到满堆
    print("\n=== Push to full ===")
    for val in range(1, 12):
        success = heap.push(val)
        print(f"Pushed {val}, success: {success}, heap: {heap._heap[: heap._size]}")

    # 检查 top
    print("\n=== Final Top ===")
    print(heap.top())  # 应该是 10

    heap2 = MaxHeap([5, 3, 8, 1, 6])
    print(heap2._heap[: heap2._size])  # 输出建堆后的数组，应该是合法最大堆
    print(heap.top())  # 最大值 8

    heap2.push(10)
    print(heap2.top())  # 最大值 10

    while not heap2.is_empty():
        print(heap2.pop(), end=" ")  # 按顺序 pop 出 10 8 6 5 3 1


def test_kth_largest():
    arr = [1, 2, 3, 4, 5, 6, 7]
    with pytest.raises(ValueError):
        kth_largest(arr, -1)
    assert kth_largest(arr, 3) == 5
