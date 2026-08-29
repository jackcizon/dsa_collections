# the math behind this problem.
# use increasing series.
# Elementary school mathematical modeling
# 小学数学问题，呵呵

# stock arr = 100 180 260 310 40 535 695
# Difference =  80  80  50   |  495 160

# series 1: 100 180 260 310
# series 2: 40 535 695

# each series must be Increasing
# the profit
# = The sum of the differences between adjacent elements in each sequence
# = 80 + 80 + 50
# += 495 + 160


def m_stocks_buy_sell(stock_arr):
    profit = 0

    for i in range(1, len(stock_arr)):
        if stock_arr[i] > stock_arr[i - 1]:
            profit += stock_arr[i] - stock_arr[i - 1]

    return profit