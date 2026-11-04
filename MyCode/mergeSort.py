nums = [5, 7, 81, 25, 6, 4, 3, 4] #divide and merge


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = mergeSort(arr[:middle])
    right = mergeSort(arr[middle:])

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


print(nums, "- Unsorted Form")
nums = mergeSort(nums)
print(nums, "- Sorted Form")