"""
============================================================
                      BUBBLE SORT
============================================================

1. WHAT IS BUBBLE SORT?
-----------------------
Bubble Sort is a simple sorting algorithm that repeatedly
compares TWO ADJACENT elements and swaps them if they are
in the wrong order.

After every pass, the largest unsorted element moves
(or "bubbles up") to its correct position at the END
of the list.

2. HOW DOES IT WORK?
--------------------
- Start comparing elements from the beginning of the list.
- Compare two adjacent elements: arr[j] and arr[j + 1].
- If the first element is greater than the second, SWAP them.
- Otherwise, leave them unchanged.
- Continue until the end of the unsorted portion.
- After each pass, the largest unsorted element reaches
  its correct position.
- Repeat until the list is sorted.

3. EXAMPLE
----------
Original List:
[5, 3, 8, 4, 2]

PASS 1:
Compare 5 and 3 -> Swap
[3, 5, 8, 4, 2]

Compare 5 and 8 -> No swap
[3, 5, 8, 4, 2]

Compare 8 and 4 -> Swap
[3, 5, 4, 8, 2]

Compare 8 and 2 -> Swap
[3, 5, 4, 2, 8]

Largest element (8) is now in its correct position.

PASS 2:
Compare 3 and 5 -> No swap
[3, 5, 4, 2, 8]

Compare 5 and 4 -> Swap
[3, 4, 5, 2, 8]

Compare 5 and 2 -> Swap
[3, 4, 2, 5, 8]

PASS 3:
Compare 3 and 4 -> No swap
[3, 4, 2, 5, 8]

Compare 4 and 2 -> Swap
[3, 2, 4, 5, 8]

PASS 4:
Compare 3 and 2 -> Swap
[2, 3, 4, 5, 8]

SORTED LIST:
[2, 3, 4, 5, 8]

4. IMPORTANT VARIABLES
----------------------
- i : Controls the number of passes.
- j : Traverses the list and compares adjacent elements.
- arr[j] : Current element.
- arr[j + 1] : Next adjacent element.

5. IMPORTANT LOGIC
------------------
- The outer loop controls the passes.
- The inner loop compares adjacent elements.
- arr[j] > arr[j + 1] checks whether swapping is required.
- If the condition is TRUE, swap both elements.
- After every pass, the largest unsorted element reaches
  its correct position at the end.

WHY DOES THE INNER LOOP USE (n - i - 1)?
----------------------------------------
- n = Total number of elements.
- i = Number of passes already completed.
- After every pass, one largest element is sorted at the end.
- Therefore, there is no need to compare the sorted elements.

6. NUMBER OF PASSES
-------------------
For a list containing n elements:

Maximum passes = n - 1

7. TIME AND SPACE COMPLEXITY
----------------------------
Best Case:    O(n)     (Optimized Bubble Sort)
Average Case: O(n²)
Worst Case:   O(n²)

Space Complexity: O(1)

Why?
- Adjacent elements are repeatedly compared.
- Only a few extra variables are required.
- No additional array is needed.

NOTE:
Without an optimization using a 'swapped' flag,
even the best-case time complexity is O(n²).

8. IMPORTANT PROPERTIES
-----------------------
- In-place sorting algorithm.
- STABLE sorting algorithm.
- Comparison-based sorting algorithm.
- Can be optimized using a swapped flag.
- Suitable for small datasets and learning sorting logic.

9. OPTIMIZATION USING SWAPPED FLAG
----------------------------------
- Initially, set swapped = False before each pass.
- Whenever two elements are swapped, set swapped = True.
- After completing a pass, check the value of swapped.
- If swapped is still False, no elements were exchanged.
- This means the list is already sorted.
- Stop the algorithm using BREAK.

============================================================
"""

nums = [5, 7, 81, 25, 6, 4, 3, 4]
n = len(nums)

def bubbleSort(arr, n):
    for i in range(n):
        isSwapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                isSwapped = True

        if not isSwapped:
            break

bubbleSort(nums, n)
print("sorted", nums)