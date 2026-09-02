"""
1. Given two sorted (in ascending order) linked lists, A and B, find their intersection and store the result in A;
2. retain the nodes in A that are also present in B, and discard those that are not.
"""
from dsa_collections.ds.linked_list import SingleLinkedList


def intersect(A: SingleLinkedList, B: SingleLinkedList):
    p1 = A._head.next
    p2 = B._head.next

    tail = A._head

    while p1 and p2:
        if p1.value == p2.value:
            tail.next = p1
            tail = p1
            p1 = p1.next
            p2 = p2.next
        elif p1.value < p2.value:
            p1 = p1.next
        else:
            p2 = p2.next

    tail.next = None
