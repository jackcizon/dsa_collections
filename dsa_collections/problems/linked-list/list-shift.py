"""
循环移位K
"""
from dsa_collections.ds.linked_list import SingleLinkedList


def list_shift(L: SingleLinkedList, k: int):
    p = L._head.next

    length = 1

    while p.next:
        p = p.next
        length += 1

    k %= length

    # 连成环
    p.next = L._head.next

    for _ in range(length - k - 1):
        p = p.next

    # 接头部
    q = p.next
    L._head.next = q

    # 消去环
    p.next = None
