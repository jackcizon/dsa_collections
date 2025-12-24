from dataclasses import dataclass
from typing import Any, Optional, Iterator


class BaseQueue:
    """basic queue implemented by simgle circled linked list"""

    @dataclass(repr=False)
    class _Node:
        value: Any = None
        next: Optional["BaseQueue._Node"] = None

    def __init__(self, capacity: int) -> None:
        self._size = 0
        self._capacity = capacity
        self._head = self._Node(value="__sentinel__", next=None)
        self._tail = self._head
        self._tail.next = self._head

    def enqueue(self, val: Any) -> None:
        """append to tail"""
        if self.is_full():
            return None
        new_node = self._Node(value=val, next=self._head)
        self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self) -> Any:
        """pop front"""
        if self.is_empty():
            return None
        del_head_next = self._head.next
        self._head.next = del_head_next.next
        if self._tail == del_head_next:
            self._tail = self._head
        self._size -= 1
        return del_head_next.value

    def is_full(self) -> bool:
        return self._size == self._capacity

    def is_empty(self) -> bool:
        return self._size == 0

    def top(self) -> Optional["BaseQueue._Node"]:
        if self.is_empty():
            return None
        return self._head.next

    def __iter__(self) -> Iterator:
        curr = self._head.next
        for i in range(self._size):
            yield curr.value
            curr = curr.next
