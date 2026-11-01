"""
PYTHON ARRAYS — COMPLETE BEGINNER NOTES + EXECUTABLE LAB
=======================================================

Based on the supplied video transcript: "Array in Python" (array module + NumPy).

HOW TO USE THIS FILE
--------------------
1. Save/run with Python 3:
       python python_arrays_complete_notes.py

2. Most examples run with Python's standard library only.
3. NumPy examples run if NumPy is installed:
       python -m pip install numpy
   Then run this file again. If NumPy is not installed, the NumPy section
   will be skipped without stopping the r
   
   est of the notes.

4. Read the explanations, then change the values and run the examples again.
   The file is intentionally written as a teaching script, not just a list
   of definitions.

IMPORTANT ACCURACY NOTES
------------------------
The video is an introductory explanation. A few statements need precision:
- Python's array.array is resizable, but it stores one compatible primitive
  data type. It is not the same thing as a normal Python list.
- Python lists are dynamic and can hold mixed types. They are often used for
  DSA exercises, even though they are not the same as low-level typed arrays.
- NumPy arrays normally have one dtype. If you mix integers and floats,
  NumPy commonly converts them to a common dtype. If you mix numbers and
  strings, it may convert all values to strings. Do not think of a normal
  NumPy ndarray as a list that preserves each item's independent type.
- array type-code sizes can depend on the platform and Python build. Check
  itemsize instead of memorising a universal byte size.
- A NumPy multidimensional array must have a regular rectangular shape for
  ordinary numeric arrays. Rows with different lengths are not a normal
  rectangular matrix.

The notes preserve the topics explained in the video and add clarifications
where a beginner could otherwise learn an incorrect rule.
"""

# ============================================================================
# PART 0 — WHAT IS AN ARRAY?
# ============================================================================

"""
An ARRAY is a way to store many related values under one variable name.

Imagine storing the roll numbers of 5 students.

Without a collection:
    roll1 = 11
    roll2 = 12
    roll3 = 13
    roll4 = 14
    roll5 = 15

With a collection:
    rolls = [11, 12, 13, 14, 15]

Why is the second way easier?
- One variable name represents the whole collection.
- A loop can process every value.
- We can access a particular value by its index.
- We can search, update, insert, delete, sort, and process values.

ARRAY TERMINOLOGY
-----------------
Element : one stored value, e.g. 30.
Index   : position number of an element.
Length  : number of elements.
Array   : the complete collection.

Python uses ZERO-BASED INDEXING:
    first element  -> index 0
    second element -> index 1
    third element  -> index 2

For:
    marks = [70, 80, 90, 95]

Index:     0   1   2   3
Value:    70  80  90  95

The last valid index is always:
    len(array) - 1

Trying to access index len(array) causes IndexError.
"""

# ============================================================================
# PART 1 — ARRAY, LIST, array MODULE, AND NUMPY: WHAT IS THE DIFFERENCE?
# ============================================================================

"""
Python offers several ways to store multiple values.

1. Python list
   - Built into Python; no import needed.
   - Resizable.
   - Can store mixed types.
   - Very commonly used for DSA in Python.

2. array.array (the standard-library array module)
   - Requires: import array
   - Resizable.
   - Stores values of one specified primitive type.
   - Useful when you want a compact typed array.
   - One-dimensional.

3. NumPy ndarray
   - Requires installing NumPy.
   - Designed for numerical/scientific computing.
   - Usually stores one common dtype.
   - Supports one, two, three, and higher dimensions.
   - Offers fast vectorised operations.

The video concentrates on array.array first and then NumPy.
For many coding-interview/DSA problems in Python, lists are also important.
"""

# Example: list can hold different types.
mixed_list = [10, 2.5, "hello", True]
print("\nPART 1 — Python list can contain mixed types:")
print(mixed_list)


# ============================================================================
# PART 2 — THE STANDARD-LIBRARY array MODULE
# ============================================================================

