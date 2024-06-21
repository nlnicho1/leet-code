
def heap_sort(arr):
    # TODO
    # build_max_heap(arr)

    # for i = n to 1
    #   swap(arr[1], arr[i])
    #   n = n - 1
    #   heapify(arr, i)

    return 0


def build_max_heap(arr):
    # n = elements_in(arr)

    # for i = floor(n/2) to 1
    #   heapify(arr, i)

    return 0


def heapify(arr, i):
    # left = 2i
    # right = 2i + 1

    # if (left <= n) and (arr[right] > arr[max])
    #   max = right

    # if (max != i)
    #   swap(arr[i], arr[max])
    #   heapify(arr, max)

    return 0


# Example usage
array = [64, 25, 12, 22, 11]
print("Sorted array is:", heap_sort(array))