from typing import Any

from dsa_collections.ds.heap import MaxHeap


def kth_largest(arr: list, k: int) -> Any:
    if k < 1 or k > len(arr):
        raise ValueError("k is out of range")
    heap = MaxHeap(arr)
    while k > 1:
        heap.pop()
        k -= 1
    return heap.pop()
