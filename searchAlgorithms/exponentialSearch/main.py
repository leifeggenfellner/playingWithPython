from math import floor

# Expects a sorted array, the length of the array, and the number you wish to find the index of.
def binarySearch(arr, start, length, target):

    l = start
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

def exponentialSearch(arr, length, target):
    if length == 0:
        return -1
    
    bound = 1
    while bound < length and arr[bound] < target:
        bound *= 2
    
    return binarySearch(arr, bound / 2, min(bound + 1, length), target)