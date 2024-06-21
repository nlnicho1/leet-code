# Time Complexity: O(n^2)
# Space Complexity: O(1)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element
        min_idx = i
        # Iterate through the unsorted elements
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Update the index of the minimum element
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# Example usage
array = [64, 25, 12, 22, 11]
selection_sort(array)
print("Sorted array is:", selection_sort(array))