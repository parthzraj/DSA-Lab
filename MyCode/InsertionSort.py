nums = [5, 7, 81, 25, 6, 4, 3, 4]
n = len(nums)


def insertionSort(arr, n):
    for i in range(1, n):
        current = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current


print(nums, "- Unsorted Form")
insertionSort(nums, n)
print(nums, "- Sorted Form")