"""
To use array.array:
    import array

Creating an array:
    values = array.array('i', [10, 20, 30])

The first argument is a TYPE CODE.
The second argument is an iterable containing the initial values.

Common type codes:
    'b' : signed char
    'B' : unsigned char
    'i' : signed int
    'I' : unsigned int
    'l' : signed long
    'L' : unsigned long
    'f' : float
    'd' : double

Important:
- The exact item size is platform-dependent.
- Ask Python for the actual size using array.itemsize.
- 'u' was historically used for Unicode characters, but it is deprecated
  in modern Python versions. Prefer strings/lists for text.

The array module does not let you freely mix an integer, float, and string
in one typed array.
"""

import array

integer_array = array.array('i', [1, 2, 3, 4, 5, 6])
print("\nPART 2 — array.array creation:")
print("Array:", integer_array)
print("Values as a list:", integer_array.tolist())
print("Type code:", integer_array.typecode)
print("Bytes used by one item on this machine:", integer_array.itemsize)


# ============================================================================
# PART 3 — ACCESSING ELEMENTS AND INDEXING
# ============================================================================

numbers = array.array('i', [10, 20, 30, 40, 50])

print("\nPART 3 — Indexing:")
print("First element, index 0:", numbers[0])
print("Second element, index 1:", numbers[1])
print("Third element, index 2:", numbers[2])
print("Last element, index -1:", numbers[-1])
print("Second-last element, index -2:", numbers[-2])

# Update/overwrite an element:
numbers[2] = 300
print("After replacing index 2 with 300:", numbers)

"""
Positive index: starts from the left at 0.
Negative index: starts from the right at -1.

Examples:
    a[0]   -> first item
    a[1]   -> second item
    a[-1]  -> last item
    a[-2]  -> second-last item

Updating an existing position does not increase the array's length:
    a[2] = 300

This is OVERWRITING, not insertion.
"""


# ============================================================================
# PART 4 — TRAVERSING / PRINTING ALL ELEMENTS
# ============================================================================

values = array.array('i', [1, 2, 3, 4, 5, 6])

print("\nPART 4A — Print the whole array:")
print(values)

print("\nPART 4B — Classic index-based for loop:")
for i in range(0, len(values)):
    print("index =", i, "value =", values[i])

print("\nPART 4C — Print on one line using end:")
for i in range(len(values)):
    print(values[i], end=" ")
print()  # move to the next output line

print("\nPART 4D — Enhanced/for-each style loop:")
for value in values:
    print(value, end=", ")
print()

"""
range(start, stop) includes start but EXCLUDES stop.

For six elements:
    range(0, 6) gives 0, 1, 2, 3, 4, 5

Why not range(0, 5)?
Because 5 is excluded, so it would only give 0 through 4.

Avoid hardcoding the length:
    for i in range(0, 6):  # fragile

Prefer:
    for i in range(len(values)):  # adapts to current length

A for-each loop is simpler if you do not need the index:
    for value in values:
        print(value)

Use index-based traversal when you need to read or update a position.
Use for-each traversal when you only need each value.
"""


# ============================================================================
# PART 5 — len(), TYPE CODE, REVERSE
# ============================================================================

values = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

print("\nPART 5 — Length and type:")
print("Length:", len(values))
print("Type code:", values.typecode)
print("Item size in bytes:", values.itemsize)

print("Before reverse:", values)
result_of_reverse = values.reverse()
print("Return value of reverse():", result_of_reverse)
print("After reverse:", values)

"""
len(a) returns the number of elements.

a.typecode tells you which type code was used.
a.itemsize tells you how many bytes each item occupies on this machine.

a.reverse() reverses the same array IN PLACE.
It changes the original array and returns None.

Incorrect:
    print(a.reverse())  # prints None

Correct:
    a.reverse()
    print(a)
"""


# ============================================================================
# PART 6 — INSERT, APPEND, AND OVERWRITE
# ============================================================================

values = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

print("\nPART 6A — Insert at an index:")
values.insert(1, 50)
print(values)  # 50 is inserted at index 1; old elements shift right.

print("\nPART 6B — Append at the end:")
values.append(100)
print(values)

