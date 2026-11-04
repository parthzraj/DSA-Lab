"""
============================================================
                  DEQUE (DOUBLE ENDED QUEUE)
============================================================

1. WHAT IS A DEQUE?
-------------------
Deque stands for DOUBLE ENDED QUEUE.

It is a linear data structure in which INSERTION and
DELETION can take place from BOTH ENDS:

1. FRONT
2. REAR

Unlike a normal queue, where insertion happens only at REAR
and deletion happens only at FRONT, a deque allows operations
at both ends.

It can behave like BOTH:
- STACK (LIFO)
- QUEUE (FIFO)

REAL-LIFE EXAMPLE:
Imagine a line where people can:
- Join from the FRONT or REAR.
- Leave from the FRONT or REAR.

2. HOW DOES A DEQUE WORK?
-------------------------
A deque has two important positions:

FRONT:
- Represents the first element.
- Elements can be inserted or deleted here.

REAR:
- Represents the last element.
- Elements can be inserted or deleted here.

Initially:
Deque = []

After INSERT REAR (10):
[10]

After INSERT REAR (20):
[10, 20]

After INSERT FRONT (5):
[5, 10, 20]

After INSERT FRONT (2):
[2, 5, 10, 20]

After DELETE REAR:
[2, 5, 10]

After DELETE FRONT:
[5, 10]

3. TYPES OF DEQUE
-----------------

A. INPUT RESTRICTED DEQUE
-------------------------
- Insertion is allowed at ONLY ONE end (usually REAR).
- Deletion is allowed at BOTH FRONT and REAR.

B. OUTPUT RESTRICTED DEQUE
--------------------------
- Insertion is allowed at BOTH FRONT and REAR.
- Deletion is allowed at ONLY ONE end (usually FRONT).

C. GENERAL DEQUE
----------------
- Insertion is allowed at BOTH ends.
- Deletion is allowed at BOTH ends.

4. BASIC DEQUE OPERATIONS
-------------------------

A. INSERT FRONT
---------------
- Adds an element at the FRONT of the deque.
- In Python, use appendleft().

Example:
dq.appendleft(10)

B. INSERT REAR
--------------
- Adds an element at the REAR of the deque.
- In Python, use append().

Example:
dq.append(20)

C. DELETE FRONT
---------------
- Removes the element from the FRONT.
- In Python, use popleft().

Example:
dq.popleft()

D. DELETE REAR
--------------
- Removes the element from the REAR.
- In Python, use pop().

Example:
dq.pop()

E. PEEK FRONT
-------------
- Returns the FRONT element without removing it.
- Access using dq[0].

Example:
dq[0]

F. PEEK REAR
------------
- Returns the REAR element without removing it.
- Access using dq[-1].

Example:
dq[-1]

G. ISEMPTY
----------
- Checks whether the deque is empty.
- Returns True if empty.
- Returns False if elements are present.

Example:
len(dq) == 0

H. DISPLAY
----------
- Displays all elements from FRONT to REAR.

Example:
print(dq)

5. EXAMPLE OF DEQUE OPERATIONS
------------------------------

Initially:
dq = []

INSERT REAR (10):
[10]

INSERT REAR (20):
[10, 20]

INSERT FRONT (5):
[5, 10, 20]

INSERT FRONT (2):
[2, 5, 10, 20]

PEEK FRONT:
2

PEEK REAR:
20

DELETE FRONT:
Removes 2
[5, 10, 20]

DELETE REAR:
Removes 20
[5, 10]

INSERT REAR (30):
[5, 10, 30]

FINAL DEQUE:
[5, 10, 30]

FRONT ELEMENT = 5
REAR ELEMENT  = 30

6. IMPLEMENTATION IN PYTHON
---------------------------
Python provides a built-in deque data structure through
the collections module.

IMPORT:
from collections import deque

CREATE:
dq = deque()

INSERT FRONT:
dq.appendleft(x)

INSERT REAR:
dq.append(x)

DELETE FRONT:
dq.popleft()

DELETE REAR:
dq.pop()

PEEK FRONT:
dq[0]

PEEK REAR:
dq[-1]

CHECK EMPTY:
len(dq) == 0

DISPLAY:
print(dq)

IMPORTANT:
Always check whether the deque is empty before performing
popleft(), pop(), or accessing dq[0] / dq[-1].

Otherwise, an IndexError may occur.

7. TIME AND SPACE COMPLEXITY
----------------------------

For Python collections.deque:

INSERT FRONT: O(1)
INSERT REAR:  O(1)
DELETE FRONT: O(1)
DELETE REAR:  O(1)
PEEK FRONT:   O(1)
PEEK REAR:    O(1)
DISPLAY:      O(n)
SEARCH:       O(n)

Space Complexity: O(n)

Where n = Number of elements in the deque.

NOTE:
Accessing elements near the middle takes O(n) time.
Deque is optimized for operations at its two ends.

8. IMPORTANT PYTHON FUNCTIONS
------------------------------

- append(x)     : Inserts x at the REAR.
- appendleft(x) : Inserts x at the FRONT.
- pop()         : Deletes from the REAR.
- popleft()     : Deletes from the FRONT.
- dq[0]         : Accesses the FRONT element.
- dq[-1]        : Accesses the REAR element.
- len(dq)       : Returns the number of elements.
- clear()       : Removes all elements.
- reverse()     : Reverses the deque.
- count(x)      : Counts occurrences of x.
- remove(x)     : Removes the first occurrence of x.

9. IMPORTANT PROPERTIES
-----------------------
- Allows insertion at BOTH ends.
- Allows deletion at BOTH ends.
- Can behave like a STACK or a QUEUE.
- Follows no single mandatory LIFO or FIFO restriction.
- Efficient for operations at both ends.
- Python implements deque using collections.deque.
- It is not designed for efficient insertion or deletion
  from the middle.

10. APPLICATIONS OF DEQUE
-------------------------
- Implementing both stacks and queues.
- Browser navigation.
- Palindrome checking.
- Sliding Window Maximum problem.
- Undo and Redo operations.
- Task scheduling.
- Breadth First Search (BFS).
- Maintaining recently used elements.
- Work-stealing algorithms.

11. DIFFERENCE BETWEEN STACK, QUEUE AND DEQUE
---------------------------------------------

STACK:
- Follows LIFO.
- Insertion = PUSH.
- Deletion = POP.
- Both operations take place at TOP.

QUEUE:
- Follows FIFO.
- Insertion = ENQUEUE (REAR).
- Deletion = DEQUEUE (FRONT).

DEQUE:
- Insertion at FRONT and REAR.
- Deletion at FRONT and REAR.
- Can be used as both a stack and a queue.

============================================================
                    REMEMBER THE LOGIC
============================================================

appendleft(x) -> Insert at FRONT.
append(x)     -> Insert at REAR.
popleft()     -> Delete from FRONT.
pop()         -> Delete from REAR.

FRONT = First element.
REAR  = Last element.

DEQUE = DOUBLE ENDED QUEUE

Insertion and deletion are possible from BOTH ENDS.

============================================================
"""


class deque:
    def __init__(self):
        self.items = []

    def length(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def insertionFront(self, data):
        self.items.insert(0, data)

    def insertionEnd(self, data):
        self.items.append(data)

    def deletionEnd(self):
        if self.isEmpty():
            print("Your queue is empty")
        else: 
            self.items.pop()

    def deletionFront(self):
        if self.isEmpty():
            print("Your queue is empty")
        else: 
            self.items.pop(0)

    def display(self):
        print("Your Queue - ", self.items)

    def peek(self):
        if self.isEmpty():
            print("Your Queue is Empty")
        else:
            return self.items[0]

deque1 = deque()
