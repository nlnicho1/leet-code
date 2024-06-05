# Level: Medium

# Problem:
#   Given an array nums of n integers, are there elements a, b, c in nums such
#   that a + b + c = 0? Find all unique triplet in the array which gives the
#   sum of 0

# Note:
#   1. The solution set must not contain duplicate triplets

# Sample Input
numbers = [-1, 0, 1, 2, -1, -4]


# Sorted Array with Left and Right Pointer
# Complexity: O(nlogn) + O(n^2)
def three_sum(nums):
    results = []
    nums.sort()

    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue    # don't reuse value

        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum_of_three_nums = num + nums[left] + nums[right]
            if sum_of_three_nums > 0:
                right -= 1
            elif sum_of_three_nums < 0:
                left += 1
            else:
                results.append([num, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    return results


result = three_sum(numbers)
print("Sets of the three numbers that add up to zero:", result)
