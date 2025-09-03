"""
Authors: Owen Cook, Wayne Yu
Creation Date: 2025/09/03
Program: Calculates maximum profit based on input stock prices
"""


def maxProfit(prices):
    # Assume no buy / sell activity if input does not have at least two prices
    if len(prices) < 2:
        return 0
    # Initialize max price and profit
    max_profit = 0
    max_price = prices[-1]
    # Iterate through prices to find the largest difference between each price and max price observed
    for i in range(len(prices) - 1, -1, -1):
        profit = max_price - prices[i]
        # Replace max profit with higher value
        max_profit = max(max_profit, profit)
        # Replace max price with higher value
        max_price = max(max_price, prices[i])
    return max_profit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    assert maxProfit(prices) == 5
    prices = [7,6,4,3,1]
    assert maxProfit(prices) == 0
    prices = [1, 700, 1, 6, 40, 32, 170]
    assert maxProfit(prices) == 699
