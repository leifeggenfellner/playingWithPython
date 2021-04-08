from math import floor

# Expects a sorted array, the length of the array, and the number you wish to find the index of.
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
    return -1
