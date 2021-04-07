from math import floor

# Finds index of sorted array.
def binarySearch(arr, length, target):

    l = 0
    r = length - 1

    while l <= r:
        m = floor((l + r) / 2)
        if arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1
        else:
            return m
    return "Number not in array"
