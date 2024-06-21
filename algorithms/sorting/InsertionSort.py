# Time Complexity: O(n^2)
# Space Complexity: O(1)

def insertion_sort(arr):
    # Traverse from 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


# Example usage
array = [64, 25, 12, 22, 11]
print("Sorted array is:", insertion_sort(array))
