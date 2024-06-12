# Level: Medium

# Problem:
#   Given an integer array nums, find the contiguous subarray (containing
#   at least one number) which has the largest product

# Notes
#   Dynamic programming problem
#   We will also need to keep track of the min subarray

# Sample Input
nums = [2, 3, -2, 4]


# Patterns? O(n)
#   - all positive -> always increasing
#   - all negative -> increasing
#   - edge case -> 0, reset min/max to 1
def calculate_max_product_of_subarray(numbers):
    max_product_subarray = max(numbers)
    current_min, current_max = 1, 1

    for n in numbers:
        if n == 0:
            current_min, current_max = 1, 1
            continue
        temp = current_max
        current_max = max(n * current_max, n * current_min, n)
        current_min = min(n * temp, n * current_min, n)
        max_product_subarray = max(max_product_subarray, current_max, current_min)

    return max_product_subarray


result = calculate_max_product_of_subarray(nums)
print(f"The max product of the subarray: {result}")

