"""
DSA IN PYTHON — SEARCHING AND SORTING
Complete beginner-friendly notes based on the supplied video transcript.

HOW TO USE THIS FILE
--------------------
1. Open this file in VS Code or any Python editor.
2. Read the explanations in order. They are written as comments/docstrings.
3. Run the file:
    python searching_sorting_complete_notes.py
4. Change the sample arrays and targets in the DEMO section.
5. The final self-tests check that the implementations work.

The notes cover the topics explained in the transcript:
- Why searching/sorting matter; what algorithms do
- Bubble, insertion, selection, merge, quick and counting sort
- Time/space complexity and sorting properties
- Sort Colors (Dutch National Flag / three pointers)
- Merge two sorted arrays in-place from the back
- Sorting intervals and removing overlaps
- Linear search and binary search
- Search Insert Position, lower bound and upper bound
- First and last occurrence of a target
- Mountain-array peak using binary search
- Binary search on the answer (Koko-style banana problem)
- Binary search on a row-major sorted 2D matrix
- Sort Array by Parity
- Executable examples, dry runs and practice tasks

IMPORTANT:
The transcript is an automatically generated Hindi transcript and contains
some speech-recognition mistakes and a few imprecise explanations. The code
below uses standard, correct Python implementations. Where a detail needs
precision, a clarification is included in the notes.
"""

# =============================================================================
# 0. WHY DO WE NEED SEARCHING AND SORTING?
# =============================================================================

"""
Imagine a platform stores information about millions of users.

If we search one-by-one from the first record to the last, the number of
checks can become very large. This is called LINEAR SEARCH.

If data is organised in sorted order, we can repeatedly inspect the middle
and discard half of the remaining search area. This is BINARY SEARCH.

For n elements:
    Linear search:   O(n)
    Binary search:   O(log n), BUT the data must have the required ordering.

Example:
    n = 800,000,000
    log2(n) is approximately 29.6, so binary search needs around 30
    comparisons in the ideal sorted-array model, whereas linear search
    can need up to 800 million comparisons.

Real websites also use databases, indexes, caches, distributed systems and
many other optimisations. The example is meant to explain the algorithmic
difference, not to claim that a large platform literally searches its entire
database with one simple binary-search call.

DSA = Data Structures + Algorithms.
A data structure organises data. An algorithm describes the steps used to
process that data.
"""

# =============================================================================
# 1. BASIC VOCABULARY YOU MUST KNOW
# =============================================================================

"""
ARRAY / LIST
------------
A collection of elements stored in an ordered sequence.

INDEX
-----
The position of an element. Python indexing starts at 0.

Example:
    nums = [3, 2, 8, 1]
    index:  0  1  2  3

LENGTH
------
len(nums) gives the number of elements. For the above list, len(nums) == 4.
The last valid index is len(nums) - 1, which is 3.

ITERATION
---------
Visiting elements one after another, commonly with a for loop.

COMPARISON
----------
For sorting in ascending order, compare adjacent or selected values to decide
which one should come first.

SWAP
----
Exchange two values:
    nums[i], nums[j] = nums[j], nums[i]

IN-PLACE
--------
An algorithm is called in-place when it rearranges the original collection
using only a small amount of auxiliary memory. Recursion stack usage is a
technical detail: some textbooks count it separately, so always state the
convention being used.

RECURSION
---------
A function calls itself on a smaller problem. Every recursive algorithm
needs a BASE CASE so that the calls eventually stop.

DIVIDE AND CONQUER
------------------
1. Divide a large problem into smaller parts.
2. Solve the smaller parts.
3. Combine their answers.
Merge sort is the classic example.
"""

# =============================================================================
# 2. BUBBLE SORT
# =============================================================================

"""
IDEA
----
Compare neighbouring elements. If they are in the wrong order, swap them.

For ascending order:
    if nums[j] > nums[j + 1]:
        swap them

After one complete pass, the largest unsorted value reaches the end.
After the second pass, the second-largest reaches its final position, and so on.

Example:
    Start:       [3, 2, 8, 1, 7, 6, 4]
    After pass1: [2, 3, 1, 7, 6, 4, 8]
The largest value, 8, has bubbled to the last position.

WHY DOES THE INNER LOOP SHRINK?
-------------------------------
After each pass, the rightmost part is already sorted. There is no need to
compare those fixed elements again.

For pass i, compare j from 0 through n-i-2.
In Python this is:
    for j in range(n - i - 1)

EARLY-STOP OPTIMISATION
-----------------------
If a complete pass performs no swap, the list is already sorted. Stop early.

COMPLEXITY
----------
Best case with early-stop flag: O(n) — already sorted input.
Average case:                  O(n^2)
Worst case:                    O(n^2)
Auxiliary space:               O(1)
Stable:                        Yes, if equal values are not swapped.
Adaptive:                      Yes, with early-stop optimisation.
In-place:                      Yes.
"""


