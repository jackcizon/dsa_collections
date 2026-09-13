"""
三元组a,b,c

d = min(abs(a-b)+abs(b-c)+abs(c-a))

a 属于升序数组s1
b s2
c s3
"""


def tuple_min_dist(s1, s2, s3):
    min_dists = []
    min_dist = 2 ** 32 - 1
    for i in range(len(s1)):
        for j in range(len(s2)):
            for k in range(len(s3)):
                a = s1[i]
                b = s2[j]
                c = s3[k]
                d = abs(a - b) + abs(b - c) + abs(c - a)
                if d < min_dist:  # 遇到更小距离，清理旧的三元组
                    min_dist = d
                    min_dists = [(a, b, c)]
                elif d == min_dist:
                    min_dists.append((a, b, c))

    return min_dist, min_dists


def tuple_min_dist_2(s1, s2, s3):
    i = j = k = 0
    min_dist = float('inf')
    min_dists = []

    while i < len(s1) and j < len(s2) and k < len(s3):
        a = s1[i]
        b = s2[j]
        c = s3[k]

        d = abs(a - b) + abs(b - c) + abs(c - a)

        if d < min_dist:  # 遇到更小距离，清理旧的三元组
            min_dist = d
            min_dists = [(a, b, c)]
        elif d == min_dist:
            min_dists.append((a, b, c))

        if a <= b and a <= c:
            i += 1
        elif b <= a and b <= c:
            j += 1
        else:
            k += 1

    return min_dist, min_dists
