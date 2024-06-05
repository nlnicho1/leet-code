# Level: Easy

# Problem:
#   Given an array of integers, return indices of the two numbers such that they
#   add up to a specific target.

# Assumptions:
#   1. Each input would have exactly ONE solution
#   2. You may not use the same element twice

# Sample Input
numbers = [2, 1, 5, 3]
target_sum = 4


def two_sum(nums, target):
    prev_map = {}    # val : index
    solution = []

    for i, n in enumerate(nums):
        diff = target - n

        if diff in prev_map:
            solution.append(prev_map[diff])
            solution.append(i)
            break

        prev_map[n] = i

    return solution


result = two_sum(numbers, target_sum)
print("Indices of the two numbers that add up to the target are:", result)
