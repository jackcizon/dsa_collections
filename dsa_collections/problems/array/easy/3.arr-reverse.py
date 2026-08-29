# Array Reverse


def reverse(arr):
    length = len(arr)

    left = 0
    right = length - 1
    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp

        left += 1
        right -= 1