print("\nPART 6C — Overwrite an existing index:")
values[2] = 200
print(values)

"""
insert(index, value)
--------------------
Adds a new element at the specified index.
Existing elements from that index onward shift right.
No old element is removed.

Example:
    a = [1, 2, 3]
    a.insert(1, 50)
    result -> [1, 50, 2, 3]

append(value)
-------------
Adds one value at the END.

Example:
    a.append(100)

Overwrite
---------
Assign directly to an existing index:
    a[2] = 200

Overwrite replaces a value; it does not shift elements or change length.
"""


# ============================================================================
# PART 7 — COPYING AN ARRAY AND LIST COMPREHENSION
# ============================================================================

original = array.array('i', [1, 2, 3, 4, 5])

# A clear copy for array.array:
copied = array.array(original.typecode, original)

# A transformed copy: multiply every value by 2.
doubled = array.array(original.typecode, (x * 2 for x in original))

print("\nPART 7 — Copying:")
print("Original:", original)
print("Copied:", copied)
print("Doubled copy:", doubled)

"""
The video demonstrates the idea of iterating over an old array and using
the collected values to create a new array.

For a Python list, this is called a LIST COMPREHENSION:
    doubled_list = [x * 2 for x in original_list]

It means:
    1. Take each x from the old collection.
    2. Calculate x * 2.
    3. Put the result into a new collection.

For array.array, the result must retain a compatible type code:
    array.array('i', (x * 2 for x in original))

A copy is a separate collection. Changing one does not automatically change
the other.
"""


# ============================================================================
# PART 8 — DELETE: pop() AND remove()
# ============================================================================

values = array.array('i', [3, 6, 9, 12, 15, 18, 21, 24, 27])

print("\nPART 8A — pop(index):")
removed_value = values.pop(3)
print("Removed value at index 3:", removed_value)
print("Array after pop(3):", values)

print("\nPART 8B — pop() without index:")
last_value = values.pop()
print("Removed last value:", last_value)
print("Array after pop():", values)

print("\nPART 8C — remove(value):")
values.remove(15)
print("Array after remove(15):", values)

"""
pop(index)
----------
Removes and RETURNS the element at the given index.

    removed = a.pop(3)

pop() with no index
-------------------
Removes and returns the LAST element.

This resembles stack behaviour:
    LIFO = Last In, First Out

The last value added is the first value removed.

remove(value)
-------------
Searches for the given VALUE and removes its first occurrence.

    a.remove(15)

Difference:
    pop(3)    -> remove by index
    pop()     -> remove last item
    remove(15)-> remove by value

If the value is absent, remove() raises ValueError.
If an index is invalid, pop() raises IndexError.
"""


# ============================================================================
# PART 9 — SLICING
# ============================================================================

values = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

print("\nPART 9 — Slicing:")
print("Original:", values)
print("Index 2 to before index 5:", values[2:5])
print("From index 2 to before the last 3 items:", values[2:-3])
print("Reverse using slicing:", values[::-1])
print("First four items:", values[:4])
print("From index 4 to the end:", values[4:])

"""
Slicing syntax:
    collection[start : stop : step]

Rules:
- start is INCLUDED.
- stop is EXCLUDED.
- step tells Python how to move between positions.

Examples:
    a[2:5]   -> indexes 2, 3, 4
    a[:4]    -> beginning through index 3
    a[4:]    -> index 4 through the end
    a[2:-3]  -> index 2 through the item before the last 3
    a[::-1]  -> all items in reverse order

A slice creates a new collection; it does not delete those items from
the original array.
"""


# ============================================================================
# PART 10 — TAKING INPUT FROM THE USER
# ============================================================================

def input_integer_array():
    """
    Ask the user how many integers they want, then read that many integers.

    Example interaction:
        How many numbers? 3
        Enter next number: 10
        Enter next number: 20
        Enter next number: 30
        Result: array('i', [10, 20, 30])
    """
    count = int(input("How many numbers do you want to enter? "))
    user_values = array.array('i')

    for index in range(count):
        value = int(input(f"Enter number {index + 1}: "))
        user_values.append(value)

    print("You entered:", end=" ")
    for value in user_values:
        print(value, end=" ")
    print()
    return user_values


