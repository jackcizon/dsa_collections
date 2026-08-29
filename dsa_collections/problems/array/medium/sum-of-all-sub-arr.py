# 1 2 3 4
# len = 4 = n

"""
all sub-series:
1
1 2
1 2 3
1 2 3 4

2
2 3
2 3 4

3
3 4

4

# contrib:

element | times | formula
1           4       (0+1)(4-0)=4  (i+1)(4-i)
2           6       
3           6
4           4

i+1 是因为下标从 0 开始,
在i之前有i个元素，
当 i=0 时，显然要 +1 来修正
即为前方还有i个元素

那么n - i就是后方元素个数

定理/推论：
if C = a[i] 在某个series中，
那么一定存在 series-Start-element <= C <= seires-End-element

所以这个元素在题目要求的答案中贡献了 N = (i+1)(n-i)次数
这个元素a[i] = C
的贡献总量 = C * N

然后总的贡献量，就是循环整个数组序列，和式求和
"""



def sum_of_all_sub_arr(arr):
    sum = 0
    n = len(arr)
    
    for i in range(n):
        sum += arr[i] * (i+1) * (n - i) # contrib
    
    return sum
