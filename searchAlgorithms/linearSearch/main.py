def linearSearch(arr, length, target):
    for i in range(length - 1, -1, -1):
        if arr[i] == target:
            return i
    return "Element not in array"


def sortedLinearSearch(arr, length, target):
    arr.sort()
    i = 0
    for j in range(length - 1, -1, -1):
        if arr[j] <= target:
            if arr[j] == target:
                return i
            else:
                return "Element not in array"
        i = i + 1
