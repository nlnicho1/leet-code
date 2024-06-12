# Level: Medium

# Problem:
#   Given n non-negative ints a1, a2, ..., where each represents a point at a
#   coordinate (i, ai) * n vertical lines are drawn such that the two endpoints
#   of the line i is at (i, ai) and (i, 0). Find two lines, which, together with
#   the x-axis forms a container such that the container contains the most water

# Note:
#   1. You may not slant the container

# Sample Input
container_heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]    # output: 49


# Linear Time solution - O(n)
# Shift the smaller height, if they're the same shift either one (or check the next height)
def find_max_volume(heights):
    max_volume = 0
    left_pos = 0
    right_pos = len(heights) - 1

    while left_pos < right_pos:
        area = (right_pos - left_pos) * min(heights[left_pos], heights[right_pos])
        max_volume = max(max_volume, area)

        if heights[left_pos] < heights[right_pos]:
            left_pos += 1
        else:
            right_pos -= 1

    return max_volume


result = find_max_volume(container_heights)
print("Max volume:", result)
