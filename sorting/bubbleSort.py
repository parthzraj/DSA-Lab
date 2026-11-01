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