def bubble_sort(nums):
    """Sort nums in ascending order in-place and return the same list."""
    n = len(nums)

    for i in range(n):
        swapped = False

        # The last i elements are already in their correct positions.
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        # No swap means the whole list is sorted.
        if not swapped:
            break

    return nums


# =============================================================================
# 3. INSERTION SORT
# =============================================================================

"""
IDEA
----
Think of arranging playing cards in your hand.

Maintain a sorted prefix on the left. Take the next element (the KEY), move
larger elements one position to the right, and insert the key in the empty
position.

Example:
    [3, 2, 8, 1]
    Sorted prefix initially: [3]
    Insert 2:                [2, 3, 8, 1]
    Insert 8:                [2, 3, 8, 1]
    Insert 1:                [1, 2, 3, 8]

IMPORTANT VARIABLES
-------------------
i   = index of the element currently being inserted.
key = value that must be placed in the sorted prefix.
j   = scans backwards through the already-sorted prefix.

WHY STORE key?
--------------
When we shift nums[j] to nums[j+1], the original value at nums[i] could be
overwritten. Saving it in key prevents losing it.

WHY j >= 0?
-----------
Python lists have negative indexes. If j becomes -1, nums[-1] means the last
element, not an invalid position. Therefore we must explicitly check j >= 0.

COMPLEXITY
----------
Best case:       O(n) — already sorted; inner while loop does not shift.
Average case:    O(n^2)
Worst case:      O(n^2) — reverse-sorted input.
Auxiliary space: O(1)
Stable:          Yes, with the strict comparison nums[j] > key.
Adaptive:        Yes.
In-place:        Yes.
"""


def insertion_sort(nums):
    """Sort nums in ascending order in-place and return the same list."""
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]  # shift larger value one position right
            j -= 1

        nums[j + 1] = key

    return nums


# =============================================================================
# 4. SELECTION SORT
# =============================================================================

"""
IDEA
----
Select the minimum value from the unsorted part and put it at the beginning
of that unsorted part.

For each i:
    1. Assume i contains the minimum.
    2. Scan j from i+1 to the end.
    3. Remember the index of the smallest value.
    4. Swap that value with nums[i].

Example:
    [3, 2, 8, 1]
    Minimum of whole list is 1 -> swap with index 0: [1, 2, 8, 3]
    Minimum of remaining part is 2 -> already correct
    Minimum of remaining part is 3 -> [1, 2, 3, 8]

WHY TRACK min_index?
--------------------
We need the POSITION of the smallest element so that we can swap it into place.
Tracking only the minimum value is not enough for an in-place swap.

COMPLEXITY
----------
Best, average and worst: O(n^2)
Auxiliary space:         O(1)
Usually not stable:      A distant swap can change the order of equal values.
Adaptive:                No — it still scans the remaining list.
In-place:                Yes.

Note: Selection sort makes at most n-1 swaps, which can be useful when writes
are expensive. Its comparisons are still quadratic.
"""


def selection_sort(nums):
    """Sort nums in ascending order in-place and return the same list."""
    n = len(nums)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums


# =============================================================================
# 5. MERGE SORT
# =============================================================================

"""
IDEA: DIVIDE AND CONQUER
-----------------------
Merge sort repeatedly divides the list into halves until each part contains
one element. A one-element list is already sorted.

Then it merges sorted parts:
    [5] + [1] -> [1, 5]
    [6] + [2] -> [2, 6]
    [4] remains [4]
    [1, 5] + [2, 6] -> [1, 2, 5, 6]
    [1, 2, 5, 6] + [4] -> [1, 2, 4, 5, 6]

The original list is not conceptually split into unrelated lists during the
recursive calls in the index-based implementation. The calls work on ranges
L..R of the same list. Temporary lists are used during merging.

RECURSION TERMS
---------------
L = left/start index of the current range.
R = right/end index of the current range.
mid = midpoint.

Base case:
    if L >= R:
        return

Recursive calls:
    sort L..mid
    sort mid+1..R
    merge the two sorted ranges

HOW MERGING WORKS
-----------------
Suppose the left half is [1, 5, 6] and right half is [2, 3, 4].

Use pointers i and j:
    Compare left[i] and right[j].
    Copy the smaller one into the result.
    Advance the pointer from which the value was copied.
When one half ends, copy the remaining values from the other half.

COMPLEXITY
----------
Best, average and worst: O(n log n)
Auxiliary space:         O(n) for the temporary merge storage.
Stable:                  Yes, if equal values are taken from the left half first.
Adaptive:                Generally no in this standard implementation.
In-place:                No in this standard implementation.
"""


def merge_sort(nums):
    """Return a NEW sorted list using merge sort. Original list is unchanged."""
    if len(nums) <= 1:
        return nums[:]

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge_two_sorted_lists(left, right)


