from typing import Any, Iterator, Iterable


class MaxHeap:
    def __init__(self, data: Iterable[Any] = (), capacity: int = None):
        self._heap = list(data)  # 把输入可迭代对象转成列表
        self._size = len(self._heap)
        self._capacity = capacity or 2**31 - 1  # 如果没指定容量，就无限大
        if self._size > 1:
            self._build_heap()  # 一次性建堆

    def _build_heap(self) -> None:
        # 自底向上 heapify_down
        for i in reversed(range(self._size // 2)):
            self._heapify_down(i)

    @staticmethod
    def _parent(i: int) -> int:
        return (i - 1) // 2

    @staticmethod
    def _left(i: int) -> int:
        return 2 * i + 1

    @staticmethod
    def _right(i: int) -> int:
        return 2 * i + 2

    def _swap(self, i: int, j: int) -> None:
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def push(self, val: Any) -> bool:
        """push into end, then maintain heap invariant"""
        if self.is_full():
            return False
        # push
        self._heap.append(val)
        self._size += 1
        # maintain invariant, reverse order to check and swap
        self._heapify_up(self._size - 1)
        return True

    def pop(self) -> Any:
        """pop frist element(largest), then maintain heap invariant"""
        # get top val(largest)
        if self.is_empty():
            return None
        val = self._heap[0]
        # maintain heap invariant
        self._size -= 1
        if not self.is_empty():
            self._heap[0] = self._heap[self._size]  # copy latest val to first pos
            self._heapify_down(0)
        self._heap.pop()  # del tail element
        return val

    def top(self) -> Any:
        if self.is_empty():
            return None
        return self._heap[0]

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self._capacity

    def _heapify_up(self, child: int) -> None:
        """inner method to justify push(), partly update.
        recursively check and swap the vals to maintain heap invariant"""
        parent = self._parent(child)
        # check
        while child > 0 and self._heap[parent] < self._heap[child]:
            self._swap(parent, child)
            child = parent
            # recursion
            parent = self._parent(child)

    def _heapify_down(self, parent: int) -> None:
        """inner method to justify pop(), full scale update.
        recursively check and swap the vals violate heap invariant"""
        # get
        left = self._left(parent)
        right = self._right(parent)
        max_val_index = parent
        # check
        if left < self._size and self._heap[left] > self._heap[max_val_index]:
            max_val_index = left
        if right < self._size and self._heap[right] > self._heap[max_val_index]:
            max_val_index = right
        # recursion
        if max_val_index != parent:
            self._swap(max_val_index, parent)
            self._heapify_down(max_val_index)

    def __iter__(self) -> Iterator:
        return iter(self._heap)
