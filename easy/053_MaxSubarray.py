# Level: Easy

# Problem:
#   Given an integer array nums, find the contiguous subarray (containing
#   at least one number) which has the largest sum

# Sample Input
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


# Kadane's Algorithm, Similar to Sliding Window - O(n)
# left pointer shifted if negative prefix, keep moving right pointer
def maximum_subarray(nums):
    max_subarray = nums[0]
    current_sum = 0

    for n in nums:
        if current_sum < 0:
            current_sum = 0
        current_sum += n
        max_subarray = max(max_subarray, current_sum)

    return max_subarray


result = maximum_subarray(numbers)
print("Maximum Subarray:", result)
