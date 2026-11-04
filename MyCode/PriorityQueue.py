"""
============================================================
                     PRIORITY QUEUE
============================================================

1. WHAT IS A PRIORITY QUEUE?
----------------------------
A Priority Queue is a linear-style data structure in which
elements are removed according to their PRIORITY rather
than simply following their insertion order.

Every element is associated with a priority.

The element with the HIGHEST priority is removed first.

IMPORTANT:
- A normal queue follows FIFO (First In, First Out).
- A priority queue follows PRIORITY ORDER.
- An element inserted later can be removed before an
  element inserted earlier if it has higher priority.

REAL-LIFE EXAMPLE:
Hospital Emergency Room:
- A critically injured patient is treated first.
- A less serious patient may have to wait.
- The order of arrival is not the only deciding factor.

2. HOW DOES A PRIORITY QUEUE WORK?
----------------------------------
Each element is associated with a priority value.

Example:

Elements with priorities:

A -> Priority 3
B -> Priority 1
C -> Priority 5
D -> Priority 2

If a SMALLER NUMBER represents HIGHER priority:

Removal order:
B -> D -> A -> C

Because:
Priority 1 is highest.
Priority 5 is lowest.

NOTE:
Priority conventions depend on the implementation.
In Python's heapq, the SMALLEST priority value is removed
first (MIN-HEAP).

3. BASIC PRIORITY QUEUE OPERATIONS
----------------------------------

A. INSERT / ENQUEUE
-------------------
- Adds an element along with its priority.
- The element is placed according to the priority structure.
- In Python heapq, use heappush().

Example:
heapq.heappush(pq, (1, "Emergency"))

B. DELETE / DEQUEUE
-------------------
- Removes the element with the highest priority.
- In Python heapq, use heappop().

Example:
heapq.heappop(pq)

IMPORTANT:
In Python's min-heap, the smallest priority number is
removed first.

C. PEEK
-------
- Returns the highest-priority element without removing it.
- In Python heapq, access pq[0].

Example:
pq[0]

D. ISEMPTY
----------
- Checks whether the priority queue is empty.
- Returns True if empty.
- Returns False if elements are present.

Example:
len(pq) == 0

E. DISPLAY
----------
- Displays the elements currently stored in the heap.

IMPORTANT:
Printing a heap does NOT necessarily display elements
in sorted priority order.

4. EXAMPLE OF PRIORITY QUEUE OPERATIONS
----------------------------------------

Initially:
pq = []

INSERT (A, Priority 3):
[(3, 'A')]

INSERT (B, Priority 1):
[(1, 'B'), (3, 'A')]

INSERT (C, Priority 5):
[(1, 'B'), (3, 'A'), (5, 'C')]

INSERT (D, Priority 2):
[(1, 'B'), (2, 'D'), (5, 'C'), (3, 'A')]

PEEK:
(1, 'B')

DEQUEUE:
Removes (1, 'B')

DEQUEUE:
Removes (2, 'D')

DEQUEUE:
Removes (3, 'A')

DEQUEUE:
Removes (5, 'C')

REMOVAL ORDER:
B -> D -> A -> C

NOTE:
The internal arrangement of a heap may differ, but
the smallest priority element is always at index 0.

5. IMPLEMENTATION IN PYTHON USING HEAPQ
---------------------------------------

Python provides the heapq module to implement a
priority queue using a MIN-HEAP.

IMPORT:
import heapq

CREATE:
pq = []

INSERT:
heapq.heappush(pq, (priority, element))

DELETE:
heapq.heappop(pq)

PEEK:
pq[0]

CHECK EMPTY:
len(pq) == 0

DISPLAY:
print(pq)

EXAMPLE:

import heapq

pq = []

heapq.heappush(pq, (3, "A"))
heapq.heappush(pq, (1, "B"))
heapq.heappush(pq, (5, "C"))
heapq.heappush(pq, (2, "D"))

print("Priority Queue:", pq)
print("Highest Priority:", pq[0])

while pq:
    priority, element = heapq.heappop(pq)
    print(element, "Priority:", priority)

6. MIN-HEAP AND MAX-HEAP
------------------------

A. MIN-HEAP
-----------
- The smallest element has the highest priority.
- The smallest element is always at the ROOT.
- Python heapq directly implements a min-heap.

Example:
[1, 3, 5, 7, 9]

The root element is 1.

B. MAX-HEAP
-----------
- The largest element has the highest priority.
- The largest element is always at the ROOT.
- A max-heap can be implemented by storing negative
  priority values in Python's heapq.

Example:

Insert:
heapq.heappush(pq, -10)
heapq.heappush(pq, -30)
heapq.heappush(pq, -20)

Delete:
value = -heapq.heappop(pq)

Output:
30

NOTE:
Negating numeric priorities reverses their ordering.
It does not directly work for arbitrary non-numeric priorities.

7. HANDLING ELEMENTS WITH THE SAME PRIORITY
-------------------------------------------
When two elements have the same priority, they are tied.

A heap does NOT automatically guarantee FIFO ordering
for elements with equal priority.

To preserve insertion order, use a counter.

Example:

import heapq
import itertools

pq = []
counter = itertools.count()

heapq.heappush(pq, (2, next(counter), "A"))
heapq.heappush(pq, (1, next(counter), "B"))
heapq.heappush(pq, (2, next(counter), "C"))

while pq:
    priority, order, element = heapq.heappop(pq)
    print(element)

Output:
B
A
C

WHY USE A COUNTER?
------------------
- Priority decides which group comes first.
- Counter decides the insertion order within equal priorities.
- It also avoids comparing task objects when priorities tie.

8. TIME AND SPACE COMPLEXITY
----------------------------

For Python heapq:

INSERT:       O(log n)
DELETE:       O(log n)
PEEK:         O(1)
HEAPIFY:      O(n)
SEARCH:       O(n)

Space Complexity: O(n)

Where:
n = Number of elements in the priority queue.

WHY?
----
- Insertion may require rearranging the heap.
- Deletion may require rearranging the heap.
- The heap root is directly accessible.
- Searching for an arbitrary element may require
  checking multiple elements.

9. IMPORTANT PROPERTIES
-----------------------
- Elements are removed according to priority.
- Does not necessarily follow FIFO.
- Python heapq implements a min-heap by default.
- The smallest priority value is removed first.
- The root contains the highest-priority element
  according to the chosen priority convention.
- Can be implemented using heaps, arrays and linked lists.
- A heap does not store all elements in completely sorted
  order.

10. TYPES OF PRIORITY QUEUES
----------------------------

A. ASCENDING PRIORITY QUEUE
---------------------------
- Smaller priority value represents higher priority.
- Element with the smallest value is removed first.
- Similar to a min-heap.

B. DESCENDING PRIORITY QUEUE
----------------------------
- Larger priority value represents higher priority.
- Element with the largest value is removed first.
- Similar to a max-heap.

11. APPLICATIONS OF PRIORITY QUEUE
----------------------------------
- Hospital emergency management.
- CPU Process Scheduling.
- Dijkstra's Shortest Path Algorithm.
- Prim's Minimum Spanning Tree Algorithm.
- Network packet scheduling.
- Event-driven simulation.
- A* Search Algorithm.
- Task scheduling.
- Huffman Coding.
- Operating System resource management.

12. DIFFERENCE BETWEEN QUEUE AND PRIORITY QUEUE
-----------------------------------------------

NORMAL QUEUE:
- Follows FIFO.
- First inserted element is removed first.
- Insertion takes place at REAR.
- Deletion takes place at FRONT.

PRIORITY QUEUE:
- Follows PRIORITY ORDER.
- Highest-priority element is removed first.
- Every element has an associated priority.
- Insertion and deletion depend on priority.

13. IMPORTANT PYTHON FUNCTIONS
------------------------------

Using heapq:

- heappush(pq, x) : Inserts an element into the heap.
- heappop(pq)     : Removes and returns the smallest element.
- pq[0]           : Accesses the smallest element.
- heapify(pq)     : Converts a list into a heap.
- heappushpop()   : Pushes an element and pops the smallest.
- heapreplace()   : Removes the smallest and inserts a new one.

============================================================
                    REMEMBER THE LOGIC
============================================================

INSERT   -> heappush()
DELETE   -> heappop()
PEEK     -> pq[0]
MIN-HEAP -> Smallest element comes out first.
MAX-HEAP -> Largest element comes out first (using
            reversed numeric priorities in heapq).

IMPORTANT:
Python heapq uses MIN-HEAP by default.

A smaller numerical priority value means higher priority
unless you deliberately reverse the priority convention.

============================================================
"""


