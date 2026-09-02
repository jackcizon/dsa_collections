"""
子字符串匹配
"""

from dsa_collections.ds.linked_list import SingleLinkedList


def sub_seq(L1: SingleLinkedList, L2: SingleLinkedList):
    """len L1 > len L2"""
    p = L1._head.next
    p_1 = p
    q = L2._head.next

    while p and q:
        if p.value == q.value:
            p = p.next
            q = q.next
        else:
            p_1 = p_1.next
            p = p_1
            q = L2._head.next

    if q is None:
        return True
    return False
