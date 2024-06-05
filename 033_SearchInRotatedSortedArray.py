# Level: Medium

# Problem:
#   Suppose an array sorted in ascending order is rotated at some pivot unknown
#   to you beforehand
#
#   i.e. [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
#
#   You are given a target value to search. If found in the array return its
#   index, otherwise return -1

# Assumptions:
#   1. No Duplicates Exist
#   2. Your algorithm's runtime complexity must be in the order of O(log n)
#      ** If it is better than O(n) then it is probably accomplished via binary
#         search

# Sample Input
numbers = [4, 5, 6, 7, 0, 1, 2]
target_value = 0


# Binary Search
# Notes
#   3 pointers: Left, Middle, Right
#   left <= right
#   if L <= M, we're in the left portion
def search_rotated_sorted_array(nums, target):
    left = 0
    right = len(nums) - 1
    target_index = -1

    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            target_index = mid
        # left sorted portion
        if nums[left] <= nums[mid]:
            # Search Right, target < nums[left]: Search Right AND Left
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            # Search Left
            else:
                right = mid - 1
        # right sorted portion
        else:
            # Search Left
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            # Search Right
            else:
                left = mid + 1

    return target_index


result = search_rotated_sorted_array(numbers, target_value)
print("Index of target value:", result)