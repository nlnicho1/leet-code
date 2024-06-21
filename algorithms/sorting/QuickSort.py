# Time Complexity: O(nlogn)
# Space Complexity: O(logn)

def quick_sort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Recursive case
        pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
        left = [x for x in arr if x < pivot]  # Elements less than the pivot
        middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
        right = [x for x in arr if x > pivot]  # Elements greater than the pivot

        return quick_sort(left) + middle + quick_sort(right)


def quick_sort_in_place(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)
        # Recursively sort the sub-arrays
        quick_sort_in_place(arr, low, pi-1)
        quick_sort_in_place(arr, pi+1, high)

    return arr


def partition(arr, low, high):
    pivot = arr[high]  # Choose the rightmost element as the pivot
    i = low - 1  # Pointer for the smaller element
    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            i += 1  # Increment the smaller element pointer
            arr[i], arr[j] = arr[j], arr[i]  # Swap the elements
    arr[i+1], arr[high] = arr[high], arr[i+1]  # Swap the pivot element
    return i + 1  # Return the partition index


# Example usage
int_array = [4, 7, 6, 3, 2, 1, 5]
char_array = ["b", "c", "d", "g", "a", "e", "f"]

print(f"Sorted Integer Array: {quick_sort(int_array)}")
print(f"Sorted Character Array: {quick_sort(char_array)}")
print(f"Sorted Integer Array Using Quick Sort In Place: "
      f"{quick_sort_in_place(int_array, 0, len(int_array)-1)}")
