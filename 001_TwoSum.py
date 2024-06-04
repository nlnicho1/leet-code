# Level: Easy

# Problem:
#   Given an array of integers, return indices of the two numbers such that they
#   add up to a specific target.

# Assumptions:
#   1. Each input would have exactly ONE solution
#   2. You may not use the same element twice

# Sample Input
numArray = [2, 1, 5, 3]
target = 4

# HASH MAP - O(n)
prevMap = {}    # val : index
solution = []

for i, n in enumerate(numArray):
    diff = target - n
    if diff in prevMap:
        solution.append(prevMap[diff])
        solution.append(i)
        break
    prevMap[n] = i

print(solution)
