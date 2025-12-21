from typing import Any, Optional, Iterator


class Node:
    def __init__(self, value: Any = None, next_: Optional["Node"] = None) -> None:
        self.value = value
        self.next = next_


class SingleLinkedList:
    """single linked list with sentinel node"""

    def __init__(self) -> None:
        self.head: Node = Node(value="__sentinel__", next_=None)

    def push(self, val: Any) -> None:
        """push a new node into list front
        the next pointer order is crucial, or will cause wild pointer"""
        new_node = Node(value=val, next_=None)
        new_node.next = self.head.next
        self.head.next = new_node

    def append(self, val: Any) -> None:
        """append a new node into list end"""
        curr_ptr = self.head
        while curr_ptr.next:
            curr_ptr = curr_ptr.next
        new_node = Node(value=val, next_=None)
        curr_ptr.next = new_node

    def insert(self) -> None:
        raise NotImplementedError("insert() method is no practical usage")

    def pop(self) -> Any:
        if not self.head.next:
            return
        curr_ptr = self.head.next
        prev_ptr = self.head
        while curr_ptr.next:
            prev_ptr = curr_ptr
            curr_ptr = curr_ptr.next
        prev_ptr.next = None
        return curr_ptr.value

    def delete(self) -> None:
        raise NotImplementedError("delete() method is no practical usage")

    def __iter__(self) -> Iterator:
        curr = self.head.next
        while curr:
            yield curr.value
            curr = curr.next
