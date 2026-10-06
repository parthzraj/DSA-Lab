import random
import time

numbers = [random.randint(1, 100000) for _ in range(10000)]

with open("generated_numbers.txt", "w") as file:
    for number in numbers:
        file.write(str(number) + "\n")


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def heapify(arr, n, i):
    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


merge_array = numbers.copy()
heap_array = numbers.copy()

start = time.perf_counter()
merge_result = merge_sort(merge_array)
merge_time = time.perf_counter() - start

start = time.perf_counter()
heap_result = heap_sort(heap_array)
heap_time = time.perf_counter() - start

with open("sorted_numbers.txt", "w") as file:
    for number in merge_result:
        file.write(str(number) + "\n")

print("--------------------------------------")
print("        SORTING COMPARISON")
print("--------------------------------------")

print("Number of elements:", len(numbers))
print("\nMerge Sort Time :", merge_time, "seconds")
print("Heap Sort Time  :", heap_time, "seconds")

print("\nBoth sorting results are same:",
      merge_result == heap_result)

if merge_time < heap_time:
    print("\nResult: Merge Sort is faster.")
elif heap_time < merge_time:
    print("\nResult: Heap Sort is faster.")
else:
    print("\nResult: Both took the same time.")

print("\nFiles created:")
print("1. generated_numbers.txt")
print("2. sorted_numbers.txt")
