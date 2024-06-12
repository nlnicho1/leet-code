# Level: Medium

# Problem:
#   Given an integer array nums, return an array answer such that answer[i] is
#   equal to the product of all elements of nums EXCEPT nums[i]
#
#   The product of any prefix or suffix of nums is guaranteed to fit in a
#   32-bit integer
#
#   You must write an algorithm that runs in O(n) time and without using the
#   division operation

# Sample Input
nums = [1, 2, 3, 4]


# Prefix, Postfix - Time = O(n), Memory = O(1)
def product_of_array_except_self(numbers):
    solution = [1] * len(numbers)

    pre = 1
    for i in range(len(numbers)):
        solution[i] = pre
        pre *= numbers[i]

    post = 1
    for i in range(len(numbers) - 1, -1, -1):
        solution[i] *= post
        post *= numbers[i]

    return solution


print(f"Product of array except self: {product_of_array_except_self(nums)}")



