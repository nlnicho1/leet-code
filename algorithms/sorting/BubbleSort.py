# Time Complexity: O(n^2)
# Space Complexity: O(1)

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# Example usage
int_array = [4, 7, 6, 3, 2, 1, 5]
char_array = ["b", "c", "d", "g", "a", "e", "f"]

print(f"Sorted Integer Array: {bubble_sort(int_array)}")
print(f"Sorted Character Array: {bubble_sort(char_array)}")
