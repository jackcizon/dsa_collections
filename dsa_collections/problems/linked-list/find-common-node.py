from dsa_collections.ds.linked_list import SingleLinkedList


def find_common_node(L1: SingleLinkedList, L2: SingleLinkedList):
    """
    len L1 = m + common-len(c)
    len L2 = n + c

    path1: m, c, n
    path2: n, c, m

                       common node
                            \/
    L1: A1 --> A2 --> A3--> C1 --> ..... Cn --> Null
                            /\
                            ||
    L2: B1 --> B2---------->//

    m = 3
    n = 2
    c = N(1->n)

    3 + n + 2 == 2 + n + c

    设置p, q这两个指针, 最后相见于C1点或Null

    :param L1:
    :param L2:
    :return: p
    """

    # init
    p = L1._head.next
    q = L2._head.next

    # loop
    while p != q:  # 直到相见, 否则不存在common-node
        if p:
            p = p.next
        else:
            p = L2._head.next

        # 对称
        if q:
            q = q.next
        else:
            q = L1._head.next

    # case 1: 当p, q都走完m + n + c的长度,相见于C1
    # case 2: p走完了m+c+n+c 和 q走完了n+c+m+c, 此时p == q == Null
    return p
