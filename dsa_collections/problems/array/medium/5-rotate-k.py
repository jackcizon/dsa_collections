# rotate k

def _reverse(arr, start, end):
    while start < end:
        tmp = arr[start]
        arr[start] = arr[end]
        arr[end] = tmp

        start += 1
        end -= 1


def rotate_k(arr, k):
    # 0 1 2 3 4
    length = len(arr)
    k %= length

    if length == 0 or k == 0:
        return

    _reverse(arr, 0, length - 1)
    # 4 3 2 1 0

    i = 0
    j = k - 1
    _reverse(arr, i, j)
    # 3 4 2 1 0

    i = k
    j = length - 1
    _reverse(arr, i, j)
    # 3 4 0 1 2
