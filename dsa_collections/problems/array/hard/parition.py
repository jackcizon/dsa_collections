"""
Source:
2016 National Graduate Entrance Exam (CS 408), Question 43 
"""

# Partition
"""
Given an array A of postive int(len(A) = n >= 2),
partition it into 2 disjoint subsets A1 and A2.

let n1 and n2 be the numbers of elements in A1 and A2,
and let S1 and S2 be the sums of the elements in A1 and A2.

dedign a effecient partition algorithm such that:
Constraints:
1. abs(n1 - n2) is minimized.
2. abs(S1 - S2) is maximized.

#############################################
my thoughts:
1. div into 2 parts, because n = floor(n/2) + ceil(n/2)
    while floor == int(n/2) - 1, (Constraint 1)
    min = 0 or 1
    左边放 floor(n/2)，右边放 ceil(n/2)

2. use qsort's partition algo.
    the sub-series than in the front of the "final pivot", all elements <= pivot(need do 1 or multi partitions)
    The same applies to the right side.(elements >= pivot)
    运气好，一次交换都不需要，非常巧pivot在中心，
    前面刚好小于pivot，后面大于pivot，
    运气不好得话，丢弃左边或者右边，对剩余区间重新选pivot，再partition

tips:
一个细节，pivot选择arr[low]或者arr[high]和后面的while loop的比较先后顺序有关
"""

from re import A
import re


def partition(arr):
    n = len(arr)
    mid = n // 2  # 5 // 2 = 2， 4 // 2 = 2
    
    pivot = 0
    low = 0
    high = n - 1
    
    # 运气不好时继续partition的索引
    low0 = 0 
    high0 = 0
    
    left_sum = 0
    right_sum = 0
    
    continue_flag = True
    
    while continue_flag:
        # select a pivot, temp save arr[low]
        pivot = arr[low]
        
        # parition algo
        while low < high:
            # 必须先比较high，否则high可能会因为先比较low导致数值丢失
            while low < high and arr[high] >= pivot:
                high -= 1
            
            if low != high:
                arr[low] = arr[high]
            
            # 对称
            while low < high and arr[low] <= pivot:
                low += 1
            
            if low != high:
                arr[high] = arr[low]
    
        # pivot 必须位于中心位置，偏差0或1个单位
        arr[low] = pivot
        # partition(s) over
        if low == mid:
            continue_flag = False 
        else:
            if low < mid - 1:
                low += 1
                low0 = low
                high = high0
            else: # 对称
                high -= 1
                high0 = high
                low = low0
        
    # sum，注意边界
    for i in range(mid):
        left_sum += arr[i]
    for i in range(mid, n):
        right_sum += arr[i]
    
    return abs(left_sum - right_sum)