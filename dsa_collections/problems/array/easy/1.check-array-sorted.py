# - Check if an Array is Sorted

def is_sorted(arr):
    prev = -2 ** 32
    for i in arr:
        if i < prev:
            return False
        else:
            prev = i
    return True

