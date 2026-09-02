from dsa_collections.ds.linked_list import DoubleCircledLinkedList


def symmetry(L: DoubleCircledLinkedList):
    p = L._head.next
    q = L._head.prev

    while p != q and q.next != p:
        if p.value == q.value:
            p = p.next
            q = q.prev
        else:
            return False
    return True