"""
Why append() is used here:
- At the start, the array is empty.
- We do not yet have an element at index 0, 1, 2, ...
- append() safely adds each new value to the end.
- The loop runs exactly count times.

input() returns text (a string).
int(input(...)) converts that text to an integer.

This interactive function is not automatically called when the file runs.
Call it yourself when you want to practise keyboard input:
    input_integer_array()
"""


# ============================================================================
# PART 11 — SEARCHING WITH index()
# ============================================================================

values = array.array('i', [10, 25, 45, 60, 90, 134])

print("\nPART 11 — Searching:")
target = 45
try:
    position = values.index(target)
    print(target, "found at index", position)
except ValueError:
    print(target, "is not present")

"""
a.index(value) returns the index of the FIRST matching value.

Example:
    a = array.array('i', [10, 25, 45, 60])
    a.index(45) -> 2

If the value is absent, array.index() raises ValueError.
It does not simply return -1.

Safe pattern:
    try:
        position = a.index(target)
    except ValueError:
        print("Not found")

This built-in search is convenient. In DSA, you should also learn to
implement linear search manually using a loop (see Part 16).
"""


# ============================================================================
# PART 12 — NUMPY: INSTALLATION AND IMPORT
# ============================================================================

"""
NumPy is a third-party Python package for numerical arrays.

Install it in the terminal:
    python -m pip install numpy

If you use a virtual environment, activate that environment first and install
NumPy inside it. The Python interpreter running your program must be the
same environment in which NumPy was installed.

Common import styles:
    import numpy
    numpy.array([1, 2, 3])

Standard alias:
    import numpy as np
    np.array([1, 2, 3])

The video also mentions:
    from numpy import *

That imports names directly, but it is generally better to use `import
numpy as np`: it makes it clear where functions such as array(), zeros(),
and linspace() come from, and avoids name collisions.
"""

try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError:
    np = None
    NUMPY_AVAILABLE = False
    print("\nNumPy is not installed. Install it with: python -m pip install numpy")


# ============================================================================
# PART 13 — NUMPY ARRAY CREATION, DTYPE, AND TYPE CONVERSION
# ============================================================================

if NUMPY_AVAILABLE:
    print("\nPART 13 — NumPy array creation:")
    a = np.array([1, 2, 3, 4])
    print("Array:", a)
    print("Data type:", a.dtype)
    print("Number of dimensions:", a.ndim)
    print("Shape:", a.shape)
    print("Number of elements:", a.size)

    # Explicit dtype:
    as_float = np.array([1, 2, 3, 4], dtype=float)
    print("Explicit float dtype:", as_float)

    # Mixed integers and floats are promoted to a common dtype:
    mixed_numbers = np.array([1, 2, 4.5])
    print("Mixed integer/float values:", mixed_numbers)
    print("Their common dtype:", mixed_numbers.dtype)

    # A string mixed with numbers usually causes a common string dtype:
    mixed_with_text = np.array([1, 2, 4.5, "A"])
    print("Mixed with text:", mixed_with_text)
    print("Dtype after promotion:", mixed_with_text.dtype)

"""
NumPy's dtype controls how values are represented in the array.

Examples:
    np.array([1, 2, 3])              # integer dtype
    np.array([1, 2, 3], dtype=float) # convert values to floats

Do not confuse:
- Python list: can preserve different Python object types.
- NumPy ndarray: normally stores a single dtype efficiently.

When values are mixed, NumPy chooses a common dtype where possible.
For example, integer + float commonly becomes float.
Adding a string may cause values to become strings.
"""


# ============================================================================
# PART 14 — NUMPY linspace(), arange(), logspace()
# ============================================================================

if NUMPY_AVAILABLE:
    print("\nPART 14A — linspace:")
    line = np.linspace(10, 20, 5)
    print(line)

    print("\nPART 14B — arange:")
    sequence = np.arange(10, 20, 2)
    print(sequence)

    print("\nPART 14C — logspace:")
    logarithmic = np.logspace(1, 3, 4)
    print(logarithmic)

