"""
A, B 2个单链表连接为A B，这里用双链表代替
"""
from dsa_collections.ds.linked_list import DoubleCircledLinkedList


def merge(L1: DoubleCircledLinkedList, L2: DoubleCircledLinkedList):
    p = L1._head.next
    q = L2._head.next

    while p.next != L1._head:
        p = p.next

    while q.next != L2._head:
        q = q.next

    p.next = L2._head.next
    q.next = L1._head
