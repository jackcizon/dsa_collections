"""
重排序
a1, a2, ..., an-1, an

a1, an, a2, an-1, ...
"""
from dsa_collections.ds.linked_list import SingleLinkedList


def rearrange(L: SingleLinkedList):
    fast = L._head
    slow = L._head

    # 找到中间位置的节点
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    # 重定位
    first = L._head.next
    second = slow.next

    # 分割为2个链表
    slow.next = None

    # 逆置后半部分second
    curr = second
    prev = None
    while curr:
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_

    # 第二个链表second指针重定位
    second = prev

    p = first
    q = second

    # 交错连接合并
    while p and q:
        p_n = p.next
        q_n = q.next

        p.next = q
        q.next = p_n

        p = p_n
        q = q_n