"""
np.linspace(start, stop, num)
-----------------------------
Creates `num` evenly spaced values from start to stop.
Both endpoints are included by default.

Example:
    np.linspace(10, 20, 5)
    -> [10.0, 12.5, 15.0, 17.5, 20.0]

The third argument is the NUMBER OF VALUES, not the step size.

np.arange(start, stop, step)
----------------------------
Creates values separated by a fixed step.
The stop value is EXCLUDED.

Example:
    np.arange(10, 20, 2)
    -> [10, 12, 14, 16, 18]

The third argument is the STEP SIZE.

Remember the difference:
    linspace(10, 20, 5) -> 5 evenly spaced values, includes 20
    arange(10, 20, 2)   -> step by 2, excludes 20

Floating-point arange steps can sometimes produce precision surprises.
For a fixed number of evenly spaced points, linspace is often preferable.

np.logspace(start, stop, num)
-----------------------------
Creates values evenly spaced on a logarithmic scale.
By default, values are powers of 10:
    np.logspace(1, 3, 4)
    -> approximately [10, 100, 1000] with four log-spaced values.
"""


# ============================================================================
# PART 15 — NUMPY zeros(), ones(), full()
# ============================================================================

if NUMPY_AVAILABLE:
    print("\nPART 15 — Initialised arrays:")
    zero_array = np.zeros(10)
    one_array = np.ones(10)
    five_array = np.full(10, 5)

    print("Ten zeros:", zero_array)
    print("Ten ones:", one_array)
    print("Ten fives:", five_array)

"""
np.zeros(shape)
---------------
Creates an array filled with zeros.

np.ones(shape)
--------------
Creates an array filled with ones.

np.full(shape, value)
---------------------
Creates an array filled with a chosen value.

Examples:
    np.zeros(10)       # 10 zeros
    np.ones(10)        # 10 ones
    np.full(10, 5)     # 10 fives

Shape can also be multidimensional:
    np.zeros((2, 3))   # 2 rows, 3 columns
"""


# ============================================================================
# PART 16 — NUMPY DIMENSIONS: 0D, 1D, 2D, 3D
# ============================================================================

if NUMPY_AVAILABLE:
    print("\nPART 16 — Dimensions:")

    zero_d = np.array(10)
    one_d = np.array([1, 2, 3, 4, 5])
    two_d = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    three_d = np.array([
        [
            [1, 2],
            [3, 4]
        ],
        [
            [5, 6],
            [7, 8]
        ]
    ])

    for name, item in [
        ("0D", zero_d),
        ("1D", one_d),
        ("2D", two_d),
        ("3D", three_d),
    ]:
        print(name, "array:")
        print(item)
        print("ndim =", item.ndim, "| shape =", item.shape)
        print()

"""
0D ARRAY — scalar
-----------------
A single value:
    np.array(10)

1D ARRAY — a sequence
---------------------
A single row/line of values:
    np.array([1, 2, 3, 4])

2D ARRAY — rows and columns
---------------------------
A collection of 1D rows:
    np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

This has shape (2, 3):
- 2 rows
- 3 columns

3D ARRAY — a collection of 2D arrays
------------------------------------
Think of it as multiple tables/layers:
    np.array([
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
    ])

This has shape (2, 2, 2):
- 2 blocks
- 2 rows in each block
- 2 columns in each row

Useful attributes:
    a.ndim  -> number of dimensions
    a.shape -> size along each dimension
    a.size  -> total number of elements
    a.dtype -> data type

For a normal rectangular numeric NumPy array, each row must have a
consistent number of elements. Ragged/nested lists with unequal row lengths
do not form a regular numeric matrix.
"""


# ============================================================================
# PART 17 — NUMPY INDEXING, SLICING, AND VECTORISED OPERATIONS
# ============================================================================

