from math import floor

def partition(arr, low, high):
    pivot = arr[high]

    i = (low - 1)

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return (i + 1)


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# Finds index of sorted array. Sorts array if it isn't sorted.
def binarySearch(arr, n, target):
    if not all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        quickSort(arr, 0, len(arr) - 1)

    l = 0
    r = n - 1

    while l <= r:
        m = floor((l + r) / 2)
        if arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1
        else:
            return m
    return "Number not in array"
