"""
============================================================
                     CIRCULAR QUEUE
============================================================

1. WHAT IS A CIRCULAR QUEUE?
----------------------------
A Circular Queue is a linear data structure that follows
the FIFO (First In, First Out) principle.

Unlike a normal linear queue, the LAST position is logically
connected to the FIRST position, forming a circle.

When the REAR reaches the last index of the array, it can
return to the beginning if empty spaces are available.

MAIN PURPOSE:
To reuse the empty spaces created after deleting elements
from the FRONT.

REAL-LIFE EXAMPLE:
Imagine people sitting around a circular table:
- New people can occupy the next available position.
- After reaching the last seat, we can use the first
  available seat again.
- The arrangement continues in a circular manner.

2. WHY DO WE NEED A CIRCULAR QUEUE?
-----------------------------------
In a normal LINEAR QUEUE using an array:

- Insertion happens at REAR.
- Deletion happens at FRONT.
- After deletion, empty spaces are created at the beginning.
- REAR may reach the last array position.
- Even if empty spaces exist at the beginning, they cannot
  be reused by a simple linear queue.

This situation is called FALSE OVERFLOW.

SOLUTION:
Circular Queue connects the last position to the first
position so that empty spaces can be reused.

3. HOW DOES A CIRCULAR QUEUE WORK?
----------------------------------
A Circular Queue uses two important variables:

FRONT:
- Points to the first element.
- Deletion takes place from FRONT.

REAR:
- Points to the last element.
- Insertion takes place at REAR.

Initially:
FRONT = -1
REAR  = -1

-1 indicates that the queue is EMPTY.

IMPORTANT:
Both FRONT and REAR move circularly using the MODULO (%)
operator.

4. UNDERSTANDING CIRCULAR MOVEMENT
----------------------------------

Suppose the queue has a capacity of 5.

Array:
[10, 20, 30, 40, 50]

Indices:
  0   1   2   3   4

If REAR is at index 4 and we want to move it forward,
it returns to index 0.

FORMULA:
next position = (current position + 1) % size

EXAMPLES:

(0 + 1) % 5 = 1
(1 + 1) % 5 = 2
(2 + 1) % 5 = 3
(3 + 1) % 5 = 4
(4 + 1) % 5 = 0

Therefore, the movement is:

0 -> 1 -> 2 -> 3 -> 4 -> 0

This is how a circular queue works.

5. BASIC CIRCULAR QUEUE OPERATIONS
----------------------------------

A. ENQUEUE (INSERTION)
---------------------
- Adds a new element at the REAR.
- REAR moves to the next circular position.
- If the queue is empty, both FRONT and REAR become 0.

STEPS:
1. Check whether the queue is FULL.
2. If FULL, display OVERFLOW.
3. If EMPTY, set FRONT = REAR = 0.
4. Otherwise, update REAR using modulo.
5. Insert the new element at REAR.

B. DEQUEUE (DELETION)
---------------------
- Removes the element from the FRONT.
- FRONT moves to the next circular position.

STEPS:
1. Check whether the queue is EMPTY.
2. If EMPTY, display UNDERFLOW.
3. Store the element at FRONT.
4. If FRONT == REAR, only one element was present.
   Set FRONT = REAR = -1.
5. Otherwise, update FRONT using modulo.

C. PEEK / FRONT
---------------
- Returns the first element without removing it.
- Access using queue[front].

D. REAR
-------
- Returns the last element without removing it.
- Access using queue[rear].

E. DISPLAY
----------
- Displays all elements from FRONT to REAR.
- Since the queue is circular, traversal must also be
  performed circularly.

6. IMPORTANT CONDITIONS
-----------------------

A. QUEUE EMPTY (UNDERFLOW)
-------------------------
A circular queue is EMPTY when:

front == -1

Initially:
FRONT = -1
REAR  = -1

B. QUEUE FULL (OVERFLOW)
-----------------------
A circular queue is FULL when the next position of REAR
is equal to FRONT.

CONDITION:

(rear + 1) % size == front

WHY?
- REAR cannot move forward because FRONT is occupying
  the next circular position.
- Therefore, there is no empty space available.

IMPORTANT:
This implementation reserves one array position to
distinguish FULL from EMPTY.

7. COMPLETE EXAMPLE
-------------------

Suppose:
SIZE = 5

Initially:
[_, _, _, _, _]

FRONT = -1
REAR  = -1

ENQUEUE(10):
[10, _, _, _, _]
FRONT = 0
REAR  = 0

ENQUEUE(20):
[10, 20, _, _, _]
FRONT = 0
REAR  = 1

ENQUEUE(30):
[10, 20, 30, _, _]
FRONT = 0
REAR  = 2

ENQUEUE(40):
[10, 20, 30, 40, _]
FRONT = 0
REAR  = 3

DEQUEUE():
Removes 10.

[_, 20, 30, 40, _]
FRONT = 1
REAR  = 3

DEQUEUE():
Removes 20.

[_, _, 30, 40, _]
FRONT = 2
REAR  = 3

ENQUEUE(50):
[_, _, 30, 40, 50]
FRONT = 2
REAR  = 4

ENQUEUE(60):
REAR moves back to index 0.

[60, _, 30, 40, 50]
FRONT = 2
REAR  = 0

NOTICE:
The REAR has returned to the beginning of the array.
The empty space created by deletion has been reused.

8. IMPLEMENTATION IN PYTHON
---------------------------

A circular queue can be implemented using a FIXED-SIZE
list (array).

IMPORTANT VARIABLES:

- queue : Stores the elements.
- size  : Maximum capacity of the queue.
- front : Index of the first element.
- rear  : Index of the last element.

INITIALIZATION:

size = 5
queue = [None] * size

front = -1
rear = -1

ENQUEUE LOGIC:

1. Check whether queue is full:

   (rear + 1) % size == front

2. If empty:

   front = rear = 0

3. Otherwise:

   rear = (rear + 1) % size

4. Insert:

   queue[rear] = value

DEQUEUE LOGIC:

1. Check whether queue is empty:

   front == -1

2. Store the front element:

   value = queue[front]

3. If only one element exists:

   front == rear

   Set:
   front = rear = -1

4. Otherwise:

   front = (front + 1) % size

5. Return the deleted value.

9. IMPORTANT PYTHON FUNCTIONS AND LOGIC
---------------------------------------

- [None] * size:
  Creates a fixed-size list.

- (rear + 1) % size:
  Moves REAR to the next circular position.

- (front + 1) % size:
  Moves FRONT to the next circular position.

- queue[front]:
  Accesses the first element.

- queue[rear]:
  Accesses the last element.

- front == -1:
  Checks whether the queue is EMPTY.

- (rear + 1) % size == front:
  Checks whether the queue is FULL.

10. DISPLAY LOGIC
-----------------
Displaying a circular queue requires special attention
because FRONT may be greater than REAR.

Example:

Array:
[60, _, 30, 40, 50]

FRONT = 2
REAR  = 0

Correct display:
30 40 50 60

LOGIC:

i = front

while True:
    print(queue[i])

    if i == rear:
        break

    i = (i + 1) % size

WHY?
- Start from FRONT.
- Print the current element.
- Move to the next circular position.
- Stop after printing the REAR element.

11. TIME AND SPACE COMPLEXITY
-----------------------------

ENQUEUE:    O(1)
DEQUEUE:    O(1)
PEEK:       O(1)
ISEMPTY:    O(1)
ISFULL:     O(1)
DISPLAY:    O(n)

Space Complexity: O(n)

Where:
n = Maximum capacity of the circular queue.

WHY?
- Insertion and deletion update only a few variables.
- No shifting of elements is required.
- The queue uses a fixed-size array.

12. IMPORTANT PROPERTIES
------------------------
- Follows FIFO (First In, First Out).
- Insertion takes place at REAR.
- Deletion takes place at FRONT.
- The last position is logically connected to the first.
- Uses FRONT and REAR pointers/indices.
- Uses the MODULO (%) operator for circular movement.
- Reuses empty spaces.
- Prevents false overflow in a linear array queue.
- Usually implemented using a fixed-size array.

13. APPLICATIONS OF CIRCULAR QUEUE
----------------------------------
- CPU Round Robin Scheduling.
- Circular Buffers.
- Keyboard Buffers.
- Network Data Transmission.
- Audio and Video Streaming.
- Memory Management.
- Printer Scheduling.
- I/O Buffering.
- Operating System Scheduling.

14. DIFFERENCE BETWEEN LINEAR AND CIRCULAR QUEUE
------------------------------------------------

LINEAR QUEUE:
- Follows FIFO.
- REAR moves only forward.
- Empty spaces at the beginning may be wasted.
- Can suffer from false overflow.
- Does not reuse deleted positions automatically.

CIRCULAR QUEUE:
- Follows FIFO.
- REAR moves circularly.
- Reuses empty spaces.
- Avoids false overflow.
- Uses modulo (%) for movement.

15. IMPORTANT FORMULAS TO REMEMBER
----------------------------------

EMPTY CONDITION:

front == -1

FULL CONDITION:

(rear + 1) % size == front

NEXT REAR POSITION:

(rear + 1) % size

NEXT FRONT POSITION:

(front + 1) % size

FIRST INSERTION:

front = rear = 0

DELETION OF LAST ELEMENT:

front = rear = -1

============================================================
                    REMEMBER THE LOGIC
============================================================

ENQUEUE -> Insert at REAR.
DEQUEUE -> Delete from FRONT.
FRONT   -> Points to the first element.
REAR    -> Points to the last element.

MODULO (%) -> Makes the movement circular.

EMPTY -> front == -1

FULL  -> (rear + 1) % size == front

============================================================

IMPORTANT EXAM TIP:
The most important part of a circular queue is understanding
how FRONT and REAR move using the modulo operator.

Always remember:
When REAR reaches the last index, it can return to index 0
if space is available.

============================================================
"""

