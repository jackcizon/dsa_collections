r"""
Extract the common elements from two sorted, ascending linked lists into a new linked list.

两个有序序列
      ↓
   双指针
      ↓
比较 p1 和 p2
 ┌────┼────┐
 ↓    ↓    ↓
=     <    >
↓     ↓    ↓
都走   p1   p2
      走    走
"""
from dsa_collections.ds.linked_list import SingleLinkedList


def extract_common_values(L1: SingleLinkedList, L2: SingleLinkedList):
    p1 = L1._head.next
    p2 = L2._head.next

    L3 = SingleLinkedList()

    while p1 and p2:
        p1_v = p1.value
        p2_v = p2.value
        if p1_v == p2_v:
            L3.append(p1_v)
            p1 = p1.next
            p2 = p2.next
        elif p1_v < p2_v:
            p1 = p1.next
        else:
            p2 = p2.next

    return L3
