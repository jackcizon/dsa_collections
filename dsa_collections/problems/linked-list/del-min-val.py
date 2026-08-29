from dsa_collections.ds.linked_list import SingleLinkedList


def del_min_val(l: SingleLinkedList):
    curr = l._head.next
    prev = l._head  # prev不能初始化为None，否则可能prev.next_出错
    del_min = curr
    min_prev = prev  # 用来保存删除节点的前驱，来保证删除后能连接到del_min_curr.next_

    while curr:
        # record min
        if curr.value < del_min.value:
            del_min = curr
            min_prev = prev

        # go next
        prev = prev.next
        curr = curr.next

    min_prev.next = del_min.next
    # free(del_min_curr)
