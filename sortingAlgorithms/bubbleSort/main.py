# Expects an array of numbers
def bubbleSort(arr):
    length = len(arr)

    while length > 1:
        newn = 0
        for i in range(1, length):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                newn = i
        length = newn