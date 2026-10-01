def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                # Swap the two elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Example
numbers = [5, 2, 8, 1, 3]

print("Before sorting:", numbers)

bubble_sort(numbers)

print("After sorting:", numbers)