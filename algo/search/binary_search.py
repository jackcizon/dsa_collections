from __future__ import annotations


class BinarySearch:
    @staticmethod
    def main(arr: list, val: int | float):
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
