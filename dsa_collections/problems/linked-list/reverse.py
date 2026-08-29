from dsa_collections.ds.linked_list import SingleLinkedList


def reverse(l: SingleLinkedList):
    """
    # init
    head-->1-->2-->3-->None
    
    # loop
    head-->1<--2 3-->None
    1-->None
    
    head-->1<--2<--3
    1-->None
    
    # connect head
    None<--1<--2<--3<--head
    """

    # init
    curr = l._head.next
    prev = None
    next_ = None

    # loop
    while curr:
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_

    # connect head
    l._head.next = prev
