class BinarySearch:
    @staticmethod
    def main(arr: list, val: int):
        left: int = 0
        right: int = len(arr) - 1

        while left <= right:
            mid: int = (left + right) // 2
            if arr[mid] == val:
                return True
            elif arr[mid] < val:
                right = mid - 1
            else:
                left = mid + 1
        return False
