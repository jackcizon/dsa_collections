# i 天买入，j天卖出，j > i, 求max(j-i), 非常简单的小学数学问题

def buy_sell_stock(stock_arr):
    """股票值(数组元素)默认>0"""
    buy = stock_arr[0]
    max_profit = 0

    for i in range(1, len(stock_arr)):
        if stock_arr[i] < buy:
            buy = stock_arr[i]

        profit = stock_arr[i] - buy

        if max_profit < profit:
            max_profit = profit

    return max_profit


if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    print(buy_sell_stock(prices))