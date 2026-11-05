"""
============================================================
                   DOUBLY LINKED LIST
============================================================

1. WHAT IS A DOUBLY LINKED LIST?
--------------------------------
A Doubly Linked List is a LINEAR, DYNAMIC data structure
in which elements are stored in separate units called NODES.

Each node contains THREE parts:

1. PREV -> Reference to the PREVIOUS node.
2. DATA -> Stores the actual value.
3. NEXT -> Reference to the NEXT node.

Unlike a Singly Linked List, where traversal is possible
only in the forward direction, a Doubly Linked List allows
traversal in BOTH FORWARD and BACKWARD directions.

MAIN IDEA:
Every node is connected to both its previous and next nodes.

EXAMPLE:

              FORWARD DIRECTION ----->

HEAD
 |
 v
None <- [10] <-> [20] <-> [30] -> None
                              ^
                              |
                             TAIL

              <----- BACKWARD DIRECTION

Here:
- HEAD points to the first node.
- TAIL points to the last node.
- PREV points to the previous node.
- NEXT points to the next node.
- None indicates the absence of a previous or next node.

2. NODE STRUCTURE
-----------------

Every node contains THREE parts:

+----------+------+----------+
|   PREV   | DATA |   NEXT   |
+----------+------+----------+

PREV:
Stores the reference to the previous node.

DATA:
Stores the actual value.

NEXT:
Stores the reference to the next node.

EXAMPLE:

None <- [10] <-> [20] <-> [30] -> None

For Node 20:
PREV = Reference to Node 10
DATA = 20
NEXT = Reference to Node 30

IMPORTANT:
- The first node's PREV is None.
- The last node's NEXT is None.
- Every connection must be updated in BOTH directions.

3. WHY DO WE NEED A DOUBLY LINKED LIST?
---------------------------------------

In a SINGLY LINKED LIST:
- Every node contains DATA and NEXT.
- Traversal is possible only in the forward direction.
- Moving backward is not directly possible.
- Deleting a node generally requires knowing its previous node.

In a DOUBLY LINKED LIST:
- Every node contains PREV, DATA and NEXT.
- Traversal is possible in both directions.
- Moving backward is possible.
- Deletion of a known node is easier because its previous
  reference is already available.

IMPORTANT:
A Doubly Linked List requires extra memory because
every node stores TWO references.

4. IMPORTANT TERMINOLOGIES
--------------------------

A. NODE
-------
An individual unit that stores data and references.

B. HEAD
-------
HEAD is a reference to the FIRST NODE.

Example:

HEAD -> 10 <-> 20 <-> 30

If the list is empty:

HEAD = None

C. TAIL
-------
TAIL is a reference to the LAST NODE.

It helps in:
- Insertion at the end.
- Deletion at the end.
- Backward traversal.

D. PREV
-------
Stores the reference to the previous node.

Example:
node.next.prev = node

E. NEXT
-------
Stores the reference to the next node.

Example:
node.prev.next = node

F. NONE
-------
Indicates that there is no previous or next node.

The first node has PREV = None.
The last node has NEXT = None.

5. REPRESENTATION OF DOUBLY LINKED LIST
---------------------------------------

EXAMPLE:

HEAD
 |
 v
None <- [10] <-> [20] <-> [30] -> None
                              ^
                              |
                             TAIL

Node 10:
PREV = None
DATA = 10
NEXT = Node 20

Node 20:
PREV = Node 10
DATA = 20
NEXT = Node 30

Node 30:
PREV = Node 20
DATA = 30
NEXT = None

IMPORTANT:
Every connection must be maintained in both directions.

If Node A is connected to Node B:

A.next = B
B.prev = A

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
        self.prev = None
        self.next = None

EXPLANATION:

- class Node:
  Creates a blueprint for a node.

- __init__():
  Constructor called whenever a new node is created.

- self.data = data:
  Stores the value.

- self.prev = None:
  Initially, there is no previous node.

- self.next = None:
  Initially, there is no next node.

CREATING A NODE:

node1 = Node(10)

node1.data -> 10
node1.prev -> None
node1.next -> None

7. INITIALIZATION OF DOUBLY LINKED LIST
---------------------------------------

Initially, the linked list is EMPTY.

head = None
tail = None

Here:
- HEAD does not point to any node.
- TAIL does not point to any node.
- The list contains zero elements.

When the first node is inserted:

new_node = Node(10)

head = new_node
tail = new_node

RESULT:

HEAD = TAIL
    |
    v
None <- [10] -> None

IMPORTANT:
When only ONE node exists, HEAD and TAIL point to
the SAME node.

============================================================
                   INSERTION OPERATIONS
============================================================

8. INSERTION IN DOUBLY LINKED LIST
----------------------------------

Insertion means adding a new node to the linked list.

COMMON TYPES:

1. Insertion at the Beginning.
2. Insertion at the End.
3. Insertion at a Specific Position.
4. Insertion After a Particular Node.
5. Insertion Before a Particular Node.

------------------------------------------------------------
A. INSERTION AT THE BEGINNING
------------------------------------------------------------

A new node is inserted BEFORE the current HEAD.

BEFORE:

HEAD
 |
 v
None <- [10] <-> [20] <-> [30] -> None

Insert 5.

STEPS:

1. Create a new node.
2. Check whether the list is empty.
3. Make the new node's NEXT point to the current HEAD.
4. Make the current HEAD's PREV point to the new node.
5. Update HEAD to the new node.
6. If the list was empty, update TAIL as well.

CODE LOGIC:

new_node = Node(5)

if head is None:
    head = tail = new_node

else:
    new_node.next = head
    head.prev = new_node
    head = new_node

AFTER:

HEAD
 |
 v
None <- [5] <-> [10] <-> [20] <-> [30] -> None

IMPORTANT:
Both references must be updated:

new_node.next = head
head.prev = new_node

TIME COMPLEXITY: O(1)

------------------------------------------------------------
B. INSERTION AT THE END
------------------------------------------------------------

A new node is inserted AFTER the current TAIL.

BEFORE:

None <- [10] <-> [20] <-> [30] -> None
                              ^
                              |
                             TAIL

Insert 40.

STEPS:

1. Create a new node.
2. Check whether the list is empty.
3. Make the new node's PREV point to the current TAIL.
4. Make the current TAIL's NEXT point to the new node.
5. Update TAIL to the new node.

CODE LOGIC:

new_node = Node(40)

if head is None:
    head = tail = new_node

else:
    new_node.prev = tail
    tail.next = new_node
    tail = new_node

AFTER:

None <- [10] <-> [20] <-> [30] <-> [40] -> None
                                        ^
                                        |
                                       TAIL

IMPORTANT:
Because we maintain a TAIL reference, we do not need
to traverse the entire list.

TIME COMPLEXITY: O(1)

------------------------------------------------------------
C. INSERTION AT A SPECIFIC POSITION
------------------------------------------------------------

A new node is inserted at a particular position.

For this implementation, positions start from 1.

BEFORE:

HEAD -> 10 <-> 20 <-> 30 <-> 40

Insert 15 at Position 2.

STEPS:

1. Create a new node.
2. If position is 1, perform insertion at the beginning.
3. Otherwise, traverse to the node at position - 1.
4. Connect the new node to the next node.
5. Connect the previous node to the new node.
6. Update both PREV and NEXT references.

CODE LOGIC:

new_node = Node(15)

temp = head

for i in range(position - 2):
    temp = temp.next

new_node.next = temp.next
new_node.prev = temp

temp.next.prev = new_node
temp.next = new_node

AFTER:

HEAD -> 10 <-> 15 <-> 20 <-> 30 <-> 40

IMPORTANT:
The four reference updates are important:

new_node.next = temp.next
new_node.prev = temp
temp.next.prev = new_node
temp.next = new_node

If inserting at the END, update TAIL instead of accessing
temp.next.prev.

TIME COMPLEXITY: O(n)

------------------------------------------------------------
D. INSERTION AFTER A PARTICULAR VALUE
------------------------------------------------------------

A new node is inserted AFTER a node containing a given value.

BEFORE:

HEAD -> 10 <-> 20 <-> 30 <-> 40

Insert 25 after 20.

STEPS:

1. Start from HEAD.
2. Search for the node containing 20.
3. Create a new node containing 25.
4. Make the new node's NEXT point to the next node.
5. Make the new node's PREV point to the current node.
6. Update the next node's PREV.
7. Update the current node's NEXT.
8. If inserting after TAIL, update TAIL.

CODE LOGIC:

new_node = Node(25)

temp = head

while temp is not None and temp.data != 20:
    temp = temp.next

if temp is not None:

    new_node.next = temp.next
    new_node.prev = temp

    if temp.next is not None:
        temp.next.prev = new_node
    else:
        tail = new_node

    temp.next = new_node

AFTER:

HEAD -> 10 <-> 20 <-> 25 <-> 30 <-> 40

TIME COMPLEXITY: O(n)

------------------------------------------------------------
E. INSERTION BEFORE A PARTICULAR VALUE
------------------------------------------------------------

A new node is inserted BEFORE a node containing a
particular value.

BEFORE:

HEAD -> 10 <-> 20 <-> 30 <-> 40

Insert 15 before 20.

STEPS:

1. Start from HEAD.
2. Search for the node containing 20.
3. Create a new node containing 15.
4. Make the new node's NEXT point to the current node.
5. Make the new node's PREV point to the previous node.
6. Update the previous node's NEXT.
7. Update the current node's PREV.
8. If inserting before HEAD, update HEAD.

CODE LOGIC:

new_node = Node(15)

temp = head

while temp is not None and temp.data != 20:
    temp = temp.next

if temp is not None:

    new_node.next = temp
    new_node.prev = temp.prev

    if temp.prev is not None:
        temp.prev.next = new_node
    else:
        head = new_node

    temp.prev = new_node

AFTER:

HEAD -> 10 <-> 15 <-> 20 <-> 30 <-> 40

TIME COMPLEXITY: O(n)

============================================================
                    DELETION OPERATIONS
============================================================

9. DELETION IN DOUBLY LINKED LIST
---------------------------------

Deletion means removing a node from the linked list.

COMMON TYPES:

1. Deletion at the Beginning.
2. Deletion at the End.
3. Deletion at a Specific Position.
4. Deletion of a Particular Value.

------------------------------------------------------------
A. DELETION AT THE BEGINNING
------------------------------------------------------------

The first node (HEAD) is removed.

BEFORE:

HEAD -> 10 <-> 20 <-> 30 -> None

STEPS:

1. Check whether the list is empty.
2. If only one node exists, set HEAD = TAIL = None.
3. Otherwise, move HEAD to the next node.
4. Set the new HEAD's PREV to None.

CODE LOGIC:

if head is None:
    pass

elif head == tail:
    head = tail = None

else:
    head = head.next
    head.prev = None

AFTER:

HEAD -> 20 <-> 30 -> None

IMPORTANT:
After updating HEAD, the new first node must have:

head.prev = None

TIME COMPLEXITY: O(1)

------------------------------------------------------------
B. DELETION AT THE END
------------------------------------------------------------

The last node (TAIL) is removed.

BEFORE:

None <- [10] <-> [20] <-> [30]
                              ^
                              |
                             TAIL

STEPS:

1. Check whether the list is empty.
2. If only one node exists, set HEAD = TAIL = None.
3. Otherwise, move TAIL to the previous node.
4. Set the new TAIL's NEXT to None.

CODE LOGIC:

if head is None:
    pass

elif head == tail:
    head = tail = None

else:
    tail = tail.prev
    tail.next = None

AFTER:

None <- [10] <-> [20] -> None
                 ^
                 |
                TAIL

IMPORTANT:
Because we have a TAIL reference, deletion at the end
does not require traversal.

TIME COMPLEXITY: O(1)

------------------------------------------------------------
C. DELETION AT A SPECIFIC POSITION
------------------------------------------------------------

Removes the node present at a particular position.

Positions start from 1.

BEFORE:

HEAD -> 10 <-> 20 <-> 30 <-> 40

Delete Position 2.

STEPS:

1. Check whether the list is empty.
2. Find the node at the required position.
3. Store its previous and next references.
4. Connect the previous node to the next node.
5. Connect the next node to the previous node.
6. Update HEAD or TAIL if the deleted node is at an end.

CODE LOGIC:

temp = head

for i in range(position - 1):
    temp = temp.next

if temp.prev is not None:
    temp.prev.next = temp.next
else:
    head = temp.next

if temp.next is not None:
    temp.next.prev = temp.prev
else:
    tail = temp.prev

AFTER:

HEAD -> 10 <-> 30 <-> 40

IMPORTANT:
The two main operations are:

temp.prev.next = temp.next
temp.next.prev = temp.prev

These connect the previous and next nodes directly.

TIME COMPLEXITY: O(n)

------------------------------------------------------------
D. DELETION OF A PARTICULAR VALUE
------------------------------------------------------------

Removes the FIRST node containing a particular value.

BEFORE:

HEAD -> 10 <-> 20 <-> 30 <-> 40

Delete value 30.

STEPS:

1. Check whether the list is empty.
2. Start from HEAD.
3. Search for the required value.
4. If found, connect its previous node to its next node.
5. Update HEAD or TAIL if necessary.

CODE LOGIC:

temp = head

while temp is not None and temp.data != 30:
    temp = temp.next

if temp is not None:

    if temp.prev is not None:
        temp.prev.next = temp.next
    else:
        head = temp.next

    if temp.next is not None:
        temp.next.prev = temp.prev
    else:
        tail = temp.prev

AFTER:

HEAD -> 10 <-> 20 <-> 40

IMPORTANT:
If the node is at the beginning, update HEAD.

If the node is at the end, update TAIL.

If the node is in the middle, connect its neighbours.

TIME COMPLEXITY: O(n)

============================================================
                TRAVERSAL AND SEARCHING
============================================================

10. FORWARD TRAVERSAL
---------------------

Forward traversal means visiting every node from HEAD
to TAIL.

EXAMPLE:

HEAD -> 10 <-> 20 <-> 30 -> None

STEPS:

1. Start from HEAD.
2. Print the current node's DATA.
3. Move to the next node using NEXT.
4. Continue until the current node becomes None.

CODE LOGIC:

temp = head

while temp is not None:
    print(temp.data)
    temp = temp.next

OUTPUT:

10
20
30

TIME COMPLEXITY: O(n)

11. BACKWARD TRAVERSAL
----------------------

Backward traversal means visiting every node from TAIL
to HEAD.

EXAMPLE:

None <- 10 <-> 20 <-> 30 <- TAIL

STEPS:

1. Start from TAIL.
2. Print the current node's DATA.
3. Move to the previous node using PREV.
4. Continue until the current node becomes None.

CODE LOGIC:

temp = tail

while temp is not None:
    print(temp.data)
    temp = temp.prev

OUTPUT:

30
20
10

TIME COMPLEXITY: O(n)

IMPORTANT:
Backward traversal is possible because each node stores
a PREV reference.

12. SEARCHING
-------------

Searching means finding whether a particular value exists
in the linked list.

EXAMPLE:

HEAD -> 10 <-> 20 <-> 30 <-> 40

Search for 30.

STEPS:

1. Start from HEAD.
2. Compare the current node's DATA with the target.
3. If equal, the element is FOUND.
4. Otherwise, move to the next node.
5. Continue until the value is found or None is reached.

CODE LOGIC:

temp = head

while temp is not None:

    if temp.data == key:
        print("Element Found")
        break

    temp = temp.next

if temp is None:
    print("Element Not Found")

TIME COMPLEXITY:

Best Case: O(1)
Worst Case: O(n)

13. COUNTING THE NUMBER OF NODES
--------------------------------

Counts the total number of nodes.

CODE LOGIC:

count = 0
temp = head

while temp is not None:
    count += 1
    temp = temp.next

print(count)

EXAMPLE:

HEAD -> 10 <-> 20 <-> 30

OUTPUT:
3

TIME COMPLEXITY: O(n)

14. REVERSING A DOUBLY LINKED LIST
----------------------------------

Reversing means changing the PREV and NEXT references
of every node so that the list is reversed.

BEFORE:

HEAD -> 10 <-> 20 <-> 30 <-> 40 <- TAIL

AFTER:

HEAD -> 40 <-> 30 <-> 20 <-> 10 <- TAIL

STEPS:

1. Start from HEAD.
2. Store the current node's NEXT reference.
3. Swap the PREV and NEXT references.
4. Move to the original NEXT node.
5. Repeat until every node has been processed.
6. Swap HEAD and TAIL.

CODE LOGIC:

current = head

while current is not None:

    next_node = current.next

    current.next = current.prev
    current.prev = next_node

    current = next_node

head, tail = tail, head

IMPORTANT VARIABLES:

current:
The node currently being processed.

next_node:
Stores the original next node before swapping references.

WHY DO WE STORE next_node FIRST?
Because after swapping PREV and NEXT, the original
next reference would otherwise be lost.

IMPORTANT:
Both PREV and NEXT references must be reversed.

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)

============================================================
                  ADDITIONAL OPERATIONS
============================================================

15. FINDING THE FIRST NODE
--------------------------

head.data

The HEAD reference directly accesses the first node.

16. FINDING THE LAST NODE
-------------------------

tail.data

The TAIL reference directly accesses the last node.

17. CHECKING WHETHER THE LIST IS EMPTY
--------------------------------------

if head is None:
    print("List is Empty")

18. DISPLAYING BOTH DIRECTIONS
------------------------------

FORWARD:

temp = head

while temp is not None:
    print(temp.data)
    temp = temp.next

BACKWARD:

temp = tail

while temp is not None:
    print(temp.data)
    temp = temp.prev

============================================================
                  IMPORTANT EDGE CASES
============================================================

19. SPECIAL CONDITIONS TO HANDLE
--------------------------------

A. EMPTY LINKED LIST
--------------------
head = None
tail = None

No node is present.

B. SINGLE NODE
--------------
HEAD = TAIL

None <- [10] -> None

Deleting this node makes:

head = None
tail = None

C. INSERTING INTO AN EMPTY LIST
-------------------------------

head = tail = new_node

D. DELETING FROM AN EMPTY LIST
------------------------------

No deletion is possible.

Display:
"List is Empty"

E. DELETING THE FIRST NODE
--------------------------
Update HEAD and set:

head.prev = None

F. DELETING THE LAST NODE
-------------------------
Update TAIL and set:

tail.next = None

G. INSERTING BEFORE HEAD
------------------------
Update HEAD to the new node.

H. INSERTING AFTER TAIL
-----------------------
Update TAIL to the new node.

I. DELETING A VALUE NOT FOUND
-----------------------------
Do not modify the list.

J. INVALID POSITION
-------------------
Insertion:
Valid positions are 1 to n + 1.

Deletion:
Valid positions are 1 to n.

============================================================
                 TIME AND SPACE COMPLEXITY
============================================================

20. TIME COMPLEXITY
-------------------

Let:
n = Number of nodes.

Assume both HEAD and TAIL references are maintained.

OPERATION                       TIME COMPLEXITY

Insertion at beginning          O(1)
Insertion at end                 O(1)
Insertion at position            O(n)
Insertion after a given value    O(n)
Insertion before a given value   O(n)

Deletion at beginning            O(1)
Deletion at end                  O(1)
Deletion at position             O(n)
Deletion by value                O(n)

Forward traversal                O(n)
Backward traversal               O(n)
Searching                        O(n)
Counting nodes                   O(n)
Reversing                        O(n)

IMPORTANT:
Insertion or deletion of a NODE ALREADY KNOWN by reference
can take O(1) time, provided the required list references
are available.

Searching for that node by its VALUE still takes O(n).

21. SPACE COMPLEXITY
--------------------

O(n)

WHY?
- Each node stores DATA.
- Each node stores PREV.
- Each node stores NEXT.
- Additional memory is required for the two references.

A Doubly Linked List uses more memory per node than a
Singly Linked List.

============================================================
                 ADVANTAGES AND DISADVANTAGES
============================================================

22. ADVANTAGES
--------------

- Traversal is possible in both directions.
- Insertion at the beginning takes O(1).
- Insertion at the end takes O(1) with a TAIL reference.
- Deletion at the end takes O(1) with a TAIL reference.
- A known node can be deleted without searching for
  its previous node.
- Useful for implementing deques.
- Easy to move backward and forward.

23. DISADVANTAGES
-----------------

- Requires extra memory for PREV references.
- Every insertion requires more pointer updates.
- Every deletion requires more pointer updates.
- Implementation is more complex than a Singly Linked List.
- Searching still takes O(n).
- No direct index-based access.

============================================================
                 APPLICATIONS
============================================================

24. APPLICATIONS OF DOUBLY LINKED LIST
--------------------------------------

- Browser Backward and Forward Navigation.
- Undo and Redo Operations.
- Music and Video Playlists.
- Image Galleries.
- Implementing Deque.
- LRU Cache.
- Memory Management.
- Navigation between records.
- Operating System Process Management.

============================================================
          SINGLY VS DOUBLY LINKED LIST
============================================================

25. DIFFERENCE BETWEEN SINGLY AND DOUBLY LINKED LIST
----------------------------------------------------

SINGLY LINKED LIST:

- Contains DATA and NEXT.
- Traversal is only FORWARD.
- Requires less memory.
- Cannot directly move backward.
- Deletion usually requires access to the previous node.

DOUBLY LINKED LIST:

- Contains PREV, DATA and NEXT.
- Traversal is FORWARD and BACKWARD.
- Requires more memory.
- Can directly move backward.
- Easier deletion when the node reference is known.

============================================================
                    IMPORTANT EXAM POINTS
============================================================

1. A Doubly Linked List is a LINEAR data structure.

2. Each node contains PREV, DATA and NEXT.

3. HEAD points to the FIRST NODE.

4. TAIL points to the LAST NODE.

5. The first node has PREV = None.

6. The last node has NEXT = None.

7. Traversal is possible in BOTH directions.

8. Insertion at beginning takes O(1).

9. Insertion at end takes O(1) with a TAIL reference.

10. Deletion at beginning takes O(1).

11. Deletion at end takes O(1) with a TAIL reference.

12. Searching takes O(n).

13. Every connection requires updating BOTH references.

14. A known node can be deleted in O(1) time if its
    neighbouring references are available.

15. Reversing requires swapping PREV and NEXT.

============================================================
                    QUICK REVISION
============================================================

DOUBLY LINKED LIST:
Linear data structure with two references per node.

NODE:
Contains PREV, DATA and NEXT.

HEAD:
Reference to the first node.

TAIL:
Reference to the last node.

PREV:
Reference to the previous node.

NEXT:
Reference to the next node.

INSERT AT BEGINNING:
new_node.next = head
head.prev = new_node
head = new_node

INSERT AT END:
new_node.prev = tail
tail.next = new_node
tail = new_node

DELETE AT BEGINNING:
head = head.next
head.prev = None

DELETE AT END:
tail = tail.prev
tail.next = None

FORWARD TRAVERSAL:
temp = temp.next

BACKWARD TRAVERSAL:
temp = temp.prev

REVERSE:
Swap PREV and NEXT for every node.
Swap HEAD and TAIL.

EMPTY LIST:
head = None
tail = None

SINGLE NODE:
head = tail

============================================================
                    REMEMBER THE LOGIC
============================================================

INSERTION:
Create Node -> Connect PREV and NEXT -> Update HEAD/TAIL.

DELETION:
Find Node -> Connect Previous and Next Nodes -> Update
HEAD/TAIL if an end node is deleted.

FORWARD TRAVERSAL:
HEAD -> NEXT -> NEXT -> TAIL

BACKWARD TRAVERSAL:
TAIL -> PREV -> PREV -> HEAD

REVERSAL:
Swap PREV and NEXT -> Swap HEAD and TAIL.

============================================================

MOST IMPORTANT CONCEPT:

In a DOUBLY LINKED LIST, every connection must be
maintained in BOTH directions.

If Node A is connected to Node B:

A.next = B
B.prev = A

If you update only one reference, the linked list
may become disconnected or inconsistent.

============================================================
"""


class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def insertionEnd(self, data):
        newNode = Node(data)
        
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp

    def display(self):
            temp = self.head
            while temp.next != None:
                print(temp.data, end = "->")
                temp = temp.next
            print(temp.data)

    def insertionBegingin(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def insertionMiddle(self, data, k):
        newNode = Node(data)
        temp  = self.head
        for i in range(k-1):
            temp = temp.next
        newNode.next = temp.next
        temp.next.prev = newNode
        temp.next = newNode
        newNode.prev = temp

    def deletion(self, x):
        temp = self.head
        while temp.data != x:
            temp = temp.next
        temp.prev.next = temp.next
        temp.next.prev = temp.prev

     

        


