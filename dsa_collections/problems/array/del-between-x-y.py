def del_between_x_y(arr: list, x, y):
    i = 0
    k = 0

    while i < len(arr):
        if arr[i] < x or arr[i] > y:
            arr[k] = arr[i]
            k += 1
        i += 1

    for i in range(len(arr) - k):
        arr.pop()
