from typing import Union


def binary_search(arr: list, val: Union[int, float]) -> bool:
    left: int = 0
    right: int = len(arr) - 1

    while left <= right:
        mid: int = (left + right) // 2
        if arr[mid] == val:
            return True
        elif arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return False
