from dsa_collections.ds.linked_list import SingleLinkedList


def max_twin_sum(L: SingleLinkedList):
    """
    n = len(L)
    max(i, 1, n - 1, sum(L[i]+L[n-i])

    这是非常简单的数组孪生和算法
    在数组中，a[i]+a[n−1−i]

    迁移到链表中，变得复杂
    1.找到中点和终点
    2.对L后半部分反转
    3.从头开始，L[i]+L[i+n//2],记录max_sum

    :param L:
    :return:
    """
    slow = L._head.next
    fast = L._head.next

    # 找到终点和中点
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse后半段
    prev = None
    curr = slow
    while curr:
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_

    # 前半部分+后半部分（反转后）
    p = L._head.next  # 首位元素
    q = prev  # prev 在 n//2 处
    max_sum = 0
    while q:
        max_sum = max(max_sum, p.value + q.value)
        p = p.next
        q = q.next

    return max_sum
