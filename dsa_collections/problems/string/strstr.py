def _get_next(P: str):
    next_ = [-1] * len(P)

    i = 0
    j = -1

    while i < len(P) - 1:  # 排除P的整串
        if j == -1 or P[i] == P[j]:  # P(-1)是逆序
            i += 1
            j += 1
            next_[i] = j
        else:
            j = next_[j]

    return next_


def strstr(T: str, P: str):
    next_ = _get_next(P)

    i = 0
    j = 0

    while i < len(T) and j < len(P):
        if j == -1 or T[i] == P[j]:  # 匹配
            i += 1
            j += 1
        else:
            j = next_[j]

    if j == len(P):
        return i - j
    else:
        return -1
