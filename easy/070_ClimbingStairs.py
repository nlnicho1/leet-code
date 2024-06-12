# Level: Easy

# Problem:
#   You are climbing a staircase. It takes n steps to reach the top.
#
#   Each time you can either climb 1 or 2 steps. How many distinct ways
#   can you climb to the top?

# Sample Input
steps = 5    # output: 8


# Decision tree, Depth-First Search not repeating branches = O(n) - memoization
# Bottom-up, fibonacci
def calculate_distinct_paths(num_steps):
    one = 1
    two = 1

    for i in range(num_steps - 1):
        temp = one
        one = one + two
        two = temp

    return one


result = calculate_distinct_paths(steps)
print("Distinct ways to the top:", result)




