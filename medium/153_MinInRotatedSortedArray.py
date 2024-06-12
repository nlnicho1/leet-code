# Level: Medium

# Problem:
#   Suppose an array of length n sorted in ascending order is rotated between 1
#   and n times. For example, the array nums = [0, 1, 2, 3, 4, 5, 6, 7] might
#   become:
#       [4, 5, 6, 7, 0, 1, 2] if it was rotated 4 times
#       [0, 1, 2, 4, 5, 6, 7] if it was rotated 7 times
#
#   Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
#   in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
#   Given the sorted rotated array nums of unique elements, return the minimum
#   element of this array
#
# You must right an algorithm that runs in O(log n) time

# Sample Input
nums = [3, 4, 5, 1, 2]


# Binary Search Algorithm - usually runs in O(log n) time
# Only works on a rotated sorted array
def min_in_rotated_sorted_array(numbers):
    minimum = numbers[0]
    left, right, = 0, len(numbers) - 1

    while left <= right:
        if numbers[left] < numbers[right]:       # sorted array
            minimum = min(minimum, numbers[left])
            break
        midpoint = (left + right) // 2
        minimum = min(minimum, numbers[midpoint])
        if numbers[midpoint] >= numbers[left]:
            left = midpoint + 1
        else:
            right = midpoint - 1

    return minimum


result = min_in_rotated_sorted_array(nums)
print(f"Minimum value in the rotated, sorted array: {result}")

