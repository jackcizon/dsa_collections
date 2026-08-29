from dsa_collections.ds.linked_list import SingleLinkedList


def del_val_between_x_y(L: SingleLinkedList, x: int, y: int):
    """
    :param L: linked-list
    :param x: min
    :param y: max
    :return: None
    """
    curr = L._head.next
    prev = L._head

    while curr:
        next_ = curr.next

        # del val if x < val < y
        if x < curr.value < y:
            prev.next = next_
            # free(curr)
        # go next
        else:
            prev = curr  # or prev.next
        curr = next_
