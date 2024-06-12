# Level: Easy

# Problem:
#   Say you have an array for which the ith element is the price of a given
#   stock on day i.
#
#   If you were only permitted to complete at most one transaction (i.e., buy
#   one and sell one share of stock), design an algorithm to find the max
#   profit
#
#   Note that you cannot sell stock before you buy one

# Sample Input
prices = [7, 1, 5, 3, 6, 4]


# Sliding Window (Left Pointer, Right Pointer) - Memory: O(1), Time: O(n)
def calculate_max_profit(stock_prices):
    left, right = 0, 1    # left = buy, right = sell
    max_profit = 0

    while right < len(stock_prices):
        if stock_prices[left] < stock_prices[right]:
            profit = stock_prices[right] - stock_prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right

        right += 1

    return max_profit


result = calculate_max_profit(prices)
print("Max profit: ", result)