if NUMPY_AVAILABLE:
    print("\nPART 17 — NumPy indexing and operations:")
    n = np.array([10, 20, 30, 40, 50])
    print("First:", n[0])
    print("Last:", n[-1])
    print("Slice [1:4]:", n[1:4])
    print("Reverse:", n[::-1])
    print("Every value multiplied by 2:", n * 2)
    print("Add 5 to every value:", n + 5)

    matrix = np.array([
        [10, 20, 30],
        [40, 50, 60]
    ])
    print("Matrix element at row 1, column 2:", matrix[1, 2])
    print("First row:", matrix[0])
    print("Second column:", matrix[:, 1])

"""
NumPy supports the same basic indexing idea:
    a[0]
    a[-1]
    a[1:4]

For 2D arrays:
    matrix[row_index, column_index]

Example:
    matrix[1, 2] -> row 1, column 2 (the value 60 in the example)

Colon means select a range/all positions:
    matrix[:, 1] -> all rows, column 1

Vectorised operations:
    a * 2
    a + 5

These perform the operation on every element without writing a Python loop.
This is one of NumPy's major advantages for numerical work.
"""


# ============================================================================
# PART 18 — DSA FOUNDATION: MANUAL LINEAR SEARCH AND BASIC LOOP LOGIC
# ============================================================================

def linear_search(data, target):
    """
    Return the index of target, or -1 if it is absent.

    Time complexity: O(n)
    Worst case: inspect every element.
    """
    for index in range(len(data)):
        if data[index] == target:
            return index
    return -1


def count_occurrences(data, target):
    """Count how many times target occurs. Time complexity: O(n)."""
    count = 0
    for value in data:
        if value == target:
            count += 1
    return count


def find_maximum(data):
    """Find the maximum without using max(). Time complexity: O(n)."""
    if len(data) == 0:
        raise ValueError("Cannot find maximum of an empty collection")

    largest = data[0]
    for index in range(1, len(data)):
        if data[index] > largest:
            largest = data[index]
    return largest


print("\nPART 18 — Manual DSA algorithms:")
sample = [12, 7, 25, 7, 40, 3]
print("Data:", sample)
print("Index of 40:", linear_search(sample, 40))
print("Index of 999 (not found):", linear_search(sample, 999))
print("Count of 7:", count_occurrences(sample, 7))
print("Maximum:", find_maximum(sample))

"""
LINEAR SEARCH — memory aid
--------------------------
1. Start at index 0.
2. Compare current element with target.
3. If equal, return the current index.
4. Otherwise move to the next index.
5. If the loop ends, target was not found.

Why O(n)?
If there are n elements, the algorithm may inspect all n elements.

For one billion elements, a worst-case linear search can require up to
one billion comparisons. Actual time depends on CPU, language, memory,
and whether the target is found earlier.
"""


# ============================================================================
# PART 19 — COMMON ERRORS AND HOW TO FIX THEM
# ============================================================================

"""
1. IndexError: array index out of range
   Cause:
       a[10] when the last valid index is 9.
   Fix:
       Check len(a), remember indexing starts at 0.

2. ValueError: value not in array
   Cause:
       a.index(999) when 999 does not exist.
   Fix:
       Use try/except or manually search.

3. TypeError when inserting a wrong type into array.array
   Cause:
       An integer array cannot store an arbitrary float/string.
   Fix:
       Use a suitable type code or use a list if mixed values are required.

4. NumPy ModuleNotFoundError
   Cause:
       NumPy is not installed in the interpreter/environment running code.
   Fix:
       python -m pip install numpy

5. Wrong loop range
   Cause:
       range(0, len(a) - 1) skips the last element.
   Fix:
       range(len(a))

6. Printing reverse() and seeing None
   Cause:
       reverse() changes the array in place and returns None.
   Fix:
       a.reverse()
       print(a)

7. Wrong array length after deletion
   Cause:
       Loop uses an old hard-coded length.
   Fix:
       Use len(current_array) at the time of traversal.

8. Confusing insert and overwrite
   insert(i, x) adds an item and shifts values.
   a[i] = x replaces the existing item.
"""


# ============================================================================
# PART 20 — QUICK REFERENCE
# ============================================================================

