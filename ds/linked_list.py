from dataclasses import dataclass
from typing import Any, Optional, Iterator


class SingleLinkedList:
    """single linked list with sentinel node"""

    @dataclass(repr=False)
    class _Node:
        """private internal dataclass"""
        value: Any = None
        next: Optional["SingleLinkedList._Node"] = None

    def __init__(self) -> None:
        self._head = self._Node(value="__sentinel__", next=None)

    def push(self, val: Any) -> None:
        """push a new node into list front
        the next pointer order is crucial, or will cause wild pointer"""
        new_node = self._Node(value=val, next=None)
        new_node.next = self._head.next  # noinspection PyProtectedMember
        self._head.next = new_node

    def append(self, val: Any) -> None:
        """append a new node into list end"""
        curr_ptr = self._head
        while curr_ptr.next:
            curr_ptr = curr_ptr.next
        new_node = self._Node(value=val, next=None)
        curr_ptr.next = new_node

    def insert(self) -> None:
        raise NotImplementedError("insert() method is no practical usage")

    def pop(self) -> Any:
        if not self._head.next:
            return
        curr_ptr = self._head.next
        prev_ptr = self._head
        while curr_ptr.next:
            prev_ptr = curr_ptr
            curr_ptr = curr_ptr.next
        prev_ptr.next = None
        return curr_ptr.value

    def delete(self) -> None:
        raise NotImplementedError("delete() method is no practical usage")

    def __iter__(self) -> Iterator:
        curr = self._head.next
        while curr:
            yield curr.value
            curr = curr.next
