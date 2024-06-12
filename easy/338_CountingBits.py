# Level: Easy

# Problem:
#   Given an integer n, return an array ans of length n + 1 such that for each
#   i (0 <= i <= n), ans[i] is the number of 1's in the binary representation
#   of i

# Sample Input
n = 2   # output [0, 1, 1]


# O(n) solution
def counting_bits(number):
    dp = [0] * (number + 1)
    offset = 1

    for i in range(1, number + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]

    return dp


result = counting_bits(n)
print(f"Binary representation: {result}")



