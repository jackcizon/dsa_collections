# Replace with Adjacent Multiplication

# Given an array arr[], replace each element with the product of itself and its adjacent elements.

# For index i:

# arr[i] = arr[i-1] * arr[i] * arr[i+1]
# Assume the prev of the first and the next of the last as 1.


def m_arr_adj_inplace(arr):
    length = len(arr)
    prev = 1
    for i in range(length):
        if i < length - 1:
            next_ = arr[i + 1]
        else:
            next_ = 1
        current = arr[i]

        arr[i] = prev * current * next_

        prev = current
