from dsa_collections.ds.linked_list import SingleLinkedList


def has_ring(L: SingleLinkedList):
    fast = L._head.next
    slow = fast

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            p = L._head.next

            while p != slow:
                p = p.next
                slow = slow.next

            return p

    return None
