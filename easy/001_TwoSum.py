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
    prev_numbers_map = {}

    for i, n in enumerate(nums):
        difference = target - n
        if difference in prev_numbers_map:
            return [prev_numbers_map[difference], i]
        prev_numbers_map[n] = i

    return


result = two_sum(numbers, target_sum)
print("Indices of the two numbers that add up to the target are:", result)