def merge_two_sorted_lists(left, right):
    """Merge two already-sorted lists into a new sorted list."""
    i = 0
    j = 0
    merged = []

    while i < len(left) and j < len(right):
        # <= preserves the original relative order of equal values.
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # At most one of these loops will append remaining elements.
    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


def merge_sort_in_place(nums, left=0, right=None):
    """
    Index-based merge sort that writes the answer back into nums.
    It still uses temporary lists during merging, so auxiliary space is O(n).
    """
    if right is None:
        right = len(nums) - 1

    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort_in_place(nums, left, mid)
    merge_sort_in_place(nums, mid + 1, right)

    left_part = nums[left:mid + 1]
    right_part = nums[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            nums[k] = left_part[i]
            i += 1
        else:
            nums[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        nums[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        nums[k] = right_part[j]
        j += 1
        k += 1


# =============================================================================
# 6. QUICK SORT
# =============================================================================

"""
IDEA
----
Quick sort also uses divide and conquer, but it works by PARTITIONING.

A pivot is selected. In the implementation below, the last element is the
pivot.

After partitioning:
    - values <= pivot are placed to its left
    - values > pivot are placed to its right
    - pivot is placed at its final sorted position

Then quick sort recursively sorts the left and right parts, excluding pivot.

PARTITION POINTERS
------------------
pivot = nums[right]
i = boundary for the next value that belongs on the left.
j = scans the current range.

Whenever nums[j] <= pivot:
    swap nums[i] and nums[j]
    move i forward

At the end:
    swap nums[i] with pivot
    return i (the pivot's final index)

COMPLEXITY
----------
Best case:       O(n log n)
Average case:    O(n log n)
Worst case:      O(n^2), e.g. consistently poor pivots on already ordered data
Auxiliary space: O(log n) average recursion stack; O(n) worst-case stack.
Stable:          Usually no.
Adaptive:        No, in the standard implementation.
In-place:        Partitioning is in-place, but recursion uses stack space.
"""


def _partition(nums, low, high):
    """Partition nums[low:high+1] around the last element; return pivot index."""
    pivot = nums[high]
    i = low

    for j in range(low, high):
        if nums[j] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[i], nums[high] = nums[high], nums[i]
    return i


def quick_sort(nums):
    """Sort nums in-place using quick sort and return the same list."""
    def _quick_sort(low, high):
        if low >= high:
            return

        pivot_index = _partition(nums, low, high)
        _quick_sort(low, pivot_index - 1)
        _quick_sort(pivot_index + 1, high)

    _quick_sort(0, len(nums) - 1)
    return nums


# =============================================================================
# 7. COUNTING SORT
# =============================================================================

"""
WHEN TO USE IT
--------------
Counting sort is useful when values are integers in a reasonably small,
known range. It counts how many times each value occurs instead of comparing
every pair of values.

Example:
    nums = [2, 1, 0, 2, 3, 1, 0]
    frequency[0] = 2
    frequency[1] = 2
    frequency[2] = 2
    frequency[3] = 1

Rebuild:
    [0, 0, 1, 1, 2, 2, 3]

If the values are 0..maximum:
    frequency list length = maximum + 1
    value itself is used as the frequency-list index.

COMPLEXITY
----------
Let n = number of input elements and k = range of possible values.
Time:  O(n + k)
Space: O(k) for the simple frequency implementation.

The transcript informally describes its cost in terms of the maximum value.
The more precise expression is O(n + k), where k is the size of the value
range. If values range from a very small minimum to a huge maximum, counting
sort may be inefficient. Negative values require an offset or a different
implementation.
"""


def counting_sort_non_negative(nums):
    """Return a sorted copy. Supports non-negative integers only."""
    if not nums:
        return []

    if any(not isinstance(x, int) or x < 0 for x in nums):
        raise ValueError("This simple counting sort accepts non-negative integers only.")

    maximum = max(nums)
    frequency = [0] * (maximum + 1)

    for value in nums:
        frequency[value] += 1

    result = []
    for value, count in enumerate(frequency):
        result.extend([value] * count)

    return result


def counting_sort_integers(nums):
    """Counting sort that also supports negative integers."""
    if not nums:
        return []

    minimum = min(nums)
    maximum = max(nums)
    frequency = [0] * (maximum - minimum + 1)

    for value in nums:
        frequency[value - minimum] += 1

    result = []
    for index, count in enumerate(frequency):
        result.extend([index + minimum] * count)

    return result


# =============================================================================
# 8. COMPARISON OF THE SIX SORTING ALGORITHMS
# =============================================================================

"""
Algorithm       Best             Average          Worst           Extra space
----------------------------------------------------------------------------
Bubble          O(n)*            O(n^2)            O(n^2)          O(1)
Insertion       O(n)             O(n^2)            O(n^2)          O(1)
Selection       O(n^2)           O(n^2)            O(n^2)          O(1)
Merge           O(n log n)       O(n log n)        O(n log n)      O(n)
Quick           O(n log n)       O(n log n)        O(n^2)          O(log n) avg
Counting        O(n+k)           O(n+k)            O(n+k)          O(k)

*Bubble sort's O(n) best case requires the early-stop flag.

STABLE SORT
-----------
If two records have equal sorting keys, a stable algorithm preserves their
original relative order.

Example records:
    [("A", 5), ("B", 2), ("C", 5)]

Sort by the numeric value:
    stable result: [("B", 2), ("A", 5), ("C", 5)]
A remains before C because A was before C originally.

ADAPTIVE SORT
-------------
An adaptive algorithm can do less work when input is already sorted or nearly
sorted. Insertion sort and optimised bubble sort are adaptive.

IN-PLACE SORT
-------------
An in-place algorithm rearranges the input using O(1) auxiliary data space
under the usual simplified definition. Bubble, insertion and selection sort
are in-place. Quick sort's partition is in-place, but its recursion stack
takes space. Merge sort uses O(n) temporary storage. Counting sort uses
additional frequency storage.

Important correction:
Stability, adaptiveness and in-place behaviour are properties of a specific
implementation, not just the algorithm's name. State the implementation
assumption in exam answers.
"""

# =============================================================================
# 9. SORT COLORS — SORT 0, 1 AND 2 (DUTCH NATIONAL FLAG)
# =============================================================================

"""
PROBLEM
-------
The list contains only 0, 1 and 2. Rearrange it so that all 0s come first,
then 1s, then 2s.

The video demonstrates a three-pointer method rather than simply using
counting sort.

POINTERS
--------
low  = next position where a 0 should go.
mid  = current element being examined.
high = next position where a 2 should go.

RULES
-----
If nums[mid] == 0:
    swap nums[low] and nums[mid]
    low += 1
    mid += 1

If nums[mid] == 1:
    mid += 1

If nums[mid] == 2:
    swap nums[mid] and nums[high]
    high -= 1
    DO NOT increment mid, because the value swapped from the right has
    not been examined yet.

The loop ends when mid > high.

Complexity: O(n) time, O(1) extra space.
"""


def sort_colors(nums):
    """Rearrange 0s, 1s, 2s in-place; return nums."""
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            # Do not move mid here.

    return nums


# =============================================================================
# 10. MERGE TWO SORTED ARRAYS IN-PLACE FROM THE BACK
# =============================================================================

"""
PROBLEM
-------
nums1 contains m valid sorted values followed by enough empty/placeholder
space to hold nums2. nums2 contains n sorted values.

Example:
    nums1 = [1, 2, 3, 0, 0, 0], m = 3
    nums2 = [2, 5, 6],           n = 3

Required:
    nums1 becomes [1, 2, 2, 3, 5, 6]

WHY START FROM THE BACK?
------------------------
If we start at the front, writing a small value into nums1 may overwrite a
value that we have not processed yet.

The end of nums1 has empty capacity. Put the largest remaining value there.

THREE POINTERS
--------------
i = m - 1       last valid element in nums1
j = n - 1       last element in nums2
k = m + n - 1   last available position in nums1

While j >= 0:
    compare nums1[i] and nums2[j]
    place the larger one at nums1[k]
    move the pointer used and move k left

Why only loop while j >= 0?
If nums1's remaining elements are already in place, no work is needed.
But every element of nums2 must be copied into nums1.

Complexity: O(m+n) time, O(1) extra space.
"""


def merge_into_first(nums1, m, nums2, n):
    """Merge sorted nums2 into nums1, modifying nums1. Returns nums1."""
    i = m - 1
    j = n - 1
    k = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    return nums1


# =============================================================================
# 11. CUSTOM SORTING WITH A KEY / LAMBDA — INTERVALS
# =============================================================================

"""
Python's sort() and sorted() accept a key function.

Example:
    intervals = [[3, 5], [1, 2], [2, 4]]
    intervals.sort(key=lambda interval: interval[0])

The lambda expression returns the first value of each interval. Therefore
sorting is performed by each interval's starting point.

NON-OVERLAPPING INTERVALS / MINIMUM REMOVALS
--------------------------------------------
A common problem:
    Given intervals, remove the minimum number so that the remaining
    intervals do not overlap.

Greedy approach:
    1. Sort by interval end time.
    2. Keep the interval that ends earliest.
    3. For each next interval:
       - if its start >= end of the last kept interval, keep it;
       - otherwise it overlaps, so remove it.
    4. Count removals.

Why sort by end?
Choosing the interval that finishes earliest leaves as much room as possible
for later intervals.

For intervals that merely touch at an endpoint, this implementation treats
[start, end] and [end, next_end] as non-overlapping, using start >= last_end.
This matches the usual interval scheduling convention for this problem.
"""


def minimum_interval_removals(intervals):
    """Return minimum number of intervals to remove to eliminate overlap."""
    if not intervals:
        return 0

    ordered = sorted(intervals, key=lambda interval: interval[1])
    kept_end = ordered[0][1]
    removals = 0

    for start, end in ordered[1:]:
        if start >= kept_end:
            kept_end = end
        else:
            removals += 1

    return removals


# =============================================================================
# 12. LINEAR SEARCH
# =============================================================================

"""
IDEA
----
Check every element from left to right until the target is found.

Algorithm:
    for i from 0 to n-1:
        if nums[i] == target:
            return i
    return -1

- Returns the first matching index.
- Returns -1 if the target is absent.
- Works on sorted and unsorted lists.
- Best case O(1), worst/average O(n), extra space O(1).

A linear scan is appropriate when the collection is small, unsorted, or only
one search is needed and sorting/index construction would cost more.
"""


def linear_search(nums, target):
    """Return first index of target, or -1 if absent."""
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


# =============================================================================
# 13. BINARY SEARCH
# =============================================================================

"""
REQUIREMENT
-----------
The list must be sorted in the order assumed by the algorithm. This standard
implementation expects ascending order.

IDEA
----
1. Set left = 0 and right = n-1.
2. Find middle.
3. If nums[mid] == target, return mid.
4. If target < nums[mid], discard the right half: right = mid-1.
5. If target > nums[mid], discard the left half: left = mid+1.
6. If left > right, target is absent; return -1.

WHY IS IT FAST?
---------------
Each comparison removes roughly half of the remaining search range:
    n -> n/2 -> n/4 -> n/8 -> ... -> 1

The number of halvings is log2(n), so time complexity is O(log n).
Space complexity of this iterative version is O(1).

COMMON MISTAKES
---------------
- Applying binary search to an unsorted list.
- Using while left < right when the chosen boundary logic needs <=.
- Forgetting mid-1 or mid+1, causing an infinite loop.
- Returning the value instead of the required index.
- Using the wrong comparison direction.
"""


def binary_search(nums, target):
    """Return any index of target in ascending sorted nums, else -1."""
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# =============================================================================
# 14. SEARCH INSERT POSITION, LOWER BOUND AND UPPER BOUND
# =============================================================================

"""
SEARCH INSERT POSITION
----------------------
Given an ascending sorted list and a target:
- If target exists, return its index.
- Otherwise, return the index where it should be inserted to keep the list
  sorted.

This is exactly the LOWER BOUND index.

LOWER BOUND
-----------
Index of the first element >= target.
If no such element exists, return len(nums).

Examples for nums = [2, 5, 8, 12, 20, 23, 40]:
    lower_bound(12) = 3   (12 itself is present)
    lower_bound(5)  = 1
    lower_bound(6)  = 2   (first value >= 6 is 8)
    lower_bound(50) = 7   (insert after the last element)

UPPER BOUND
-----------
Index of the first element > target.
If no such element exists, return len(nums).

Examples:
    upper_bound(12) = 4   (first value strictly greater is 20)
    upper_bound(6)  = 2
    upper_bound(50) = 7

THE ONLY LOGIC DIFFERENCE
-------------------------
Lower bound:
    if nums[mid] >= target:
        answer = mid
        search left

Upper bound:
    if nums[mid] > target:
        answer = mid
        search left

Otherwise search right.

The answer variable starts at len(nums), which handles targets larger than
every element.
"""


def lower_bound(nums, target):
    """Return first index i where nums[i] >= target; else len(nums)."""
    left = 0
    right = len(nums)  # half-open interval [left, right)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left


def upper_bound(nums, target):
    """Return first index i where nums[i] > target; else len(nums)."""
    left = 0
    right = len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left


def search_insert_position(nums, target):
    """Search Insert Position is the lower-bound index."""
    return lower_bound(nums, target)


# =============================================================================
# 15. FIRST AND LAST POSITION OF A TARGET IN A SORTED ARRAY
# =============================================================================

"""
PROBLEM
-------
The list is sorted and may contain duplicates. Find the first and last index
of target.

Use:
    first = lower_bound(nums, target)
    after_last = upper_bound(nums, target)

If first == after_last, target does not exist -> [-1, -1].
Otherwise:
    first occurrence = first
    last occurrence  = after_last - 1

Example:
    nums = [1, 2, 5, 5, 5, 8, 9]
    target = 5
    lower_bound = 2
    upper_bound = 5
    answer = [2, 4]

Both searches are O(log n), so total time is O(log n).
"""


def first_last_position(nums, target):
    """Return [first_index, last_index], or [-1, -1] if target is absent."""
    first = lower_bound(nums, target)
    after_last = upper_bound(nums, target)

    if first == after_last:
        return [-1, -1]

    return [first, after_last - 1]


# =============================================================================
# 16. BINARY SEARCH ON A MOUNTAIN ARRAY — FIND THE PEAK
# =============================================================================

"""
MOUNTAIN ARRAY
--------------
Values first increase, reach a peak, and then decrease.

Example:
    [2, 5, 9, 12, 7, 6, 1]
               ^
             peak

At a middle index:
    If nums[mid] < nums[mid+1], we are on the increasing slope.
    The peak must be to the right, so left = mid+1.

    Otherwise, we are on the decreasing slope or at the peak.
    The peak is at mid or to the left, so right = mid.

Stop when left == right. That index is the peak.

This version assumes a valid mountain array with a single peak and no
ambiguous plateau. It uses O(log n) time and O(1) extra space.
"""


def mountain_peak_index(nums):
    """Return peak index in a valid mountain array."""
    if len(nums) < 3:
        raise ValueError("A mountain array must contain at least 3 elements.")

    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


# =============================================================================
# 17. BINARY SEARCH ON THE ANSWER — KOKO / BANANA-EATING SPEED
# =============================================================================

"""
PROBLEM MODEL
-------------
There are piles of bananas. A worker eats at speed k bananas per hour.
For a pile of size p, the time required is ceil(p/k) hours.
Only one pile is worked on at a time. Given H hours, find the minimum integer
speed k that finishes all piles within H hours.

Example:
    piles = [3, 6, 7, 11]
    H = 8

For k = 4:
    ceil(3/4)  = 1 hour
    ceil(6/4)  = 2 hours
    ceil(7/4)  = 2 hours
    ceil(11/4) = 3 hours
    total = 8 hours, so k=4 works.

For k=3:
    1 + 2 + 3 + 4 = 10 hours, so k=3 does not work.

Answer is the minimum speed that works.

WHY BINARY SEARCH?
------------------
We are not searching an array element. We are searching a possible ANSWER.

Feasibility is monotonic:
    If speed k works, every speed greater than k also works.
    If speed k does not work, every smaller speed also does not work.

Search range:
    left = 1
    right = max(piles)

For a candidate speed:
    hours = sum((pile + speed - 1) // speed for pile in piles)

The expression (pile + speed - 1) // speed computes ceiling division for
positive integers. It is equivalent to math.ceil(pile / speed), without
floating-point arithmetic.

If hours <= H:
    speed works; save it and try a smaller speed.
Otherwise:
    speed is too slow; increase it.

Complexity:
    O(n log M) time, where M = max(piles).
    O(1) extra space.
"""


def minimum_eating_speed(piles, hours_available):
    """Return minimum integer speed to finish all piles within given hours."""
    if not piles:
        return 0
    if hours_available < len(piles):
        raise ValueError("Impossible: at least one hour is needed per non-empty pile.")

    left = 1
    right = max(piles)
    answer = right

    while left <= right:
        speed = (left + right) // 2

        hours_needed = 0
        for pile in piles:
            hours_needed += (pile + speed - 1) // speed

        if hours_needed <= hours_available:
            answer = speed
            right = speed - 1  # works; try to find a smaller speed
        else:
            left = speed + 1   # too slow; increase speed

    return answer


# =============================================================================
# 18. BINARY SEARCH IN A ROW-MAJOR SORTED 2D MATRIX
# =============================================================================

"""
MATRIX CONDITION
----------------
This method requires the matrix to be sorted as if all rows were joined into
one long ascending list. In other words:
    - every row is sorted;
    - the first element of each row is greater than the last element of the
      previous row.

Example:
    [
        [ 1,  3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]

Treat it as a virtual one-dimensional array of 12 values:
    virtual index: 0 1 2 3 4 5 6 7 8 9 10 11

Convert virtual index mid to matrix coordinates:
    row = mid // number_of_columns
    col = mid % number_of_columns

Why?
    Each full row occupies number_of_columns positions.
    Integer division tells how many full rows have passed.
    Modulo tells the position inside the current row.

Search range:
    left = 0
    right = rows * columns - 1

At each step:
    value = matrix[mid // columns][mid % columns]

Compare value with target exactly like normal binary search.

Complexity:
    O(log(rows * columns)) time, O(1) extra space.

Important distinction:
A matrix where each row is individually sorted but the rows do not form one
globally sorted row-major sequence does NOT satisfy this exact method's
condition. Other matrix-search patterns may be needed.
"""


def search_sorted_matrix(matrix, target):
    """Return True if target exists in a row-major sorted rectangular matrix."""
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    left = 0
    right = rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // cols
        col = mid % cols
        value = matrix[row][col]

        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# =============================================================================
# 19. SORT ARRAY BY PARITY — EVEN VALUES FIRST
# =============================================================================

"""
PROBLEM
-------
Move all even numbers to the beginning and all odd numbers to the end.
The relative order does not need to be preserved.

Two approaches:
1. Extra list: collect evens, then odds. O(n) extra space.
2. In-place two-pointer/partition approach.

The transcript's approach uses:
    start = next position for an even number
    i = scan index

If nums[i] is even:
    swap nums[start] and nums[i]
    start += 1

For odd values, just continue.

This is O(n) time and O(1) extra space. It is not stable: relative order
within the even or odd groups may change.
"""


def sort_array_by_parity(nums):
    """Move evens before odds in-place; return nums."""
    start = 0

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[start], nums[i] = nums[i], nums[start]
            start += 1

    return nums


# =============================================================================
# 20. HOW TO DRY-RUN ANY SORTING OR SEARCHING CODE
# =============================================================================

"""
Use a table on paper. Do not try to hold every pointer in your head.

BUBBLE SORT DRY RUN
-------------------
Write columns:
    pass | i | j | nums[j] | nums[j+1] | swap? | array after operation

INSERTION SORT DRY RUN
----------------------
Write:
    i | key | j | comparison | shift / insert | array

SELECTION SORT DRY RUN
----------------------
Write:
    i | current min_index | j | new minimum? | array after swap

MERGE SORT DRY RUN
------------------
Draw the recursion tree:
    original range
      /          \\
    left        right
    / \\          / \\
  ... ...      ... ...
Then draw the merge steps from one-element ranges upwards.

QUICK SORT DRY RUN
------------------
For each partition, write:
    pivot | i | j | swap? | array | final pivot index
Then draw the two recursive ranges excluding the pivot.

BINARY SEARCH DRY RUN
---------------------
Write:
    left | right | mid | nums[mid] | comparison | updated boundary

LOWER / UPPER BOUND DRY RUN
---------------------------
Also maintain:
    answer
When a valid candidate is found, save mid and continue searching left.

GENERAL LOOP CHECKLIST
----------------------
1. What is the loop's starting value?
2. What is the stopping condition?
3. Which variable changes each iteration?
4. Does every branch move a pointer or change state?
5. Can an index become -1 or len(nums)?
6. Are you accidentally skipping a value after swapping?
7. What happens for an empty list or one-element list?
8. What should be returned when the target is absent?
"""

# =============================================================================
# 21. RUNNABLE DEMONSTRATIONS
# =============================================================================


def run_demos():
    print("\n" + "=" * 65)
    print("SEARCHING AND SORTING — EXECUTABLE DEMONSTRATIONS")
    print("=" * 65)

    sample = [3, 2, 8, 1, 7, 6, 4]
    print("\nOriginal list:", sample)
    print("Bubble sort:  ", bubble_sort(sample.copy()))
    print("Insertion:    ", insertion_sort(sample.copy()))
    print("Selection:    ", selection_sort(sample.copy()))
    print("Merge sort:   ", merge_sort(sample.copy()))
    print("Quick sort:   ", quick_sort(sample.copy()))
    print("Counting sort:", counting_sort_non_negative(sample))

    print("\nSort Colors:")
    colors = [2, 0, 2, 1, 1, 0]
    print("Before:", colors)
    print("After: ", sort_colors(colors.copy()))

    print("\nMerge two sorted arrays in-place:")
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    print("Before:", nums1, "+", nums2)
    print("After: ", merge_into_first(nums1, 3, nums2, 3))

    print("\nInterval removals:")
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print("Intervals:", intervals)
    print("Minimum removals:", minimum_interval_removals(intervals))

    print("\nLinear and binary search:")
    values = [2, 5, 8, 12, 20, 23, 40]
    print("Linear search for 20:", linear_search(values, 20))
    print("Binary search for 20:", binary_search(values, 20))
    print("Binary search for 99:", binary_search(values, 99))

    print("\nLower and upper bounds:")
    print("values:", values)
    for target in [5, 6, 12, 50]:
        print(
            f"target={target:>2} | lower={lower_bound(values, target)}"
            f" | upper={upper_bound(values, target)}"
            f" | insert={search_insert_position(values, target)}"
        )

    print("\nFirst and last occurrence:")
    duplicates = [1, 2, 5, 5, 5, 8, 9]
    print("Array:", duplicates)
    print("Target 5:", first_last_position(duplicates, 5))
    print("Target 4:", first_last_position(duplicates, 4))

    print("\nMountain peak:")
    mountain = [2, 5, 9, 12, 7, 6, 1]
    peak_index = mountain_peak_index(mountain)
    print("Array:", mountain)
    print("Peak index:", peak_index, "| Peak value:", mountain[peak_index])

    print("\nBinary search on answer — banana speed:")
    piles = [3, 6, 7, 11]
    h = 8
    print("Piles:", piles, "| Hours:", h)
    print("Minimum speed:", minimum_eating_speed(piles, h))

    print("\nBinary search on 2D matrix:")
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60],
    ]
    print("Find 34:", search_sorted_matrix(matrix, 34))
    print("Find 13:", search_sorted_matrix(matrix, 13))

    print("\nSort array by parity:")
    parity = [5, 4, 2, 7, 6, 9]
    print("Before:", parity)
    print("After: ", sort_array_by_parity(parity.copy()))


# =============================================================================
# 22. SELF-TESTS — RUN THESE TO CHECK YOUR UNDERSTANDING
# =============================================================================


def run_self_tests():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([]) == []
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]

    assert insertion_sort([3, 2, 1]) == [1, 2, 3]
    assert selection_sort([3, 2, 1]) == [1, 2, 3]
    assert merge_sort([3, 2, 1]) == [1, 2, 3]
    assert quick_sort([3, 2, 1]) == [1, 2, 3]

    assert counting_sort_non_negative([2, 1, 0, 2, 1]) == [0, 1, 1, 2, 2]
    assert counting_sort_integers([3, -2, 0, -2, 5]) == [-2, -2, 0, 3, 5]

    assert sort_colors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]

    a = [1, 2, 3, 0, 0, 0]
    assert merge_into_first(a, 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]

    assert minimum_interval_removals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1

    assert linear_search([4, 2, 9], 2) == 1
    assert linear_search([4, 2, 9], 7) == -1
    assert binary_search([2, 5, 8, 12, 20], 12) == 3
    assert binary_search([2, 5, 8, 12, 20], 7) == -1

    assert lower_bound([2, 5, 8, 12], 8) == 2
    assert lower_bound([2, 5, 8, 12], 7) == 2
    assert lower_bound([2, 5, 8, 12], 99) == 4
    assert upper_bound([2, 5, 8, 12], 8) == 3
    assert upper_bound([2, 5, 8, 12], 7) == 2
    assert first_last_position([1, 2, 5, 5, 5, 8], 5) == [2, 4]
    assert first_last_position([1, 2, 5, 5, 5, 8], 4) == [-1, -1]

    assert mountain_peak_index([2, 5, 9, 12, 7, 6, 1]) == 3
    assert minimum_eating_speed([3, 6, 7, 11], 8) == 4

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert search_sorted_matrix(matrix, 34) is True
    assert search_sorted_matrix(matrix, 13) is False

    parity_result = sort_array_by_parity([5, 4, 2, 7, 6, 9])
    first_odd = next((i for i, x in enumerate(parity_result) if x % 2), len(parity_result))
    assert all(x % 2 == 0 for x in parity_result[:first_odd])
    assert all(x % 2 == 1 for x in parity_result[first_odd:])

    print("\nAll self-tests passed.")


