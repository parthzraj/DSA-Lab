nums = [5,7,81,25,6,4,3,4]
"""
============================================================
                    SELECTION SORT
============================================================

1. WHAT IS SELECTION SORT?
--------------------------
Selection Sort is a simple sorting algorithm that sorts a
list by repeatedly finding the SMALLEST element from the
unsorted part of the list and placing it at the correct
position.

2. HOW DOES IT WORK?
--------------------
- Divide the list into two parts:
    1. Sorted part   -> Elements already in correct order.
    2. Unsorted part -> Elements that are yet to be sorted.

- Initially, the entire list is unsorted.
- Find the smallest element in the unsorted part.
- Swap it with the first element of the unsorted part.
- The sorted part grows by one element.
- Repeat until the entire list is sorted.

3. EXAMPLE
----------
Original List:
[64, 25, 12, 22, 11]

PASS 1:
Smallest element = 11
Swap 11 with 64
[11, 25, 12, 22, 64]

PASS 2:
Smallest element = 12
Swap 12 with 25
[11, 12, 25, 22, 64]

PASS 3:
Smallest element = 22
Swap 22 with 25
[11, 12, 22, 25, 64]

PASS 4:
Smallest element = 25
No swap required
[11, 12, 22, 25, 64]

Sorted List:
[11, 12, 22, 25, 64]

4. IMPORTANT VARIABLES
----------------------
- i       : Represents the current position where the
            smallest element should be placed.
- j       : Used to traverse the remaining unsorted elements.
- min_idx : Stores the INDEX of the smallest element found.

5. IMPORTANT LOGIC
------------------
- The outer loop selects the position to be filled.
- The inner loop searches for the smallest element.
- min_idx is updated whenever a smaller element is found.
- After the inner loop finishes, swap arr[i] and arr[min_idx].

6. NUMBER OF PASSES
-------------------
For a list containing n elements:
Number of passes = n - 1

7. TIME AND SPACE COMPLEXITY
----------------------------
Best Case:    O(n²)
Average Case: O(n²)
Worst Case:   O(n²)

Space Complexity: O(1)

Why?
- Every element is compared with the remaining unsorted
  elements, even if the list is already sorted.
- Only a few extra variables are used.

8. IMPORTANT PROPERTIES
-----------------------
- In-place sorting algorithm.
- Generally NOT stable.
- Performs at most n - 1 swaps.
- Suitable for understanding basic sorting logic.

============================================================
"""


