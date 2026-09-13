def same_values(a, b, c, length):
    i = 0
    j = 0
    k = 0

    values = []

    while i < length and j < length and k < length:
        if a[i] == b[j] == c[k]:
            values.append(a[i])
            i += 1
            j += 1
            k += 1
        else:
            local_max = max(a[i], b[j], c[k])
            if a[i] < local_max:
                i += 1
            if b[j] < local_max:
                j += 1
            if c[k] < local_max:
                k += 1

    return values
