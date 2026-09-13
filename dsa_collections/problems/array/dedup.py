def dedup(arr: list):
    i = 0
    k = 1
    j = 0

    while k < len(arr):
        if arr[i] != arr[k]:
            i += 1
            arr[i] = arr[k]
            k += 1
        else:
            k += 1
            j += 1

    for _ in range(j):
        arr.pop()
