"""
============================================================
                   SINGLY LINKED LIST
============================================================

1. WHAT IS A LINKED LIST?
-------------------------
A Linked List is a LINEAR, DYNAMIC data structure in which
elements are stored in separate units called NODES.

Unlike arrays, linked list elements are NOT stored in
continuous memory locations.

Each node contains:
1. DATA  -> Stores the actual value.
2. NEXT  -> Stores the reference (address) of the next node.

The nodes are connected using references (links).

MAIN IDEA:
Each node points to the next node, forming a chain.

EXAMPLE:

HEAD
 |
 v
+------+------+
|  10  |   o-----> +------+------+
+------+------+    |  20  |   o-----> +------+------+
                   +------+------+    |  30  | None |
                                      +------+------+

Here:
- 10, 20, 30 are DATA values.
- Each arrow represents the NEXT reference.
- HEAD points to the first node.
- None indicates the end of the linked list.

2. WHAT IS A SINGLY LINKED LIST?
--------------------------------
A Singly Linked List is a type of linked list in which
each node contains:

1. DATA
2. NEXT (reference to the next node)

Every node points ONLY in the FORWARD direction.

The last node always points to None.

STRUCTURE:

+---------+---------+
|  DATA   |  NEXT   |
+---------+---------+

EXAMPLE:

HEAD
 |
 v
[10 | Next] -> [20 | Next] -> [30 | None]

IMPORTANT:
- Traversal is possible only in the forward direction.
- We cannot directly move backward.
- The last node points to None.
- HEAD stores the reference to the first node.

3. WHY DO WE NEED LINKED LISTS?
-------------------------------
In an ARRAY:
- Elements are generally stored in continuous memory.
- Insertion in the middle may require shifting elements.
- Size is usually fixed in basic static-array implementations.

In a LINKED LIST:
- Nodes can be stored at different memory locations.
- Nodes are connected using references.
- Insertion and deletion can be performed without shifting
  other nodes.
- The list can grow and shrink dynamically.

IMPORTANT:
A Python list is a dynamic array, not a linked list.
A linked list must be implemented using nodes and references.

4. BASIC TERMINOLOGIES
----------------------

A. NODE
-------
A node is an individual unit of a linked list.

It contains DATA and NEXT.

B. HEAD
-------
HEAD is a reference to the FIRST node of the linked list.

Example:

HEAD -> [10] -> [20] -> [30] -> None

If the list is empty:

HEAD = None

C. DATA
-------
Stores the actual value of a node.

Example:
Node(10)

Here, 10 is the data.

D. NEXT
-------
Stores the reference to the next node.

Example:
node.next = another_node

E. TAIL
-------
TAIL is a reference to the LAST node.

It is optional in a singly linked list implementation.

The last node always points to None.

F. NONE
-------
None indicates that there is no next node.

It represents the end of the linked list.

5. REPRESENTATION OF SINGLY LINKED LIST
---------------------------------------

Example:

HEAD
 |
 v
+----+----+    +----+----+    +----+------+
| 10 |  o----->| 20 |  o----->| 30 | None |
+----+----+    +----+----+    +----+------+

Node 1:
DATA = 10
NEXT = Address of Node 2

Node 2:
DATA = 20
NEXT = Address of Node 3

Node 3:
DATA = 30
NEXT = None

IMPORTANT:
The HEAD reference is required to access the linked list.

Without HEAD, we lose the starting reference and cannot
normally access the remaining nodes.

============================================================
                 IMPLEMENTATION IN PYTHON
============================================================

6. CREATING A NODE CLASS
------------------------
In Python, we use a CLASS to create individual nodes.

CODE:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

EXPLANATION:

- class Node:
  Creates a blueprint for a node.

- __init__():
  Constructor that initializes a new node.

- self.data = data:
  Stores the value inside the node.

- self.next = None:
  Initially, the node does not point to another node.

CREATING A NODE:

node1 = Node(10)

node1.data -> 10
node1.next -> None

CREATING MULTIPLE NODES:

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

CONNECTING NODES:

node1.next = node2
node2.next = node3

HEAD:

head = node1

RESULT:

HEAD -> 10 -> 20 -> 30 -> None

7. INITIALIZATION OF LINKED LIST
--------------------------------

Initially, the linked list is EMPTY.

head = None

This means:
- No node exists.
- There is no first element.
- The list contains zero elements.

When the first node is inserted:

head = Node(10)

Now:

HEAD -> 10 -> None

============================================================
                 OPERATIONS ON LINKED LIST
============================================================

8. INSERTION IN SINGLY LINKED LIST
----------------------------------

Insertion means adding a new node to the linked list.

There are FOUR COMMON TYPES:

1. Insertion at the Beginning.
2. Insertion at the End.
3. Insertion at a Specific Position.
4. Insertion After a Particular Value.

------------------------------------------------------------
A. INSERTION AT THE BEGINNING
------------------------------------------------------------

A new node is inserted BEFORE the current HEAD.

EXAMPLE:

BEFORE:

HEAD -> 10 -> 20 -> 30 -> None

Insert 5.

STEPS:

1. Create a new node.
2. Make the new node point to the current HEAD.
3. Update HEAD to the new node.

CODE LOGIC:

new_node = Node(5)

new_node.next = head

head = new_node

AFTER:

HEAD -> 5 -> 10 -> 20 -> 30 -> None

IMPORTANT:
First connect the new node to the old HEAD.
Then update HEAD.

If HEAD is updated first, the reference to the original
list may be lost.

TIME COMPLEXITY: O(1)

------------------------------------------------------------
B. INSERTION AT THE END
------------------------------------------------------------

A new node is inserted AFTER the current last node.

EXAMPLE:

BEFORE:

HEAD -> 10 -> 20 -> 30 -> None

Insert 40.

STEPS:

1. Create a new node.
2. Check whether the list is empty.
3. If empty, make the new node HEAD.
4. Otherwise, start from HEAD.
5. Traverse until the last node is found.
6. Connect the last node to the new node.

CODE LOGIC:

new_node = Node(40)

if head is None:
    head = new_node

else:
    temp = head

    while temp.next is not None:
        temp = temp.next

    temp.next = new_node

AFTER:

HEAD -> 10 -> 20 -> 30 -> 40 -> None

IMPORTANT:
temp.next is None means that the current node is the
LAST NODE.

TIME COMPLEXITY:
Without a TAIL reference: O(n)

With a TAIL reference: O(1)

------------------------------------------------------------
C. INSERTION AT A SPECIFIC POSITION
------------------------------------------------------------

A new node is inserted at a particular position.

For this implementation, positions start from 1.

EXAMPLE:

BEFORE:

HEAD -> 10 -> 20 -> 30 -> None

Insert 15 at Position 2.

STEPS:

1. Create a new node.
2. If position is 1, perform insertion at beginning.
3. Otherwise, start from HEAD.
4. Traverse until the node at position - 1.
5. Connect the new node to the next node.
6. Connect the previous node to the new node.

CODE LOGIC:

new_node = Node(15)

temp = head

for i in range(position - 2):
    temp = temp.next

new_node.next = temp.next
temp.next = new_node

AFTER:

HEAD -> 10 -> 15 -> 20 -> 30 -> None

IMPORTANT:
The order of these two statements matters:

new_node.next = temp.next
temp.next = new_node

First connect the new node to the remaining list.
Then connect the previous node to the new node.

TIME COMPLEXITY: O(n)

NOTE:
A complete program must validate the position and check
whether the list is empty before performing this operation.

------------------------------------------------------------
D. INSERTION AFTER A PARTICULAR VALUE
------------------------------------------------------------

A new node is inserted AFTER a node containing a specific
value.

EXAMPLE:

BEFORE:

HEAD -> 10 -> 20 -> 30 -> None

Insert 25 after 20.

STEPS:

1. Start from HEAD.
2. Search for the node containing 20.
3. Create a new node containing 25.
4. Make the new node point to the next node.
5. Make the current node point to the new node.

CODE LOGIC:

new_node = Node(25)

temp = head

while temp is not None and temp.data != 20:
    temp = temp.next

if temp is not None:
    new_node.next = temp.next
    temp.next = new_node

AFTER:

HEAD -> 10 -> 20 -> 25 -> 30 -> None

TIME COMPLEXITY: O(n)

============================================================
                 DELETION IN LINKED LIST
============================================================

9. DELETION IN SINGLY LINKED LIST
---------------------------------

Deletion means removing a node from the linked list.

There are FOUR COMMON TYPES:

1. Deletion at the Beginning.
2. Deletion at the End.
3. Deletion at a Specific Position.
4. Deletion of a Particular Value.

------------------------------------------------------------
A. DELETION AT THE BEGINNING
------------------------------------------------------------

The first node (HEAD) is removed.

BEFORE:

HEAD -> 10 -> 20 -> 30 -> None

STEPS:

1. Check whether the list is empty.
2. Store the current HEAD's next reference.
3. Update HEAD to the next node.

CODE LOGIC:

if head is not None:
    head = head.next

AFTER:

HEAD -> 20 -> 30 -> None

IMPORTANT:
When HEAD moves to the next node, the previous first
node is no longer part of the list.

TIME COMPLEXITY: O(1)

------------------------------------------------------------
B. DELETION AT THE END
------------------------------------------------------------

The last node is removed.

BEFORE:

HEAD -> 10 -> 20 -> 30 -> None

STEPS:

1. Check whether the list is empty.
2. If only one node exists, set HEAD = None.
3. Otherwise, traverse until the SECOND LAST NODE.
4. Set the second last node's NEXT to None.

CODE LOGIC:

if head is None:
    # List is empty
    pass

elif head.next is None:
    head = None

else:
    temp = head

    while temp.next.next is not None:
        temp = temp.next

    temp.next = None

AFTER:

HEAD -> 10 -> 20 -> None

IMPORTANT:
Why use temp.next.next?

Because we need to stop at the SECOND LAST NODE.

For the last node:
temp.next.next == None

TIME COMPLEXITY: O(n)

------------------------------------------------------------
C. DELETION AT A SPECIFIC POSITION
------------------------------------------------------------

Removes the node present at a particular position.

For this implementation, positions start from 1.

BEFORE:

HEAD -> 10 -> 20 -> 30 -> 40 -> None

Delete Position 2.

STEPS:

1. Check whether the list is empty.
2. If position is 1, update HEAD.
3. Otherwise, traverse to position - 1.
4. Connect the previous node to the node after the
   node being deleted.

CODE LOGIC:

temp = head

for i in range(position - 2):
    temp = temp.next

temp.next = temp.next.next

AFTER:

HEAD -> 10 -> 30 -> 40 -> None

IMPORTANT:
temp.next is the node being deleted.

temp.next.next is the node after the deleted node.

By changing the reference, we skip the node to be deleted.

TIME COMPLEXITY: O(n)

NOTE:
Always validate the position and check that temp.next
exists before accessing temp.next.next.

------------------------------------------------------------
D. DELETION OF A PARTICULAR VALUE
------------------------------------------------------------

Removes the FIRST node containing a particular value.

BEFORE:

HEAD -> 10 -> 20 -> 30 -> 40 -> None

Delete value 30.

STEPS:

1. Check whether the list is empty.
2. If HEAD contains the value, update HEAD.
3. Otherwise, search for the node.
4. Maintain a reference to the previous node.
5. Connect the previous node to the next node of the
   node being deleted.

CODE LOGIC:

temp = head

while temp.next is not None and temp.next.data != 30:
    temp = temp.next

if temp.next is not None:
    temp.next = temp.next.next

AFTER:

HEAD -> 10 -> 20 -> 40 -> None

IMPORTANT:
We use temp.next.data because temp points to the
PREVIOUS NODE of the node we want to delete.

TIME COMPLEXITY: O(n)

============================================================
                 TRAVERSAL AND SEARCHING
============================================================

10. TRAVERSAL / DISPLAY
-----------------------

Traversal means visiting each node from the beginning
to the end of the linked list.

EXAMPLE:

HEAD -> 10 -> 20 -> 30 -> None

STEPS:

1. Create a temporary reference called temp.
2. Set temp = HEAD.
3. Access and print temp.data.
4. Move to the next node using temp.next.
5. Repeat until temp becomes None.

CODE LOGIC:

temp = head

while temp is not None:
    print(temp.data)
    temp = temp.next

OUTPUT:

10
20
30

IMPORTANT:
- Never move HEAD while traversing.
- Use a temporary reference.
- temp = temp.next moves to the next node.
- The loop stops when temp becomes None.

TIME COMPLEXITY: O(n)

11. SEARCHING
-------------

Searching means finding whether a particular value exists
in the linked list.

EXAMPLE:

HEAD -> 10 -> 20 -> 30 -> 40 -> None

Search for 30.

STEPS:

1. Start from HEAD.
2. Compare the current node's data with the target.
3. If equal, the element is FOUND.
4. Otherwise, move to the next node.
5. Continue until the value is found or temp becomes None.

CODE LOGIC:

temp = head

while temp is not None:

    if temp.data == key:
        print("Element Found")
        break

    temp = temp.next

if temp is None:
    print("Element Not Found")

IMPORTANT:
Unlike a BST, a singly linked list does not have a
left/right ordering property.

Therefore, searching generally requires sequential
traversal.

TIME COMPLEXITY:
Best Case: O(1)
Worst Case: O(n)

12. COUNTING THE NUMBER OF NODES
--------------------------------

Counts the total number of nodes in the linked list.

STEPS:

1. Start from HEAD.
2. Initialize count = 0.
3. Visit each node.
4. Increase count by 1.
5. Move to the next node.
6. Stop when temp becomes None.

CODE LOGIC:

count = 0
temp = head

while temp is not None:
    count += 1
    temp = temp.next

print(count)

EXAMPLE:

HEAD -> 10 -> 20 -> 30 -> None

OUTPUT:
3

TIME COMPLEXITY: O(n)

13. REVERSING A SINGLY LINKED LIST
----------------------------------

Reversing means changing the direction of all NEXT
references so that the last node becomes the first node.

BEFORE:

HEAD -> 10 -> 20 -> 30 -> 40 -> None

AFTER:

HEAD -> 40 -> 30 -> 20 -> 10 -> None

THREE IMPORTANT VARIABLES:

1. prev -> Stores the previous node.
2. current -> Stores the current node.
3. next_node -> Temporarily stores the next node.

STEPS:

1. Initialize prev = None.
2. Set current = HEAD.
3. Store current.next in next_node.
4. Reverse the current node's NEXT reference.
5. Move prev to current.
6. Move current to next_node.
7. Repeat until current becomes None.
8. Update HEAD = prev.

CODE LOGIC:

prev = None
current = head

while current is not None:

    next_node = current.next

    current.next = prev

    prev = current

    current = next_node

head = prev

WHY DO WE USE THREE VARIABLES?

prev:
Remembers the node behind the current node.

current:
Points to the node being processed.

next_node:
Saves the remaining list before reversing the link.

IMPORTANT:
Always save current.next BEFORE changing current.next.
Otherwise, the remaining list may be lost.

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1) EXTRA SPACE

============================================================
                 COMPLETE LINKED LIST PROPERTIES
============================================================

14. TIME AND SPACE COMPLEXITY
-----------------------------

Let:
n = Number of nodes in the linked list.

OPERATION                  TIME COMPLEXITY

Insertion at beginning     O(1)
Insertion at end           O(n)
Insertion at position      O(n)
Insertion after a value    O(n)

Deletion at beginning      O(1)
Deletion at end            O(n)
Deletion at position       O(n)
Deletion by value          O(n)

Searching                  O(n)
Traversal / Display        O(n)
Counting nodes             O(n)
Reversing                   O(n)

SPACE COMPLEXITY:

O(n)

WHY?
- Each node stores data and a NEXT reference.
- Memory is allocated separately for every node.
- Total storage increases with the number of nodes.

NOTE:
If a TAIL reference is maintained, insertion at the end
can be performed in O(1) time.

15. ADVANTAGES OF SINGLY LINKED LIST
------------------------------------

- Dynamic memory allocation.
- Can grow and shrink during program execution.
- Insertion at the beginning takes O(1).
- Deletion at the beginning takes O(1).
- No shifting of elements is required.
- Does not require continuous memory locations.

16. DISADVANTAGES OF SINGLY LINKED LIST
---------------------------------------

- Cannot move backward.
- No direct index-based access.
- Searching takes O(n) time.
- Extra memory is required for NEXT references.
- Insertion and deletion at the end require traversal
  when no TAIL reference is maintained.
- Implementation is more complex than a basic array.

17. APPLICATIONS OF SINGLY LINKED LIST
--------------------------------------

- Implementing stacks.
- Implementing queues.
- Dynamic memory management.
- Hash table chaining.
- Graph adjacency lists.
- Maintaining dynamic collections.
- Music playlist navigation (forward-only).
- Representing polynomial expressions.

18. DIFFERENCE BETWEEN ARRAY AND LINKED LIST
--------------------------------------------

ARRAY:
- Elements are stored in indexed positions.
- Usually requires continuous memory.
- Supports direct access using indexes.
- Insertion/deletion in the middle may require shifting.
- Searching an unsorted array takes O(n).

LINKED LIST:
- Elements are stored in separate nodes.
- Nodes are connected using references.
- No direct indexing.
- Insertion/deletion can avoid shifting.
- Searching takes O(n).

============================================================
                    IMPORTANT EDGE CASES
============================================================

19. SPECIAL CONDITIONS TO HANDLE
--------------------------------

A. EMPTY LINKED LIST
--------------------
head = None

No node is present.

B. SINGLE NODE
--------------
HEAD -> 10 -> None

The first node is also the last node.

Deleting it makes:
head = None

C. INSERTING INTO AN EMPTY LIST
-------------------------------
If head is None:

head = new_node

D. DELETING FROM AN EMPTY LIST
------------------------------
No deletion is possible.

Display:
"List is Empty"

E. SEARCHING AN EMPTY LIST
--------------------------
The element cannot be found.

F. INVALID POSITION
-------------------
A position less than 1 or greater than n + 1 is invalid
for insertion.

For deletion, a position less than 1 or greater than n
is invalid.

G. VALUE NOT FOUND
------------------
If the searched value does not exist, do not modify the list.

============================================================
                    IMPORTANT EXAM POINTS
============================================================

1. A linked list is a LINEAR data structure.

2. A singly linked list contains DATA and NEXT.

3. HEAD points to the FIRST NODE.

4. The LAST NODE points to NONE.

5. Traversal is possible only in the FORWARD direction.

6. Insertion at beginning takes O(1).

7. Deletion at beginning takes O(1).

8. Searching takes O(n).

9. Insertion at the end takes O(n) without a TAIL reference.

10. Deletion at the end takes O(n).

11. temp = temp.next moves to the next node.

12. temp.next is None indicates the last node.

13. head = head.next removes the first node from the list.

14. temp.next = temp.next.next skips a node during deletion.

15. Reversing requires prev, current and next_node.

============================================================
                    QUICK REVISION
============================================================

LINKED LIST:
Linear data structure made of connected nodes.

NODE:
Contains DATA and NEXT.

HEAD:
Reference to the first node.

TAIL:
Reference to the last node.

NEXT:
Reference to the next node.

NONE:
Indicates the end of the list.

INSERTION:
Adding a new node.

DELETION:
Removing an existing node.

TRAVERSAL:
Visiting every node.

SEARCH:
Finding a particular value.

REVERSAL:
Changing the direction of NEXT references.

EMPTY LIST:
head = None

LAST NODE:
temp.next = None

INSERT AT BEGINNING:
new_node.next = head
head = new_node

INSERT AT END:
temp.next = new_node

DELETE AT BEGINNING:
head = head.next

DELETE AFTER A PREVIOUS NODE:
temp.next = temp.next.next

TRAVERSE:
temp = temp.next

REVERSE:
Use prev, current and next_node.

============================================================
                    REMEMBER THE LOGIC
============================================================

INSERTION:
Create Node -> Connect References -> Update HEAD if needed.

DELETION:
Find Node -> Change References -> Remove Node from Chain.

TRAVERSAL:
Start at HEAD -> Visit Data -> Move using NEXT -> Stop at None.

SEARCH:
Compare Data -> Move NEXT -> Repeat until Found or None.

REVERSAL:
Save NEXT -> Reverse Link -> Move Forward -> Update HEAD.

============================================================
"""


