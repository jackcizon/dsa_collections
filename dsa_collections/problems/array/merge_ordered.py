def merge_ordered(a, b):
    i = 0
    j = 0
    k = 0

    len_a = len(a)
    len_b = len(b)

    c = [None] * (len_a + len_b)

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        c[k] = a[i]
        k += 1
        i += 1

    while j < len_b:
        c[k] = b[j]
        k += 1
        j += 1
