# The leader's val >= all subsequent elements in the array.

# leader i, subs j >= i + 1(1 to n),
# arr[i] > max(arr[i+1], arr[i+2], ..., arr[n - 1])

# BF is ignored

# 16 17 4 3 5 2

# find n series
# s1: 17 4 3 5 2
# s2: 5 2
# s3: 2

# Reverse iteration

def leaders(arr):
    _leaders = []

    local_max = - 2 ** 32
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] >= local_max:
            local_max = arr[i]
            _leaders.append(local_max)

    return _leaders[::-1]
