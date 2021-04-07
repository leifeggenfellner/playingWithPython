# Expects a sorted array, the length of the array, and the number you wish to find the index of.
def fibonacciSearch(arr, length, target):
    f2 = 0
    f1 = 1
    fm = f2 + f1
    
    offset = -1

    while fm < length:
        f2 = f1
        f1 = fm
        fm = f2 + f1
    
    while fm > 1:
        i = min(offset + f2, length - 1)

        if arr[i] < target:
            fm = f1
            f1 = f2
            f2 = fm - f1
            offset = i
        elif arr[i] > target:
            fm = f2
            f1 = f1 - f2
            f2 = fm - f1
        else:
            return i

    if f1 and arr[offset + 1] == target:
        return offset + 1
    
    return "Element not in array"