from typing import Any, Iterator


class DynamicArray:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.size: int = 0
        self.items: list = [None] * capacity

    def is_full(self) -> bool:
        return self.size == self.capacity

    def is_empty(self) -> bool:
        return self.size == 0

    def _resize(self) -> None:
        self.items += [None] * self.capacity
        self.capacity *= 2

    def _check_index_insert(self, index: int) -> None:
        if index < 0 or index > self.size:
            raise IndexError("Sequence index out of range.")

    def _check_index_delete(self, index: int) -> None:
        if index < 0 or index > self.size - 1:
            raise IndexError("Sequence index out of range.")

    def insert(self, val: Any, index: int) -> None:
        if self.is_full():
            self._resize()

        self._check_index_insert(index)

        for i in range(self.size, index, -1):
            self.items[i] = self.items[i - 1]

        self.items[index] = val
        self.size += 1

    def append(self, val: Any) -> None:
        self.insert(val, self.size)

    def push(self, val: Any) -> None:
        self.insert(val, 0)

    def pop(self) -> None:
        self.delete(self.size - 1)

    def delete(self, index: int) -> None:
        self._check_index_delete(index)

        for i in range(index + 1, self.size):
            self.items[i - 1] = self.items[i]

        self.items[self.size - 1] = None
        self.size -= 1

    def remove(self, val: Any) -> bool:
        for i in range(self.size):
            if self.items[i] == val:
                for j in range(i + 1, self.size):
                    self.items[j - 1] = self.items[j]

                self.items[self.size - 1] = None
                self.size -= 1
                return True
        return False

    def get(self, index: int) -> Any:
        self._check_index_delete(index)
        return self.items[index]

    def exists(self, val: Any) -> bool:
        for i in range(self.size):
            if self.items[i] == val:
                return True
        return False

    def __iter__(self) -> Iterator:
        for val in self.items:
            if val:
                yield val
