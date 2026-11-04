"""
============================================================
                         STACK
============================================================

1. WHAT IS A STACK?
-------------------
A Stack is a linear data structure in which insertion and
deletion of elements take place from ONLY ONE END, called TOP.

It follows the LIFO principle:

LIFO = LAST IN, FIRST OUT

The element inserted LAST will be removed FIRST.

REAL-LIFE EXAMPLE:
A stack of plates:
- You place a new plate on the top.
- You remove the plate from the top.
- You cannot directly remove a plate from the middle.

2. HOW DOES A STACK WORK?
-------------------------
A stack has one important position called TOP.

- PUSH  : Insert an element at the TOP.
- POP   : Remove the topmost element.
- PEEK  : View the topmost element without removing it.
- DISPLAY: Print all elements of the stack.
- ISEMPTY: Check whether the stack is empty.

3. STACK REPRESENTATION
-----------------------

Initially:
Stack = []
TOP = -1

After PUSH(10):
Stack = [10]
TOP = 0

After PUSH(20):
Stack = [10, 20]
TOP = 1

After PUSH(30):
Stack = [10, 20, 30]
TOP = 2

After POP():
Stack = [10, 20]
TOP = 1

The TOP always points to the last inserted element.

NOTE:
In Python, the last element of a list represents the TOP
when we implement a stack using a list.

4. BASIC STACK OPERATIONS
-------------------------

A. PUSH (INSERTION)
-------------------
- Adds a new element to the TOP of the stack.
- In Python, use append().

Example:
stack.append(10)

B. POP (DELETION)
-----------------
- Removes the element from the TOP.
- In Python, use pop().

Example:
stack.pop()

IMPORTANT:
Always check whether the stack is empty before performing
POP, otherwise an IndexError occurs.

C. PEEK (TOP ELEMENT)
---------------------
- Returns the topmost element without deleting it.
- In Python, access stack[-1].

Example:
stack[-1]

D. ISEMPTY
----------
- Checks whether the stack contains any elements.
- Returns True if the stack is empty.
- Returns False if the stack contains elements.

Example:
len(stack) == 0

E. DISPLAY
----------
- Displays all elements present in the stack.
- The TOP element is the last element of the list.

5. EXAMPLE OF STACK OPERATIONS
------------------------------

Initially:
stack = []

PUSH(10):
[10]

PUSH(20):
[10, 20]

PUSH(30):
[10, 20, 30]

PEEK():
30

POP():
Removes 30
[10, 20]

PUSH(40):
[10, 20, 40]

POP():
Removes 40
[10, 20]

FINAL STACK:
[10, 20]

TOP ELEMENT = 20

6. STACK CONDITIONS
-------------------

A. STACK UNDERFLOW
------------------
Occurs when we try to POP or PEEK an element from an
EMPTY stack.

Example:
stack = []
stack.pop()  # Underflow condition

Solution:
Always check whether the stack is empty before POP or PEEK.

B. STACK OVERFLOW
-----------------
Occurs when we try to insert an element into a FULL stack.

In an array-based stack with a fixed capacity, overflow
occurs when the stack reaches its maximum size.

NOTE:
A normal Python list-based stack does not have a predefined
fixed capacity. It grows dynamically, subject to available
memory.

7. IMPORTANT PYTHON FUNCTIONS
-----------------------------
- append(x) : Inserts x at the top.
- pop()     : Removes and returns the top element.
- stack[-1] : Accesses the top element.
- len()     : Returns the number of elements.
- not stack : Checks whether the stack is empty.

8. TIME AND SPACE COMPLEXITY
----------------------------

PUSH:       O(1) amortized
POP:        O(1)
PEEK:       O(1)
ISEMPTY:    O(1)
DISPLAY:    O(n)
SEARCH:     O(n)

Space Complexity: O(n)

Where n = Number of elements in the stack.

9. IMPORTANT PROPERTIES
-----------------------
- Follows LIFO (Last In, First Out).
- Insertion and deletion happen only at the TOP.
- Can be implemented using arrays or linked lists.
- No direct insertion or deletion from the middle.
- PUSH and POP are the fundamental operations.

10. APPLICATIONS OF STACK
-------------------------
- Undo and Redo operations.
- Browser back and forward navigation.
- Function calls and recursion (Call Stack).
- Expression evaluation.
- Infix to Postfix conversion.
- Parentheses balancing.
- Reversing strings.
- Depth First Search (DFS).
- Backtracking and maze solving.

11. IMPORTANT DIFFERENCE
------------------------

STACK:
LIFO (Last In, First Out)

QUEUE:
FIFO (First In, First Out)

In STACK:
Insertion = PUSH
Deletion  = POP

In QUEUE:
Insertion = ENQUEUE
Deletion  = DEQUEUE

============================================================
                  REMEMBER THE LOGIC
============================================================

PUSH  -> Add element at TOP.
POP   -> Remove element from TOP.
PEEK  -> View TOP without removing it.
LIFO  -> Last element inserted comes out first.

============================================================
"""
class stack:
    def __init__(self):
        self.st = []

    def length(self):
        return len(self.st)

