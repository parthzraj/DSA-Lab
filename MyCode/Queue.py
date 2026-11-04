"""
============================================================
                          QUEUE
============================================================

1. WHAT IS A QUEUE?
-------------------
A Queue is a linear data structure in which insertion takes
place at ONE END (REAR) and deletion takes place at the
OTHER END (FRONT).

It follows the FIFO principle:

FIFO = FIRST IN, FIRST OUT

The element inserted FIRST will be removed FIRST.

REAL-LIFE EXAMPLE:
A queue of people waiting for a ticket:
- A new person joins at the REAR.
- The person at the FRONT gets served first.
- Nobody can directly jump ahead in the queue.

2. HOW DOES A QUEUE WORK?
-------------------------
A queue has two important positions:

FRONT:
- Points to the first element.
- The element at FRONT is removed first.

REAR:
- Points to the last element.
- New elements are inserted at REAR.

Initially:
Queue = []
FRONT = -1
REAR = -1

After ENQUEUE(10):
Queue = [10]
FRONT = 0
REAR = 0

After ENQUEUE(20):
Queue = [10, 20]
FRONT = 0
REAR = 1

After ENQUEUE(30):
Queue = [10, 20, 30]
FRONT = 0
REAR = 2

After DEQUEUE():
Queue = [20, 30]
FRONT = 0 (if using a Python list with pop(0))
REAR = 1

NOTE:
The FRONT and REAR indices shown above are for a simple
array implementation. Python list operations can be
implemented differently.

3. BASIC QUEUE OPERATIONS
-------------------------

A. ENQUEUE (INSERTION)
----------------------
- Adds a new element at the REAR of the queue.
- In Python, use append().

Example:
queue.append(10)

B. DEQUEUE (DELETION)
---------------------
- Removes the element from the FRONT of the queue.
- In a simple Python list implementation, use pop(0).

Example:
queue.pop(0)

IMPORTANT:
Always check whether the queue is empty before performing
DEQUEUE, otherwise an IndexError occurs.

C. PEEK / FRONT
---------------
- Returns the first element without removing it.
- In a Python list implementation, use queue[0].

Example:
queue[0]

D. REAR
-------
- Returns the last element without removing it.
- In a Python list implementation, use queue[-1].

Example:
queue[-1]

E. ISEMPTY
----------
- Checks whether the queue contains any elements.
- Returns True if the queue is empty.
- Returns False if the queue contains elements.

Example:
len(queue) == 0

F. DISPLAY
----------
- Displays all elements present in the queue.
- Elements are displayed from FRONT to REAR.

4. EXAMPLE OF QUEUE OPERATIONS
------------------------------

Initially:
queue = []

ENQUEUE(10):
[10]

ENQUEUE(20):
[10, 20]

ENQUEUE(30):
[10, 20, 30]

PEEK():
10

DEQUEUE():
Removes 10
[20, 30]

ENQUEUE(40):
[20, 30, 40]

DEQUEUE():
Removes 20
[30, 40]

FINAL QUEUE:
[30, 40]

FRONT ELEMENT = 30
REAR ELEMENT  = 40

5. QUEUE CONDITIONS
-------------------

A. QUEUE UNDERFLOW
------------------
Occurs when we try to DEQUEUE or PEEK an element from
an EMPTY queue.

Example:
queue = []
queue.pop(0)  # Underflow condition

Solution:
Always check whether the queue is empty before DEQUEUE
or PEEK.

B. QUEUE OVERFLOW
-----------------
Occurs when we try to insert an element into a FULL queue.

In a fixed-size array-based queue, overflow occurs when
the queue reaches its maximum capacity.

NOTE:
A normal Python list-based queue does not have a
predefined fixed capacity. It grows dynamically, subject
to available memory.

6. IMPORTANT PYTHON FUNCTIONS
-----------------------------

For a simple list-based queue:

- append(x) : Inserts x at the REAR.
- pop(0)    : Removes the FRONT element.
- queue[0]  : Accesses the FRONT element.
- queue[-1] : Accesses the REAR element.
- len()     : Returns the number of elements.
- not queue : Checks whether the queue is empty.

7. TIME AND SPACE COMPLEXITY
----------------------------

For a Python LIST-based queue:

ENQUEUE:    O(1) amortized
DEQUEUE:    O(n)
PEEK:       O(1)
ISEMPTY:    O(1)
DISPLAY:    O(n)

Space Complexity: O(n)

WHY IS DEQUEUE O(n)?
--------------------
When pop(0) removes the first element, all the remaining
elements have to shift one position to the left.

Therefore, deletion from the beginning of a Python list
takes O(n) time.

8. BETTER PYTHON IMPLEMENTATION: DEQUE
--------------------------------------
Python provides a collection called deque (Double Ended Queue)
that is more efficient for implementing a normal queue.

Import:
from collections import deque

Create:
queue = deque()

ENQUEUE:
queue.append(10)

DEQUEUE:
queue.popleft()

FRONT:
queue[0]

REAR:
queue[-1]

ISEMPTY:
len(queue) == 0

TIME COMPLEXITY USING DEQUE:
ENQUEUE: O(1)
DEQUEUE: O(1)
PEEK:    O(1)

NOTE:
For learning basic queue operations, a Python list is easy
to understand. For practical applications, prefer deque.

9. TYPES OF QUEUES
------------------

A. SIMPLE / LINEAR QUEUE
------------------------
- Follows FIFO.
- Insertion takes place at REAR.
- Deletion takes place at FRONT.
- Elements move in one direction.

B. CIRCULAR QUEUE
-----------------
- The last position is connected logically to the first.
- The REAR can return to the beginning when space is available.
- Reuses empty positions created by deletion.
- Avoids wastage of space in a fixed-size array implementation.

C. PRIORITY QUEUE
-----------------
- Every element is assigned a priority.
- Elements are removed according to priority rather than
  simply following their insertion order.
- If priorities are equal, FIFO ordering may be used.

D. DEQUE (DOUBLE ENDED QUEUE)
-----------------------------
- Insertion and deletion can take place at BOTH ends.
- Elements can be added or removed from FRONT and REAR.

10. IMPORTANT PROPERTIES
------------------------
- Follows FIFO (First In, First Out).
- Insertion takes place at REAR.
- Deletion takes place at FRONT.
- Uses FRONT and REAR positions.
- Can be implemented using arrays or linked lists.
- Commonly used in scheduling and buffering.

11. APPLICATIONS OF QUEUE
-------------------------
- CPU Process Scheduling.
- Printer Job Scheduling.
- Waiting-line management systems.
- Breadth First Search (BFS).
- Network Data Packets.
- Keyboard/Input Buffers.
- Operating System Task Scheduling.
- Call Centre Systems.
- Message Queues.

12. DIFFERENCE BETWEEN STACK AND QUEUE
--------------------------------------

STACK:
- Follows LIFO.
- Insertion = PUSH.
- Deletion = POP.
- Both operations take place at TOP.

QUEUE:
- Follows FIFO.
- Insertion = ENQUEUE.
- Deletion = DEQUEUE.
- Insertion at REAR and deletion at FRONT.

============================================================
                    REMEMBER THE LOGIC
============================================================

ENQUEUE   -> Add element at REAR.
DEQUEUE   -> Remove element from FRONT.
PEEK      -> View FRONT without removing it.
REAR      -> Last element of the queue.
FIFO      -> First element inserted comes out first.

============================================================
"""

class queue:
    def __init__(self):
        self.queue = []

    def length(self):
        return len(self.queue)

    def push(self, data):
        self.queue.append(data)

    def isEmpty(self):
        return len(self.queue) == 0

    def pop(self):
        if self.isEmpty():
            print("your queue is empty")
        else:
            self.queue.pop(0)

    def display(self):
        print(self.queue)

    def peek(self):
        if self.isEmpty():
            print("your queue is empty")
        else:
            return self.queue[-1]

