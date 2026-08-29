def first_non_repeating(s: str):
    s = s.lower()

    # alphabet freq table
    f = [0] * 26

    ascii_a_number = ord('a')

    # record all
    for c in s:
        f[ord(c) - ascii_a_number] += 1

    # extract first
    for c in s:
        if f[ord(c) - ascii_a_number] == 1:
            return c

    return '$'
