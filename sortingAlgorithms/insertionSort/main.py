# Expects an array of numbers and the length of the array - 1
def insertionSort(arr, length):
    if length > 0:
        insertionSort(arr, length - 1)
        x = arr[length]
        j = length - 1

        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = x
