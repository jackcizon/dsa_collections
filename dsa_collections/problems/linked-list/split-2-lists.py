"""
C = head -> a1 -> b1 -> a2 -> b2 -> .... -> an -> bn -> Null

split into A and B,

A: a1 -> a2 -> ... -> an -> Null
B: bn -> bn-1 -> ... -> b1 -> Null

A is a part of original C, B is new list
"""
from dsa_collections.ds.linked_list import SingleLinkedList


def split_2_lists(C: SingleLinkedList):
    # new B
    B = SingleLinkedList()

    curr = C._head.next
    tail_a = C._head

    while curr:
        # reserve Ai
        tail_a.next = curr
        tail_a = curr

        # get Bi
        b = curr.next
        if b is None:  # 超出最大长度
            break

        # move 2 times， 给Ai+1使用
        curr = curr.next.next

        # B.push(val)
        b.next = B._head.next  # 初始化B时，B._head.next=Null,头插法
        B._head.next = b

    tail_a.next = None
    A = C  # optional, A is a ptr of C, A is the alias of C
    return A, B
