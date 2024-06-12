# Level: Easy

# Problem:
#   Given an array nums containing n distinct numbers in the range [0, n],
#   return the only number in the range that is missing from the array

# Sample Input
nums = [3, 0, 1, 4, 5, 6, 7, 8, 10, 9]    # Output 2


# 0(n) uses a hashset
def missing_number(numbers):
    result = len(numbers)

    for i in range(len(numbers)):
        result += (i - numbers[i])

    return result


result = missing_number(nums)
print(f"The missing number in the array: {result}")
