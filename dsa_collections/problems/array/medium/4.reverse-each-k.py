# 整数数组arr，和整数k，
# 每k个为1组，反转，
# 不足k个的（大致是mod k = r != 0,有余数），最后r个自行反转
# Given an int arr and an int k, 
# divide the array into groups of k consecutive elements and reverse each group.
# If fewer than k elements remain at the end, reverse those remaining elements as well.


def _reverse(arr, start, end):
    """helper function for inner call"""
    left = start
    right = end
    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
    
        left += 1
        right -= 1


def reverse_k(arr, k):
    length = len(arr)
    
    if k > length:
        _reverse(arr, start=0, end=length - 1)
        return
    
    groups = length // k
    remainder = length % k
    
    # index  0 1 2   3 4 5   6 7
    # arr   [1 2 3] [4 5 6] [7 8]   
    # length = 8
    # k = 3
    # groups = 8 // 3 = 2
    # remainder = 8 mod 3 = 2
    
    # 后r个余数
    i = length - remainder
    j = length - 1
    _reverse(arr, start=i, end=j)
    
    # 前面的groups组数
    i = 0
    j = i + k - 1
    for _ in range(groups):  # 0, 1
        _reverse(arr, start=i, end=j)
        i += k
        j = i + k - 1