# =============================================================================
# 23. PRACTICE QUESTIONS
# =============================================================================

"""
Try these yourself before looking up a solution:

SORTING
-------
1. Dry-run bubble sort on [5, 1, 4, 2, 8].
2. Dry-run insertion sort on [7, 4, 5, 2].
3. Why does insertion sort need to save key?
4. Why does selection sort remain O(n^2) even when the list is sorted?
5. Explain merge sort's base case.
6. In quick sort, why is the pivot excluded from both recursive calls?
7. When is counting sort a poor choice?

SORTING PROBLEMS
----------------
8. Sort [2, 0, 1, 2, 1, 0] using sort_colors().
9. Merge [1, 4, 7, 0, 0, 0] with [2, 5, 6].
10. Find the minimum removals for [[1, 2], [1, 3], [2, 4], [3, 5]].
11. Move evens before odds in [9, 4, 7, 2, 6, 3].

SEARCHING
---------
12. Linear-search [10, 4, 7, 2] for 7.
13. Binary-search [1, 3, 5, 7, 9, 11] for 9.
14. Why must a normal binary-search input be sorted?
15. Find lower_bound and upper_bound of 5 in [1, 3, 5, 5, 5, 8].
16. Find first and last position of 5 in [1, 3, 5, 5, 5, 8].
17. Find the peak index in [1, 4, 8, 12, 10, 6, 2].
18. Find minimum eating speed for piles [30, 11, 23, 4, 20] in 6 hours.
19. Search for 16 in:
        [[1, 3, 5, 7],
         [10, 11, 16, 20],
         [23, 30, 34, 60]]

COMPLEXITY
----------
20. State best/average/worst time and extra space for each of the six sorts.
21. Which of the algorithms are stable in the implementations in this file?
22. Which are adaptive?
23. Which use extra memory proportional to input/range size?
24. Compare O(n), O(log n), O(n log n), and O(n^2) for large n.
"""

if __name__ == "__main__":
    run_demos()
    run_self_tests()
