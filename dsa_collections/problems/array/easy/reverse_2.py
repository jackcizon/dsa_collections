r"""
a1,a2,...,am,b1,b2,...,bn
||
\/
b1,b2,...,bn,a1,a2,...,am

rev(a)
rev(b)
rev(a+b)
"""


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


def reverse_2(arr, m, n):
    # rev(a)
    _reverse(arr, start=0, end=m - 1)
    # rev(b) n = len(arr) - m
    _reverse(arr, start=m, end=len(arr) - 1)
    # rev(a+b)
    _reverse(arr, 0, len(arr) - 1)
