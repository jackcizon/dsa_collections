from typing import Any

from dsa_collections.ds.linked_list import SingleLinkedList


def del_all_val_x(l: SingleLinkedList, x: Any):
    curr = l._head.next
    prev = l._head  # prev不能初始化为None，否则可能prev.next_出错

    while curr:
        next_ = curr.next
        if curr.value == x:
            prev.next = next_
            # free(curr)
            curr = next_
        else:
            prev = curr
            curr = next_
