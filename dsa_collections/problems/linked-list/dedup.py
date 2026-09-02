"""
Remove duplicates from a sorted, increasing linked list.
"""
from dsa_collections.ds.linked_list import SingleLinkedList


def dedup(L: SingleLinkedList):
    curr = L._head.next

    while curr and curr.next:
        next_ = curr.next
        if curr.value == next_.value:
            curr.next = next_.next
            # free(next_)
        else:
            curr = curr.next
