from dsa_collections.ds.heap import MaxHeap


def heap_sort(arr: list) -> list:
    heap = MaxHeap(arr)
    sorted_res = []
    while not heap.is_empty():
        sorted_res.append(heap.pop())
    return sorted_res
