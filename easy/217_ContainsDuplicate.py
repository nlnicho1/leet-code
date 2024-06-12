# Level: Easy

# Problem:
#   Given an integer array nums, return true if any value appears at least twice
#   in the array, false if every element is distinct

# Sample Input
nums = [1, 2, 3, 1]

# Brute Force - Memory: O(1), Time: O(n^2)

# Unique Length vs Array Length

# Sort - Time: O(nlog(n)), Memory: O(1)


# Hash Set - Time: O(n),  Memory: O(n)
def contains_duplicate(numbers):
    hash_set = set()
    has_duplicate = False

    for n in numbers:
        if n in hash_set:
            has_duplicate = True
            break
        hash_set.add(n)

    return has_duplicate


result = contains_duplicate(nums)
print(f"Array contains duplicate: {result}")