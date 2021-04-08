from math import sqrt, floor

# Takes in sorted array, the full length of the array and the target number.
def jumpSearch(arr, length, target):
    a = 0
    b = floor(sqrt(length))

    while arr[min(b, length) - 1] < target:
        a = b
        b = b + floor(sqrt(length))

        if a >= length:
            return "Element not in array"
        
    while arr[a] < target:
        a = a + 1

        if a == min(b, length):
            return "Element not in array"

    if arr[a] == target:
        return a
    else:
        return "Element not in array"
