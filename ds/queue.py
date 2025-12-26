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


class StandardQueue:
    def __init__(self, exp2_len: int) -> None:
        """standard queue with size=2**k
        queue may be not cleaned when it's not full,
        with code logic, we can pass those dirty data"""
        if exp2_len > 10:
            exp2_len = 10
        if exp2_len < 1:
            exp2_len = 1
        self._capacity = 2 ** int(exp2_len)
        self._size = 0
        self._front = 0
        self._rear = 0
        self._buffer = [None] * self._capacity

    def size(self) -> int:
        return self._size

    def capacity(self) -> int:
        return self._capacity

    def enqueue(self, val: Any) -> bool:
        if self.is_full():
            return False
        self._buffer[self._rear] = val
        self._rear = (self._rear + 1) & (self._capacity - 1)
        self._size += 1
        return True

    def dequeue(self) -> Any:
        """may generate dirty data, make inaccessible through code logic"""
        if self.is_empty():
            return None
        val = self._buffer[self._front]
        self._front = (self._front + 1) & (self._capacity - 1)
        self._size -= 1
        return val

    def top(self) -> Any:
        if self.is_empty():
            return None
        return self._buffer[self._front]

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self._capacity

    def __iter__(self) -> Iterator:
        """fake dequeue to iter"""
        size = self._size
        front = self._front
        while size > 0:
            yield self._buffer[front]
            # print(self._buffer[front])
            front = (front + 1) & (self._capacity - 1)
            size -= 1


class DoubleEndsQueue:
    def __init__(self, exp2_len: int) -> None:
        if exp2_len < 1:
            exp2_len = 1
        if exp2_len > 10:
            exp2_len = 10
        self._capacity = 2**exp2_len
        self._size = 0
        self._front = 0
        self._rear = 0
        self._buffer = [None] * self._capacity

    def size(self) -> int:
        return self._size

    def capacity(self) -> int:
        return self._capacity

    def push_back(self, val: Any) -> bool:
        """enqueue() in StandardQueue"""
        if self.is_full():
            return False
        self._buffer[self._rear] = val
        self._rear = (self._rear + 1) & (self._capacity - 1)
        self._size += 1
        return True

    def push_front(self, val: Any) -> bool:
        """reverse push_back() code logic, symmetrical to pop_back()"""
        if self.is_full():
            return False
        self._front = (self._front - 1 + self._capacity) & (self._capacity - 1)
        self._buffer[self._front] = val
        self._size += 1
        return True

    def pop_front(self) -> Any:
        """dequeue() in StandardQueue"""
        if self.is_empty():
            return None
        val = self._buffer[self._front]
        self._front = (self._front + 1) & (self._capacity - 1)
        self._size -= 1
        return val

    def pop_back(self) -> Any:
        """reverse pop_front() code logic, symmetrical to push_front()"""
        if self.is_empty():
            return None
        self._rear = (self._rear - 1 + self._capacity) & (self._capacity - 1)
        val = self._buffer[self._rear]
        self._size -= 1
        return val

    def is_full(self) -> bool:
        return self._size == self._capacity

    def is_empty(self) -> bool:
        return self._size == 0

    def __iter__(self) -> Iterator:
        """fake dequeue to iter"""
        front = self._front
        for _ in range(self._size):
            yield self._buffer[front]
            front = (front + 1) & (self._capacity - 1)
