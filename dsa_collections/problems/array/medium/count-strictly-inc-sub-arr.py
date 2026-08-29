# 在一个超级大数组中，某个检测到的递增序列为如下：
# [1,2,3,4,5], n = 5
# 该递增序列中，当sbustr：
# len = 2
# [1,2]
# [2,3]
# [3,4]
# [4,5]
# c = 4 = n - 1
# 当substr：
# len = 3, 
# [1 2 3]
# [2 3 4]
# [3 4 5]
# c = 3 = n - 2
# ....
# ....
# 直到 [1 2 3 4 5]
# c = 1 = n - 4
#  同理，对于数组中检测到的某个长度为n的子递增序列中，它可能的substr(递增)个数总和：
# 该子序列的总递增substr个数 
# (n - 1) + (n -2) + .... + 1 
# = 1/2 * (n - 1) * (n-1+1)
# = 1/2 * (n-1)*n


def count_strictly_inc_sub_arr(arr):
    n = len(arr)
    
    if n < 2:
        return 0
    
    count = 0
    length = 1
    
    for i in range(1, n):
        if arr[i] > arr[i - 1]: # inc
            length += 1
        else: # stat, over, go next
            count += length * (length - 1) // 2 # 统计该substr的可能个数，见上方注释
            length = 1 # reset
        
    count += length * (length - 1) // 2
    
    return count