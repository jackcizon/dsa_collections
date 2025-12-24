from dataclasses import dataclass
from typing import Any, Optional, List, Iterator


class LinkedStack:
    """stack implemented by single linked list with sentinel node"""

    @dataclass(repr=False)
    class _Node:
        value: Any = None
        next: Optional["LinkedStack._Node"] = None

    def __init__(self, capacity: int) -> None:
        self._size = 0
        self._capacity = capacity
        self._head: Optional["LinkedStack._Node"] = self._Node(value="__sentinel__", next=None)

    def size(self) -> int:
        return self._size

    def capacity(self) -> int:
        return self._capacity

    def top(self) -> Optional["LinkedStack._Node"]:
        if self.is_empty():
            return None
        return self._head.next

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self._capacity

    def push(self, val: Any) -> bool:
        if self.is_full():
            return False
        new_node = self._Node(value=val, next=self._head.next)
        self._head.next = new_node
        self._size += 1
        return True

    def pop(self) -> Any:
        if self.is_empty():
            return None
        del_head_next = self._head.next
        head_next_next = self._head.next.next
        self._head.next = head_next_next
        self._size -= 1
        return del_head_next.value

    def __iter__(self) -> Iterator:
        curr = self._head.next
        while curr:
            yield curr.value
            curr = curr.next
