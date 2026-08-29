def is_substr(s, sub):
    i = 0
    j = 0

    while i < len(s) and j < len(sub):
        if s[i] == sub[j]:
            i += 1
        i += 1

    return j == len(sub)