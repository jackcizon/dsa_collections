# 正数在偶数位置
# 负数在奇数位置

def arrange_bu_sign(arr):
    # setup
    negative = []
    positive = []

    # append
    for a in arr:
        if a > 0:
            positive.append(a)
        else:
            negative.append(a)

    # min length, loop ptrs
    min_length = min(len(positive), len(negative)) * 2  # 确保各有n个数
    pos = 0
    neg = 0

    for i in range(min_length):
        if i % 2 == 0:
            arr[i] = positive[pos]
            pos += 1
        else:
            arr[i] = negative[neg]
            neg += 1

    i = min_length

    if len(positive) == len(negative):
        return
    elif len(positive) > len(negative):
        while pos < len(positive):
            arr[i] = positive[pos]
            pos += 1
            i += 1
    else:
        while neg < len(negative):
            arr[i] = negative[neg]
            neg += 1
            i += 1
