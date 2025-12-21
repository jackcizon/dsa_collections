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

    def is_empty(self) -> bool:
        return self._head.next is None

    def pop(self) -> Any:
        if self.is_empty():
            return None
        curr_ptr = self._head.next
        prev_ptr = self._head
        while curr_ptr.next:
            curr_ptr = curr_ptr.next
            prev_ptr = prev_ptr.next
        prev_ptr.next = None
        return curr_ptr.value

    def pop_front(self) -> Any:
        if self.is_empty():
            return None
        del_head_next = self._head.next
        head_next_next = self._head.next.next
        self._head.next = head_next_next
        return del_head_next.value

    def insert(self) -> None:
        raise NotImplementedError("insert() method is no practical usage")

    def delete(self) -> None:
        raise NotImplementedError("delete() method is no practical usage")

    def __iter__(self) -> Iterator:
        curr = self._head.next
        while curr:
            yield curr.value
            curr = curr.next


class DoubleLinkedList:
    """double linked list with 2 sentinel nodes"""

    @dataclass(repr=False)
    class _Node:
        value: Any = None
        prev: Optional["DoubleLinkedList._Node"] = None
        next: Optional["DoubleLinkedList._Node"] = None

    def __init__(self) -> None:
        self._head = self._Node(value="__head__", prev=None, next=None)
        self._tail = self._Node(value="__tail__", prev=self._head, next=None)
        self._head.next = self._tail

    def insert(self) -> None:
        raise NotImplementedError("insert() method is no practical usage")

    def delete(self) -> None:
        raise NotImplementedError("delete() method is no practical usage")

    def push(self, val: Any) -> None:
        head_next = self._head.next
        new_node = self._Node(value=val, prev=self._head, next=head_next)
        head_next.prev = new_node
        self._head.next = new_node

    def append(self, val: Any) -> None:
        """symmetrical with push()"""
        tail_prev = self._tail.prev
        new_node = self._Node(value=val, prev=tail_prev, next=self._tail)
        tail_prev.next = new_node
        self._tail.prev = new_node

    def is_empty(self) -> bool:
        return self._head.next is self._tail

    def pop(self) -> Any:
        if self.is_empty():
            return None
        del_tail_prev = self._tail.prev
        tail_prev_prev = self._tail.prev.prev
        self._tail.prev = tail_prev_prev
        tail_prev_prev.next = self._tail
        return del_tail_prev.value

    def pop_front(self) -> Any:
        """symmetrical with pop()"""
        if self.is_empty():
            return None
        del_head_next = self._head.next
        head_next_next = self._head.next.next
        self._head.next = head_next_next
        head_next_next.prev = self._head
        return del_head_next.value

    def __iter__(self) -> Iterator:
        curr = self._head.next
        while curr is not self._tail:
            yield curr.value
            curr = curr.next