"""
array.array:
    import array
    a = array.array('i', [1, 2, 3])
    len(a)             # number of elements
    a[0]               # access
    a[1] = 50          # overwrite
    a.insert(1, 50)    # insert at index
    a.append(100)      # add at end
    a.pop(2)           # remove by index and return value
    a.pop()            # remove last and return value
    a.remove(50)       # remove first matching value
    a.index(3)         # find first matching index
    a.reverse()        # reverse in place
    a.typecode         # type code
    a.itemsize         # bytes per item
    a.tolist()         # convert to list

NumPy:
    import numpy as np
    np.array([1, 2, 3])
    np.array([1, 2, 3], dtype=float)
    np.linspace(10, 20, 5)
    np.arange(10, 20, 2)
    np.logspace(1, 3, 4)
    np.zeros(10)
    np.ones(10)
    np.full(10, 5)
    a.ndim             # number of dimensions
    a.shape            # dimensions/shape
    a.size             # total number of elements
    a.dtype            # data type
"""


# ============================================================================
# PART 21 — PRACTICE TASKS (TRY BEFORE READING THE SOLUTIONS)
# ============================================================================

def run_practice_tasks():
    """
    Run this function to see sample solutions.
    First try solving each task yourself.
    """
    print("\nPART 21 — Practice tasks and sample solutions")

    # Task 1: Create an integer array from 1 to 5 and print every item.
    task1 = array.array('i', [1, 2, 3, 4, 5])
    print("Task 1:", end=" ")
    for item in task1:
        print(item, end=" ")
    print()

    # Task 2: Insert 99 at index 2.
    task2 = array.array('i', [10, 20, 30, 40])
    task2.insert(2, 99)
    print("Task 2:", task2)

    # Task 3: Remove the last item.
    task3 = array.array('i', [10, 20, 30, 40])
    removed = task3.pop()
    print("Task 3: removed =", removed, "| remaining =", task3)

    # Task 4: Reverse a collection using slicing (new list).
    task4 = [1, 2, 3, 4, 5]
    print("Task 4:", task4[::-1])

    # Task 5: Find the index of 30 using the manual linear search.
    task5 = [10, 20, 30, 40]
    print("Task 5:", linear_search(task5, 30))

    # Task 6: Make a new list containing squares of each value.
    task6 = [1, 2, 3, 4, 5]
    squares = [x * x for x in task6]
    print("Task 6:", squares)

    # Task 7: Count even numbers.
    task7 = [2, 5, 8, 11, 14, 17]
    even_count = 0
    for value in task7:
        if value % 2 == 0:
            even_count += 1
    print("Task 7: even count =", even_count)

    # Task 8: NumPy 2D array and shape.
    if NUMPY_AVAILABLE:
        task8 = np.array([[1, 2, 3], [4, 5, 6]])
        print("Task 8:\n", task8)
        print("Task 8 shape:", task8.shape)


# ============================================================================
# PART 22 — MINI SELF-TEST
# ============================================================================

def self_test():
    """Small automatic checks to confirm that the examples behave as expected."""
    a = array.array('i', [1, 2, 3])
    assert len(a) == 3
    assert a[0] == 1
    a.insert(1, 9)
    assert a.tolist() == [1, 9, 2, 3]
    assert a.pop(1) == 9
    a.remove(3)
    assert a.tolist() == [1, 2]
    assert linear_search([4, 8, 12], 8) == 1
    assert linear_search([4, 8, 12], 99) == -1
    if NUMPY_AVAILABLE:
        assert np.array([[1, 2], [3, 4]]).shape == (2, 2)
        assert np.linspace(10, 20, 5).size == 5
    print("\nSELF-TEST PASSED: core examples are working.")


# ============================================================================
# RUN CONTROL
# ============================================================================

if __name__ == "__main__":
    self_test()

    # Uncomment the next line to practise the user-input program:
    # input_integer_array()

    # Uncomment the next line to run the practice-task solutions:
    # run_practice_tasks()

    print("\nEnd of notes. Change the example values and run the file again.")
