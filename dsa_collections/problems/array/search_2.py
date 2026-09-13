def search_2(arr, x):
    """
    find, sway with successor
    if not found, insert
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            if mid < len(arr) - 1:
                arr[mid], arr[mid + 1] = arr[mid + 1], arr[mid]
            return
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    # 未找到，low 就是插入位置
    for i in range(len(arr) - 1, low - 1, -1):
        arr[i + 1] = arr[i]

    arr[low] = x
