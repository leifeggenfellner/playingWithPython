def interpolationSearch(arr, length, target):
    low = 0
    high = length - 1

    while arr[high] != arr[low] and target >= arr[low] and target <= arr[high]:
        mid = round(low + ((target - arr[low]) * (high - low) / (arr[high] - arr[low])))

        if arr[mid] < target:
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1
        else:
            return mid

    if target == arr[low]:
        return low
    else:
        return -1