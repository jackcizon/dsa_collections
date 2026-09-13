def del_all_x(arr, x):
    i = 0
    k = 0

    while i < len(arr):
        if arr[i] != x:
            arr[k] = arr[i]
            k += 1
        i += 1

    for i in range(len(arr) - k):
        arr.pop()


if __name__ == '__main__':
    a = [1, 2, 3, 4, -1, -1, 1]
    del_all_x(a, -1)
    print(len(a))
