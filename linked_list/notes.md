# LINKED LISTS IN DATA STRUCTURES AND ALGORITHMS (DSA)

# Complete Notes: Singly, Doubly and Circular Linked Lists (Python)

---

# TABLE OF CONTENTS

1. Introduction to Linked Lists
2. Understanding Nodes and Pointers
3. Linked List vs Array
4. Basic Terminology
5. Singly Linked List (SLL)
   - Structure and Working
   - Traversal and Display
   - Insertion
   - Deletion
   - Searching
   - Complete Python Implementation
6. Doubly Linked List (DLL)
   - Structure and Working
   - Forward and Backward Traversal
   - Insertion
   - Deletion
   - Searching
   - Complete Python Implementation
7. Circular Linked List (CLL)
   - Singly Circular Linked List
   - Structure and Working
   - Insertion
   - Deletion
   - Searching
   - Complete Python Implementation
8. Doubly Circular Linked List
   - Structure and Working
   - Insertion
   - Deletion
   - Searching
   - Complete Python Implementation
9. Time and Space Complexity
10. Comparison of Linked Lists
11. Common Mistakes and Edge Cases
12. Applications of Linked Lists
13. Important DSA Interview and Examination Questions
14. Quick Revision Sheet

---

# 1. INTRODUCTION TO LINKED LISTS

## 1.1 What is a Linked List?

A Linked List is a linear data structure in which elements are stored in separate objects called **Nodes**.

Unlike arrays, linked list elements are not required to occupy consecutive memory locations.

Each node contains:

1. Data: The actual value stored in the node.
2. Link/Pointer: A reference to another node.

A linked list connects nodes using these references.

### Example

Suppose we want to store:

`10, 20, 30, 40`

A linked list looks like:

```text
HEAD
 |
 v
[10 | •] ---> [20 | •] ---> [30 | •] ---> [40 | None]
                                                   |
                                                  NULL
```

Here:

- `10, 20, 30, 40` are data values.
- Each arrow represents a link to the next node.
- `HEAD` stores the reference to the first node.
- `None` indicates that there is no next node.

## 1.2 Why Do We Need Linked Lists?

Arrays have some limitations.

For example:

Suppose we have an array:

```python
arr = [10, 20, 30, 40, 50]
```

If we want to insert `25` between `20` and `30`, we generally need to shift the subsequent elements.

```text
Before:

[10, 20, 30, 40, 50]

After:

[10, 20, 25, 30, 40, 50]
```

This shifting takes O(n) time in the worst case.

Linked lists solve this problem differently.

We can create a new node and modify references.

```text
Before:

10 ---> 20 ---> 30 ---> 40

After:

10 ---> 20 ---> 25 ---> 30 ---> 40
```

Only a few links need to be modified.

However, linked lists also have disadvantages, such as slower random access.

## 1.3 Important Characteristics

- Dynamic size: A linked list can grow or shrink during program execution.
- Non-contiguous memory: Nodes do not need to be stored next to each other.
- Sequential access: We generally access elements by traversing from the beginning.
- Dynamic memory allocation: New nodes are created when required.
- Efficient insertion/deletion: Once the relevant node or position is known, links can be modified efficiently.

---

# 2. UNDERSTANDING NODES AND POINTERS

This is the most important foundation of linked lists.

Before learning insertion and deletion, understand how nodes work.

## 2.1 What is a Node?

A Node is an individual unit of a linked list.

In a singly linked list, a node contains:

```text
+----------+----------+
|   DATA   |   NEXT   |
+----------+----------+
```

Example:

```text
+----------+----------+
|    10    |  Address |
+----------+----------+
```

The `NEXT` field stores a reference to the next node.

## 2.2 Creating a Node in Python

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

Explanation:

- `class Node`: Defines a node.
- `__init__`: Constructor called when a new node is created.
- `self.data`: Stores the value.
- `self.next`: Stores the reference to the next node.
- `None`: Initially, the node does not point to another node.

Creating a node:

```python
new_node = Node(10)

print(new_node.data)  # 10
print(new_node.next)  # None
```

head.info = access the current block

head.next = access the next block

## 2.3 What is a Pointer?

In languages such as C and C++, pointers store memory addresses.

Python handles this differently.

Python variables store references to objects.

For example:

```python
a = Node(10)
b = Node(20)

a.next = b
```

Now:

```text
a
|
v
[10 | •] ------> [20 | None]
                   ^
                   |
                   b
```

`a.next = b` means that the next reference of node `a` points to the node referenced by `b`.

**Important:** In Python, we use object references instead of manually manipulating memory addresses.

## 2.4 What is HEAD?

`head` is a reference to the first node of a linked list.

Example:

```text
head
 |
 v
[10] ---> [20] ---> [30] ---> None
```

If we lose the reference to `head` and have no other references to the nodes, we can lose access to the entire list.

## 2.5 What is TAIL?

`tail` is a reference to the last node of a linked list.

```text
head                              tail
 |                                  |
 v                                  v
[10] ---> [20] ---> [30] ---> [40 | None]
```

Maintaining a tail reference allows us to insert elements at the end in O(1) time in a singly linked list.

---

# 3. LINKED LIST VS ARRAY

| Feature                | Array                             | Linked List            |
| ---------------------- | --------------------------------- | ---------------------- |
| Memory allocation      | Usually contiguous                | Non-contiguous         |
| Size                   | Often fixed in traditional arrays | Dynamic                |
| Access by index        | O(1)                              | O(n)                   |
| Searching              | O(n)                              | O(n)                   |
| Insertion at beginning | O(n)                              | O(1)                   |
| Insertion at end       | O(1) amortized for dynamic arrays | O(1) with tail         |
| Deletion at beginning  | O(n)                              | O(1)                   |
| Memory usage           | Less overhead                     | Extra memory for links |
| Cache performance      | Generally better                  | Generally poorer       |

Note: Python lists are dynamic arrays, not linked lists.

---

# 4. BASIC TERMINOLOGY

| Term            | Meaning                                         |
| --------------- | ----------------------------------------------- |
| Node            | Individual element of a linked list             |
| Data            | Value stored inside a node                      |
| Next            | Reference to the next node                      |
| Previous (prev) | Reference to the previous node                  |
| Head            | Reference to the first node                     |
| Tail            | Reference to the last node                      |
| NULL / None     | Indicates absence of a reference                |
| Traversal       | Visiting nodes one by one                       |
| Insertion       | Adding a new node                               |
| Deletion        | Removing an existing node                       |
| Searching       | Finding a particular value                      |
| Circular link   | Link connecting the last node back to the first |

---

# 5. SINGLY LINKED LIST (SLL)

## 5.1 What is a Singly Linked List?

A Singly Linked List is a linked list in which each node contains:

1. Data
2. A reference to the next node

Each node points only in the forward direction.

### Structure

```text
HEAD
 |
 v
[10 | •] ---> [20 | •] ---> [30 | •] ---> [40 | None]
```

The last node points to `None`.

### Node Structure

```text
+------+------+
| DATA | NEXT |
+------+------+
```

### Python Node Class

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

## 5.2 Traversal in Singly Linked List

Traversal means visiting every node one by one.

We start from `head` and move using `next`.

### Algorithm

1. Check whether the list is empty.
2. Create a temporary reference pointing to head.
3. Process the current node.
4. Move to the next node.
5. Repeat until the current node becomes None.

### Python Code

```python
def display(self):
    current = self.head

    while current.next != None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")
```

### Dry Run

List:

```text
10 -> 20 -> 30 -> None
```

| Iteration | Current | Output |
| --------- | ------- | ------ |
| 1         | 10      | 10     |
| 2         | 20      | 20     |
| 3         | 30      | 30     |
| 4         | None    | Stop   |

Output:

```text
10 -> 20 -> 30 -> None
```

Time Complexity: O(n)

Space Complexity: O(1)

---

# 5.3 INSERTION IN SINGLY LINKED LIST

Insertion means adding a new node to the linked list.

There are four important insertion operations:

1. Insertion at the beginning.
2. Insertion at the end.
3. Insertion at a specific position.
4. Insertion after a particular value/node.

## A. Insertion at the Beginning

Suppose the linked list is:

```text
HEAD
 |
 v
10 ---> 20 ---> 30 ---> None
```

We want to insert `5`.

### Steps

1. Create a new node.
2. Make the new node point to the current head.
3. Update head to the new node.

### Diagram

Before:

```text
HEAD
 |
 v
10 ---> 20 ---> 30 ---> None
```

After:

```text
HEAD
 |
 v
5 ---> 10 ---> 20 ---> 30 ---> None
```

### Python Code

```python
def insert_at_beginning(self, data):

    new_node = Node(data)

    new_node.next = self.head

    self.head = new_node
```

### Understanding the Most Important Line

```python
new_node.next = self.head
```

This connects the new node to the existing first node.

```python
self.head = new_node
```

This makes the new node the first node.

Time Complexity: O(1)

---

## B. Insertion at the End

Suppose:

```text
10 ---> 20 ---> 30 ---> None
```

We want to insert `40`.

### Steps

1. Create a new node.
2. Check whether the list is empty.
3. If empty, make the new node the head.
4. Otherwise, traverse to the last node.
5. Make the last node point to the new node.

### Diagram

Before:

```text
10 ---> 20 ---> 30 ---> None
```

After:

```text
10 ---> 20 ---> 30 ---> 40 ---> None
```

### Python Code

```python
def insert_at_end(self, data):

    new_node = Node(data)

    if self.head is None:
        self.head = new_node
        return

    current = self.head

    while current.next is not None:
        current = current.next

    current.next = new_node
```

### Why do we use `current.next is not None`?

We need to reach the last node.

The last node has:

```python
current.next = None
```

Therefore, we stop when `current.next` becomes None.

Time Complexity: O(n) without a tail reference.

---

## C. Insertion at a Specific Position

Suppose:

```text
10 ---> 20 ---> 40 ---> None
```

We want to insert `30` at position 3.

Assume positions start from 1.

### Steps

1. Check whether the position is valid.
2. If position is 1, insert at the beginning.
3. Otherwise, reach the node at position `position - 1`.
4. Create a new node.
5. Connect the new node to the next node.
6. Connect the previous node to the new node.

### Diagram

Before:

```text
10 ---> 20 ---> 40 ---> None
```

After:

```text
10 ---> 20 ---> 30 ---> 40 ---> None
```

### Python Code

```python
def insert_at_position(self, data, position):

    if position < 1:
        print("Invalid position")
        return

    if position == 1:
        self.insert_at_beginning(data)
        return

    current = self.head

    for _ in range(position - 2):

        if current is None:
            print("Position out of range")
            return

        current = current.next

    if current is None:
        print("Position out of range")
        return

    new_node = Node(data)

    new_node.next = current.next

    current.next = new_node
```

### Why `position - 2`?

Suppose we insert at position 3.

We need to reach position 2 because the new node must be connected after position 2.

For example:

```text
Position:  1       2       3
           |       |       |
           v       v       v
          [10] -> [20] -> [40]
```

We stop at node 2.

Then:

```python
new_node.next = current.next
current.next = new_node
```

Time Complexity: O(n)

---

## D. Insertion After a Particular Value

Suppose:

```text
10 ---> 20 ---> 40 ---> None
```

Insert `30` after `20`.

### Python Code

```python
def insert_after_value(self, target, data):

    current = self.head

    while current is not None:

        if current.data == target:

            new_node = Node(data)

            new_node.next = current.next

            current.next = new_node

            return

        current = current.next

    print("Target not found")
```

Time Complexity: O(n)

---

# 5.4 DELETION IN SINGLY LINKED LIST

Deletion means removing a node from the linked list.

Important operations:

1. Delete from the beginning.
2. Delete from the end.
3. Delete from a specific position.
4. Delete a node containing a particular value.

## A. Deletion from the Beginning

Suppose:

```text
HEAD
 |
 v
10 ---> 20 ---> 30 ---> None
```

We want to delete `10`.

### Steps

1. Check whether the list is empty.
2. Move head to the next node.

### Diagram

Before:

```text
HEAD
 |
 v
10 ---> 20 ---> 30 ---> None
```

After:

```text
HEAD
 |
 v
20 ---> 30 ---> None
```

### Python Code

```python
def delete_from_beginning(self):

    if self.head is None:
        print("List is empty")
        return

    self.head = self.head.next
```

### Important Concept

```python
self.head = self.head.next
```

This changes the head reference.

The old first node is no longer reachable through the list.

Python's garbage collector can reclaim it when no references remain.

Time Complexity: O(1)

---

## B. Deletion from the End

Suppose:

```text
10 ---> 20 ---> 30 ---> None
```

We want to delete `30`.

### Steps

1. Check whether the list is empty.
2. If there is only one node, set head to None.
3. Otherwise, traverse to the second-last node.
4. Set its next reference to None.

### Diagram

Before:

```text
10 ---> 20 ---> 30 ---> None
```

After:

```text
10 ---> 20 ---> None
```

### Python Code

```python
def delete_from_end(self):

    if self.head is None:
        print("List is empty")
        return

    if self.head.next is None:
        self.head = None
        return

    current = self.head

    while current.next.next is not None:
        current = current.next

    current.next = None
```

### Why `current.next.next`?

We want to stop at the second-last node.

Suppose:

```text
10 ---> 20 ---> 30 ---> None
```

At node 20:

```python
current.next = node 30
current.next.next = None
```

Therefore, the loop stops at 20.

Then:

```python
current.next = None
```

This removes the connection to 30.

Time Complexity: O(n)

---

## C. Deletion from a Specific Position

Suppose:

```text
10 ---> 20 ---> 30 ---> 40 ---> None
```

Delete position 3.

### Steps

1. Check whether the position is valid.
2. If position is 1, delete the first node.
3. Otherwise, reach the node immediately before the target.
4. Change its next reference to the target's next reference.

### Diagram

Before:

```text
10 ---> 20 ---> 30 ---> 40 ---> None
```

After:

```text
10 ---> 20 ------------> 40 ---> None
```

### Python Code

```python
def delete_at_position(self, position):

    if position < 1:
        print("Invalid position")
        return

    if self.head is None:
        print("List is empty")
        return

    if position == 1:
        self.delete_from_beginning()
        return

    current = self.head

    for _ in range(position - 2):

        if current is None:
            print("Position out of range")
            return

        current = current.next

    if current is None or current.next is None:
        print("Position out of range")
        return

    current.next = current.next.next
```

Time Complexity: O(n)

---

## D. Delete a Node by Value

Suppose:

```text
10 ---> 20 ---> 30 ---> 40 ---> None
```

Delete the node containing `30`.

### Python Code

```python
def delete_by_value(self, value):

    if self.head is None:
        print("List is empty")
        return

    if self.head.data == value:
        self.head = self.head.next
        return

    current = self.head

    while current.next is not None:

        if current.next.data == value:

            current.next = current.next.next

            return

        current = current.next

    print("Value not found")
```

### Explanation

We check the next node instead of the current node because we need access to the previous node to change its link.

Time Complexity: O(n)

---

# 5.5 SEARCHING IN SINGLY LINKED LIST

Searching means finding whether a particular value exists in the list.

### Algorithm

1. Start from head.
2. Compare the current node's data with the target.
3. If equal, return its position.
4. Otherwise, move to the next node.
5. Stop when the target is found or the list ends.

### Python Code

```python
def search(self, value):

    current = self.head

    position = 1

    while current is not None:

        if current.data == value:
            return position

        current = current.next

        position += 1

    return -1
```

### Example

```text
10 ---> 20 ---> 30 ---> 40 ---> None
```

Search for 30.

| Step | Current Value | Comparison |
| ---- | ------------- | ---------- |
| 1    | 10            | Not found  |
| 2    | 20            | Not found  |
| 3    | 30            | Found      |

Output:

```text
Element found at position 3
```

Time Complexity: O(n)

---

# 5.6 COMPLETE SINGLY LINKED LIST IMPLEMENTATION IN PYTHON

This implementation combines all the operations discussed above.

```python
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    # INSERTION AT BEGINNING
    def insert_at_beginning(self, data):

        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node

    # INSERTION AT END
    def insert_at_end(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # INSERTION AT POSITION (1-BASED)
    def insert_at_position(self, data, position):

        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            self.insert_at_beginning(data)
            return

        current = self.head

        for _ in range(position - 2):

            if current is None:
                print("Position out of range")
                return

            current = current.next

        if current is None:
            print("Position out of range")
            return

        new_node = Node(data)

        new_node.next = current.next

        current.next = new_node

    # INSERT AFTER A VALUE
    def insert_after_value(self, target, data):

        current = self.head

        while current is not None:

            if current.data == target:

                new_node = Node(data)

                new_node.next = current.next

                current.next = new_node

                return

            current = current.next

        print("Target not found")

    # DELETE FROM BEGINNING
    def delete_from_beginning(self):

        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # DELETE FROM END
    def delete_from_end(self):

        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head

        while current.next.next is not None:
            current = current.next

        current.next = None

    # DELETE AT POSITION
    def delete_at_position(self, position):

        if position < 1:
            print("Invalid position")
            return

        if self.head is None:
            print("List is empty")
            return

        if position == 1:
            self.delete_from_beginning()
            return

        current = self.head

        for _ in range(position - 2):

            if current is None:
                print("Position out of range")
                return

            current = current.next

        if current is None or current.next is None:
            print("Position out of range")
            return

        current.next = current.next.next

    # DELETE BY VALUE
    def delete_by_value(self, value):

        if self.head is None:
            print("List is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None:

            if current.next.data == value:

                current.next = current.next.next

                return

            current = current.next

        print("Value not found")

    # SEARCH
    def search(self, value):

        current = self.head

        position = 1

        while current is not None:

            if current.data == value:
                return position

            current = current.next

            position += 1

        return -1

    # DISPLAY
    def display(self):

        current = self.head

        if current is None:
            print("List is empty")
            return

        while current is not None:

            print(current.data, end=" -> ")

            current = current.next

        print("None")


# DRIVER CODE

ll = SinglyLinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

ll.insert_at_beginning(5)

ll.insert_at_position(15, 3)

ll.display()

print("Position:", ll.search(20))

ll.delete_from_beginning()

ll.delete_from_end()

ll.delete_at_position(2)

ll.delete_by_value(20)

ll.display()
```

---

# 6. DOUBLY LINKED LIST (DLL)

## 6.1 What is a Doubly Linked List?

A Doubly Linked List is a linked list in which every node contains three fields:

1. Previous reference (`prev`)
2. Data
3. Next reference (`next`)

Unlike a singly linked list, we can move in both directions.

### Node Structure

```text
+----------+----------+----------+
|   PREV   |   DATA   |   NEXT   |
+----------+----------+----------+
```

### Diagram

```text
NULL <--- 10 <----> 20 <----> 30 ---> NULL
```

Each node maintains a reference to both its previous and next nodes.

## 6.2 Creating a Doubly Linked List Node

```python
class Node:

    def __init__(self, data):

        self.data = data

        self.prev = None

        self.next = None
```

Explanation:

- `data`: Stores the value.
- `prev`: Points to the previous node.
- `next`: Points to the next node.

## 6.3 Head and Tail

A doubly linked list commonly maintains both head and tail references.

```text
HEAD                              TAIL
 |                                  |
 v                                  v
None <- 10 <----> 20 <----> 30 -> None
```

---

# 6.4 TRAVERSAL IN DOUBLY LINKED LIST

A major advantage of a doubly linked list is that traversal is possible in both directions.

## A. Forward Traversal

Start from head and follow next references.

```text
10 ---> 20 ---> 30 ---> None
```

Code:

```python
def display_forward(self):

    current = self.head

    while current is not None:

        print(current.data, end=" <-> ")

        current = current.next

    print("None")
```

## B. Backward Traversal

Start from tail and follow previous references.

```text
30 ---> 20 ---> 10
```

Code:

```python
def display_backward(self):

    current = self.tail

    while current is not None:

        print(current.data, end=" <-> ")

        current = current.prev

    print("None")
```

Both traversals take O(n) time.

---

# 6.5 INSERTION IN DOUBLY LINKED LIST

Insertion requires modifying both previous and next references.

There are four major operations.

## A. Insertion at Beginning

Suppose:

```text
None <- 10 <----> 20 <----> 30 -> None
```

Insert `5`.

### Steps

1. Create a new node.
2. Make its next reference point to the old head.
3. Make the old head's previous reference point to the new node.
4. Update head.
5. If the list was empty, also update tail.

### Diagram

After:

```text
None <- 5 <----> 10 <----> 20 <----> 30 -> None
```

### Python Code

```python
def insert_at_beginning(self, data):

    new_node = Node(data)

    if self.head is None:

        self.head = new_node
        self.tail = new_node

        return

    new_node.next = self.head

    self.head.prev = new_node

    self.head = new_node
```

Time Complexity: O(1)

---

## B. Insertion at End

Suppose:

```text
None <- 10 <----> 20 <----> 30 -> None
```

Insert `40`.

### Steps

1. Create a new node.
2. If the list is empty, update head and tail.
3. Otherwise, connect the new node's previous reference to tail.
4. Connect tail's next reference to the new node.
5. Update tail.

### Python Code

```python
def insert_at_end(self, data):

    new_node = Node(data)

    if self.head is None:

        self.head = new_node
        self.tail = new_node

        return

    new_node.prev = self.tail

    self.tail.next = new_node

    self.tail = new_node
```

Time Complexity: O(1)

Because we maintain a tail reference.

---

## C. Insertion at a Specific Position

Suppose:

```text
10 <----> 20 <----> 40
```

Insert `30` at position 3.

### Python Code

```python
def insert_at_position(self, data, position):

    if position < 1:
        print("Invalid position")
        return

    if position == 1:
        self.insert_at_beginning(data)
        return

    current = self.head

    for _ in range(position - 2):

        if current is None:
            print("Position out of range")
            return

        current = current.next

    if current is None:
        print("Position out of range")
        return

    if current.next is None:
        self.insert_at_end(data)
        return

    new_node = Node(data)

    new_node.next = current.next

    new_node.prev = current

    current.next.prev = new_node

    current.next = new_node
```

### Understanding the Four Link Operations

```python
new_node.next = current.next
```

New node points to the next node.

```python
new_node.prev = current
```

New node points backward to the previous node.

```python
current.next.prev = new_node
```

The next node now points backward to the new node.

```python
current.next = new_node
```

The previous node now points forward to the new node.

**Important:** The order of operations matters. Preserve the old connections before overwriting them.

Time Complexity: O(n)

---

## D. Insertion After a Particular Value

```python
def insert_after_value(self, target, data):

    current = self.head

    while current is not None:

        if current.data == target:

            if current == self.tail:
                self.insert_at_end(data)
                return

            new_node = Node(data)

            new_node.next = current.next

            new_node.prev = current

            current.next.prev = new_node

            current.next = new_node

            return

        current = current.next

    print("Target not found")
```

Time Complexity: O(n)

---

# 6.6 DELETION IN DOUBLY LINKED LIST

## A. Deletion from Beginning

Suppose:

```text
None <- 10 <----> 20 <----> 30 -> None
```

Delete 10.

### Steps

1. Check if the list is empty.
2. If there is only one node, set head and tail to None.
3. Otherwise, move head to the next node.
4. Set the new head's previous reference to None.

### Python Code

```python
def delete_from_beginning(self):

    if self.head is None:
        print("List is empty")
        return

    if self.head == self.tail:

        self.head = None
        self.tail = None

        return

    self.head = self.head.next

    self.head.prev = None
```

Time Complexity: O(1)

---

## B. Deletion from End

Suppose:

```text
None <- 10 <----> 20 <----> 30 -> None
```

Delete 30.

### Steps

1. Check whether the list is empty.
2. If only one node exists, set head and tail to None.
3. Move tail to the previous node.
4. Set the new tail's next reference to None.

### Python Code

```python
def delete_from_end(self):

    if self.head is None:
        print("List is empty")
        return

    if self.head == self.tail:

        self.head = None
        self.tail = None

        return

    self.tail = self.tail.prev

    self.tail.next = None
```

Time Complexity: O(1)

---

## C. Deletion at a Specific Position

```python
def delete_at_position(self, position):

    if position < 1:
        print("Invalid position")
        return

    if self.head is None:
        print("List is empty")
        return

    if position == 1:
        self.delete_from_beginning()
        return

    current = self.head

    for _ in range(position - 1):

        if current is None:
            print("Position out of range")
            return

        current = current.next

    if current is None:
        print("Position out of range")
        return

    if current == self.tail:
        self.delete_from_end()
        return

    current.prev.next = current.next

    current.next.prev = current.prev
```

### Important Operations

```python
current.prev.next = current.next
```

The previous node skips the current node and connects to the next node.

```python
current.next.prev = current.prev
```

The next node connects backward to the previous node.

Time Complexity: O(n)

---

## D. Delete by Value

```python
def delete_by_value(self, value):

    current = self.head

    while current is not None:

        if current.data == value:

            if current == self.head:
                self.delete_from_beginning()
                return

            if current == self.tail:
                self.delete_from_end()
                return

            current.prev.next = current.next

            current.next.prev = current.prev

            return

        current = current.next

    print("Value not found")
```

Time Complexity: O(n)

---

# 6.7 SEARCHING IN DOUBLY LINKED LIST

Searching can be performed from either direction.

### Forward Search

```python
def search_forward(self, value):

    current = self.head

    position = 1

    while current is not None:

        if current.data == value:
            return position

        current = current.next

        position += 1

    return -1
```

### Backward Search

```python
def search_backward(self, value):

    current = self.tail

    position = 1

    while current is not None:

        if current.data == value:
            return position

        current = current.prev

        position += 1

    return -1
```

Note: Backward search returns the position counted from the end, not the original forward position.

Time Complexity: O(n)

---

# 6.8 COMPLETE DOUBLY LINKED LIST IMPLEMENTATION IN PYTHON

```python
class Node:

    def __init__(self, data):

        self.data = data

        self.prev = None

        self.next = None


class DoublyLinkedList:

    def __init__(self):

        self.head = None

        self.tail = None

    # INSERT AT BEGINNING
    def insert_at_beginning(self, data):

        new_node = Node(data)

        if self.head is None:

            self.head = new_node
            self.tail = new_node

            return

        new_node.next = self.head

        self.head.prev = new_node

        self.head = new_node

    # INSERT AT END
    def insert_at_end(self, data):

        new_node = Node(data)

        if self.head is None:

            self.head = new_node
            self.tail = new_node

            return

        new_node.prev = self.tail

        self.tail.next = new_node

        self.tail = new_node

    # INSERT AT POSITION
    def insert_at_position(self, data, position):

        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            self.insert_at_beginning(data)
            return

        current = self.head

        for _ in range(position - 2):

            if current is None:
                print("Position out of range")
                return

            current = current.next

        if current is None:
            print("Position out of range")
            return

        if current.next is None:
            self.insert_at_end(data)
            return

        new_node = Node(data)

        new_node.next = current.next
        new_node.prev = current

        current.next.prev = new_node
        current.next = new_node

    # INSERT AFTER VALUE
    def insert_after_value(self, target, data):

        current = self.head

        while current is not None:

            if current.data == target:

                if current == self.tail:
                    self.insert_at_end(data)
                    return

                new_node = Node(data)

                new_node.next = current.next
                new_node.prev = current

                current.next.prev = new_node
                current.next = new_node

                return

            current = current.next

        print("Target not found")

    # DELETE FROM BEGINNING
    def delete_from_beginning(self):

        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:

            self.head = None
            self.tail = None

            return

        self.head = self.head.next

        self.head.prev = None

    # DELETE FROM END
    def delete_from_end(self):

        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:

            self.head = None
            self.tail = None

            return

        self.tail = self.tail.prev

        self.tail.next = None

    # DELETE AT POSITION
    def delete_at_position(self, position):

        if position < 1:
            print("Invalid position")
            return

        if self.head is None:
            print("List is empty")
            return

        if position == 1:
            self.delete_from_beginning()
            return

        current = self.head

        for _ in range(position - 1):

            if current is None:
                print("Position out of range")
                return

            current = current.next

        if current is None:
            print("Position out of range")
            return

        if current == self.tail:
            self.delete_from_end()
            return

        current.prev.next = current.next

        current.next.prev = current.prev

    # DELETE BY VALUE
    def delete_by_value(self, value):

        current = self.head

        while current is not None:

            if current.data == value:

                if current == self.head:
                    self.delete_from_beginning()
                    return

                if current == self.tail:
                    self.delete_from_end()
                    return

                current.prev.next = current.next

                current.next.prev = current.prev

                return

            current = current.next

        print("Value not found")

    # SEARCH FORWARD
    def search_forward(self, value):

        current = self.head

        position = 1

        while current is not None:

            if current.data == value:
                return position

            current = current.next

            position += 1

        return -1

    # SEARCH BACKWARD
    def search_backward(self, value):

        current = self.tail

        position = 1

        while current is not None:

            if current.data == value:
                return position

            current = current.prev

            position += 1

        return -1

    # DISPLAY FORWARD
    def display_forward(self):

        current = self.head

        if current is None:
            print("List is empty")
            return

        while current is not None:

            print(current.data, end=" <-> ")

            current = current.next

        print("None")

    # DISPLAY BACKWARD
    def display_backward(self):

        current = self.tail

        if current is None:
            print("List is empty")
            return

        while current is not None:

            print(current.data, end=" <-> ")

            current = current.prev

        print("None")


# DRIVER CODE

dll = DoublyLinkedList()

dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)

dll.insert_at_beginning(5)

dll.insert_at_position(15, 3)

dll.display_forward()

dll.display_backward()

print("Position:", dll.search_forward(20))

dll.delete_from_beginning()

dll.delete_from_end()

dll.delete_at_position(2)

dll.delete_by_value(20)

dll.display_forward()
```

---

# 7. CIRCULAR LINKED LIST (CLL)

## 7.1 What is a Circular Linked List?

A Circular Linked List is a linked list in which the last node connects back to the first node.

Unlike a normal singly linked list, the last node does not point to None.

### Normal Singly Linked List

```text
10 ---> 20 ---> 30 ---> None
```

### Circular Singly Linked List

```text
       +----------------------+
       |                      |
       v                      |
10 ---> 20 ---> 30 ------------+
```

The last node points back to head.

## 7.2 Important Characteristics

- The last node points to the first node.
- There is no None at the end of a non-empty circular list.
- Traversal can continue indefinitely if no stopping condition is used.
- We need a special condition to detect when traversal is complete.

## 7.3 Why is a Circular Linked List Used?

Imagine a music playlist that repeats automatically.

After the last song, the first song plays again.

This is similar to a circular linked list.

Other applications include:

- Round-robin CPU scheduling.
- Multiplayer turn systems.
- Circular queues.
- Repeated task scheduling.

---

# 7.4 TRAVERSAL IN CIRCULAR LINKED LIST

In a normal linked list, we use:

```python
while current is not None:
```

But this will not work in a circular linked list because no node points to None.

Instead, we use a `do-while`-style traversal.

Python does not have a built-in do-while loop, so we use:

```python
def display(self):

    if self.head is None:
        print("List is empty")
        return

    current = self.head

    while True:

        print(current.data, end=" -> ")

        current = current.next

        if current == self.head:
            break

    print("(Back to Head)")
```

### Why do we use `while True`?

We must print the first node before checking whether we have returned to head.

The loop stops when:

```python
current == self.head
```

This means we have completed one full cycle.

---

# 7.5 INSERTION IN SINGLY CIRCULAR LINKED LIST

For this implementation, we maintain both `head` and `tail`.

Important condition:

```python
tail.next == head
```

## A. Insertion at Beginning

Suppose:

```text
10 ---> 20 ---> 30
^              |
|______________|
```

Insert `5`.

### Steps

1. Create a new node.
2. If the list is empty, set head and tail to the new node.
3. Make the new node point to the current head.
4. Update head.
5. Make tail point to the new head.

### Python Code

```python
def insert_at_beginning(self, data):

    new_node = Node(data)

    if self.head is None:

        self.head = new_node
        self.tail = new_node

        new_node.next = new_node

        return

    new_node.next = self.head

    self.head = new_node

    self.tail.next = self.head
```

### Diagram

Before:

```text
10 ---> 20 ---> 30
^              |
|______________|
```

After:

```text
5 ---> 10 ---> 20 ---> 30
^                       |
|_______________________|
```

Time Complexity: O(1)

---

## B. Insertion at End

Suppose:

```text
10 ---> 20 ---> 30
^              |
|______________|
```

Insert `40`.

### Steps

1. Create a new node.
2. If empty, make it the head and tail.
3. Make the current tail point to the new node.
4. Update tail.
5. Make the new tail point to head.

### Python Code

```python
def insert_at_end(self, data):

    new_node = Node(data)

    if self.head is None:

        self.head = new_node
        self.tail = new_node

        new_node.next = new_node

        return

    self.tail.next = new_node

    self.tail = new_node

    self.tail.next = self.head
```

Time Complexity: O(1)

Because we maintain a tail reference.

---

## C. Insertion at Specific Position

```python
def insert_at_position(self, data, position):

    if position < 1:
        print("Invalid position")
        return

    if position == 1:
        self.insert_at_beginning(data)
        return

    if self.head is None:
        print("Position out of range")
        return

    current = self.head

    for _ in range(position - 2):

        if current == self.tail:
            print("Position out of range")
            return

        current = current.next

    new_node = Node(data)

    new_node.next = current.next

    current.next = new_node

    if current == self.tail:
        self.tail = new_node
```

Time Complexity: O(n)

---

## D. Insertion After a Particular Value

```python
def insert_after_value(self, target, data):

    if self.head is None:
        print("List is empty")
        return

    current = self.head

    while True:

        if current.data == target:

            new_node = Node(data)

            new_node.next = current.next

            current.next = new_node

            if current == self.tail:
                self.tail = new_node

            return

        current = current.next

        if current == self.head:
            break

    print("Target not found")
```

Time Complexity: O(n)

---

# 7.6 DELETION IN SINGLY CIRCULAR LINKED LIST

## A. Deletion from Beginning

Suppose:

```text
10 ---> 20 ---> 30
^              |
|______________|
```

Delete 10.

### Steps

1. Check whether the list is empty.
2. If only one node exists, set head and tail to None.
3. Otherwise, move head to the next node.
4. Update tail's next reference to the new head.

### Python Code

```python
def delete_from_beginning(self):

    if self.head is None:
        print("List is empty")
        return

    if self.head == self.tail:

        self.head = None
        self.tail = None

        return

    self.head = self.head.next

    self.tail.next = self.head
```

Time Complexity: O(1)

---

## B. Deletion from End

Suppose:

```text
10 ---> 20 ---> 30
^              |
|______________|
```

Delete 30.

### Steps

1. Check whether the list is empty.
2. If only one node exists, clear head and tail.
3. Traverse to the second-last node.
4. Make it the new tail.
5. Make the new tail point to head.

### Python Code

```python
def delete_from_end(self):

    if self.head is None:
        print("List is empty")
        return

    if self.head == self.tail:

        self.head = None
        self.tail = None

        return

    current = self.head

    while current.next != self.tail:
        current = current.next

    self.tail = current

    self.tail.next = self.head
```

Time Complexity: O(n)

---

## C. Deletion at Specific Position

```python
def delete_at_position(self, position):

    if position < 1:
        print("Invalid position")
        return

    if self.head is None:
        print("List is empty")
        return

    if position == 1:
        self.delete_from_beginning()
        return

    current = self.head

    for _ in range(position - 2):

        if current == self.tail:
            print("Position out of range")
            return

        current = current.next

    if current.next == self.head:
        print("Position out of range")
        return

    target = current.next

    current.next = target.next

    if target == self.tail:
        self.tail = current
```

Time Complexity: O(n)

---

## D. Delete by Value

```python
def delete_by_value(self, value):

    if self.head is None:
        print("List is empty")
        return

    if self.head.data == value:
        self.delete_from_beginning()
        return

    current = self.head

    while current.next != self.head:

        if current.next.data == value:

            target = current.next

            current.next = target.next

            if target == self.tail:
                self.tail = current

            return

        current = current.next

    print("Value not found")
```

This implementation deletes the first occurrence of the value.

Time Complexity: O(n)

---

# 7.7 SEARCHING IN SINGLY CIRCULAR LINKED LIST

```python
def search(self, value):

    if self.head is None:
        return -1

    current = self.head

    position = 1

    while True:

        if current.data == value:
            return position

        current = current.next

        position += 1

        if current == self.head:
            break

    return -1
```

The search stops when we return to head.

Time Complexity: O(n)

---

# 7.8 COMPLETE SINGLY CIRCULAR LINKED LIST IMPLEMENTATION

```python
class Node:

    def __init__(self, data):

        self.data = data

        self.next = None


class CircularLinkedList:

    def __init__(self):

        self.head = None

        self.tail = None

    # INSERT AT BEGINNING
    def insert_at_beginning(self, data):

        new_node = Node(data)

        if self.head is None:

            self.head = new_node
            self.tail = new_node

            new_node.next = new_node

            return

        new_node.next = self.head

        self.head = new_node

        self.tail.next = self.head

    # INSERT AT END
    def insert_at_end(self, data):

        new_node = Node(data)

        if self.head is None:

            self.head = new_node
            self.tail = new_node

            new_node.next = new_node

            return

        self.tail.next = new_node

        self.tail = new_node

        self.tail.next = self.head

    # INSERT AT POSITION
    def insert_at_position(self, data, position):

        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            self.insert_at_beginning(data)
            return

        if self.head is None:
            print("Position out of range")
            return

        current = self.head

        for _ in range(position - 2):

            if current == self.tail:
                print("Position out of range")
                return

            current = current.next

        new_node = Node(data)

        new_node.next = current.next

        current.next = new_node

        if current == self.tail:
            self.tail = new_node

    # INSERT AFTER VALUE
    def insert_after_value(self, target, data):

        if self.head is None:
            print("List is empty")
            return

        current = self.head

        while True:

            if current.data == target:

                new_node = Node(data)

                new_node.next = current.next

                current.next = new_node

                if current == self.tail:
                    self.tail = new_node

                return

            current = current.next

            if current == self.head:
                break

        print("Target not found")

    # DELETE FROM BEGINNING
    def delete_from_beginning(self):

        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:

            self.head = None
            self.tail = None

            return

        self.head = self.head.next

        self.tail.next = self.head

    # DELETE FROM END
    def delete_from_end(self):

        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:

            self.head = None
            self.tail = None

            return

        current = self.head

        while current.next != self.tail:
            current = current.next

        self.tail = current

        self.tail.next = self.head

    # DELETE AT POSITION
    def delete_at_position(self, position):

        if position < 1:
            print("Invalid position")
            return

        if self.head is None:
            print("List is empty")
            return

        if position == 1:
            self.delete_from_beginning()
            return

        current = self.head

        for _ in range(position - 2):

            if current == self.tail:
                print("Position out of range")
                return

            current = current.next

        if current.next == self.head:
            print("Position out of range")
            return

        target = current.next

        current.next = target.next

        if target == self.tail:
            self.tail = current

    # DELETE BY VALUE
    def delete_by_value(self, value):

        if self.head is None:
            print("List is empty")
            return

        if self.head.data == value:
            self.delete_from_beginning()
            return

        current = self.head

        while current.next != self.head:

            if current.next.data == value:

                target = current.next

                current.next = target.next

                if target == self.tail:
                    self.tail = current

                return

            current = current.next

        print("Value not found")

    # SEARCH
    def search(self, value):

        if self.head is None:
            return -1

        current = self.head

        position = 1

        while True:

            if current.data == value:
                return position

            current = current.next

            position += 1

            if current == self.head:
                break

        return -1

    # DISPLAY
    def display(self):

        if self.head is None:
            print("List is empty")
            return

        current = self.head

        while True:

            print(current.data, end=" -> ")

            current = current.next

            if current == self.head:
                break

        print("(Back to Head)")


# DRIVER CODE

cll = CircularLinkedList()

cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)

cll.insert_at_beginning(5)

cll.insert_at_position(15, 3)

cll.display()

print("Position:", cll.search(20))

cll.delete_from_beginning()

cll.delete_from_end()

cll.delete_at_position(2)

cll.delete_by_value(20)

cll.display()
```

---

# 8. DOUBLY CIRCULAR LINKED LIST

## 8.1 What is a Doubly Circular Linked List?

A Doubly Circular Linked List combines the features of a doubly linked list and a circular linked list.

Every node contains:

1. Previous reference.
2. Data.
3. Next reference.

Additionally:

- The last node points to the first node.
- The first node's previous reference points to the last node.

### Diagram

```text
          +---------------------------+
          |                           |
          v                           |
     +--------+     +--------+     +--------+
<--->|   10   |<--->|   20   |<--->|   30   |<--->
     +--------+     +--------+     +--------+
          ^                           |
          |___________________________|
```

More precisely, the important relationships are:

```python
head.prev == tail
tail.next == head
```

These two conditions define the circular doubly linked structure.

## 8.2 Node Structure

```python
class Node:

    def __init__(self, data):

        self.data = data

        self.prev = None

        self.next = None
```

---

# 8.3 TRAVERSAL

## A. Forward Traversal

```python
def display_forward(self):

    if self.head is None:
        print("List is empty")
        return

    current = self.head

    while True:

        print(current.data, end=" <-> ")

        current = current.next

        if current == self.head:
            break

    print("(Back to Head)")
```

## B. Backward Traversal

```python
def display_backward(self):

    if self.tail is None:
        print("List is empty")
        return

    current = self.tail

    while True:

        print(current.data, end=" <-> ")

        current = current.prev

        if current == self.tail:
            break

    print("(Back to Tail)")
```

Both operations take O(n) time.

---

# 8.4 INSERTION IN DOUBLY CIRCULAR LINKED LIST

## A. Insertion at Beginning

### Steps

1. Create a new node.
2. If empty, point its next and previous references to itself.
3. Otherwise, connect the new node between the old tail and old head.
4. Update head.
5. Maintain the circular connections.

### Python Code

```python
def insert_at_beginning(self, data):

    new_node = Node(data)

    if self.head is None:

        self.head = new_node
        self.tail = new_node

        new_node.next = new_node
        new_node.prev = new_node

        return

    new_node.next = self.head
    new_node.prev = self.tail

    self.head.prev = new_node
    self.tail.next = new_node

    self.head = new_node
```

Time Complexity: O(1)

---

## B. Insertion at End

```python
def insert_at_end(self, data):

    new_node = Node(data)

    if self.head is None:

        self.head = new_node
        self.tail = new_node

        new_node.next = new_node
        new_node.prev = new_node

        return

    new_node.prev = self.tail
    new_node.next = self.head

    self.tail.next = new_node
    self.head.prev = new_node

    self.tail = new_node
```

Time Complexity: O(1)

---

## C. Insertion at a Specific Position

```python
def insert_at_position(self, data, position):

    if position < 1:
        print("Invalid position")
        return

    if position == 1:
        self.insert_at_beginning(data)
        return

    if self.head is None:
        print("Position out of range")
        return

    current = self.head

    for _ in range(position - 2):

        if current == self.tail:
            print("Position out of range")
            return

        current = current.next

    if current == self.tail:
        self.insert_at_end(data)
        return

    new_node = Node(data)

    new_node.next = current.next
    new_node.prev = current

    current.next.prev = new_node
    current.next = new_node
```

Time Complexity: O(n)

---

## D. Insertion After a Particular Value

```python
def insert_after_value(self, target, data):

    if self.head is None:
        print("List is empty")
        return

    current = self.head

    while True:

        if current.data == target:

            if current == self.tail:
                self.insert_at_end(data)
                return

            new_node = Node(data)

            new_node.next = current.next
            new_node.prev = current

            current.next.prev = new_node
            current.next = new_node

            return

        current = current.next

        if current == self.head:
            break

    print("Target not found")
```

Time Complexity: O(n)

---

# 8.5 DELETION IN DOUBLY CIRCULAR LINKED LIST

## A. Deletion from Beginning

### Steps

1. Check whether the list is empty.
2. If only one node exists, set head and tail to None.
3. Otherwise, move head to the next node.
4. Update the new head's previous reference to tail.
5. Update tail's next reference to head.

### Python Code

```python
def delete_from_beginning(self):

    if self.head is None:
        print("List is empty")
        return

    if self.head == self.tail:

        self.head = None
        self.tail = None

        return

    self.head = self.head.next

    self.head.prev = self.tail

    self.tail.next = self.head
```

Time Complexity: O(1)

---

## B. Deletion from End

```python
def delete_from_end(self):

    if self.head is None:
        print("List is empty")
        return

    if self.head == self.tail:

        self.head = None
        self.tail = None

        return

    self.tail = self.tail.prev

    self.tail.next = self.head

    self.head.prev = self.tail
```

Time Complexity: O(1)

---

## C. Deletion at a Specific Position

```python
def delete_at_position(self, position):

    if position < 1:
        print("Invalid position")
        return

    if self.head is None:
        print("List is empty")
        return

    if position == 1:
        self.delete_from_beginning()
        return

    current = self.head

    for _ in range(position - 1):

        if current == self.tail:
            print("Position out of range")
            return

        current = current.next

    if current == self.tail:
        self.delete_from_end()
        return

    current.prev.next = current.next

    current.next.prev = current.prev
```

Time Complexity: O(n)

---

## D. Delete by Value

```python
def delete_by_value(self, value):

    if self.head is None:
        print("List is empty")
        return

    current = self.head

    while True:

        if current.data == value:

            if current == self.head:
                self.delete_from_beginning()
                return

            if current == self.tail:
                self.delete_from_end()
                return

            current.prev.next = current.next

            current.next.prev = current.prev

            return

        current = current.next

        if current == self.head:
            break

    print("Value not found")
```

Time Complexity: O(n)

---

# 8.6 SEARCHING IN DOUBLY CIRCULAR LINKED LIST

```python
def search(self, value):

    if self.head is None:
        return -1

    current = self.head

    position = 1

    while True:

        if current.data == value:
            return position

        current = current.next

        position += 1

        if current == self.head:
            break

    return -1
```

Time Complexity: O(n)

---

# 8.7 COMPLETE DOUBLY CIRCULAR LINKED LIST IMPLEMENTATION

```python
class Node:

    def __init__(self, data):

        self.data = data

        self.prev = None

        self.next = None


class DoublyCircularLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

    # INSERT AT BEGINNING
    def insert_at_beginning(self, data):

        new_node = Node(data)

        if self.head is None:

            self.head = new_node
            self.tail = new_node

            new_node.next = new_node
            new_node.prev = new_node

            return

        new_node.next = self.head
        new_node.prev = self.tail

        self.head.prev = new_node
        self.tail.next = new_node

        self.head = new_node

    # INSERT AT END
    def insert_at_end(self, data):

        new_node = Node(data)

        if self.head is None:

            self.head = new_node
            self.tail = new_node

            new_node.next = new_node
            new_node.prev = new_node

            return

        new_node.prev = self.tail
        new_node.next = self.head

        self.tail.next = new_node
        self.head.prev = new_node

        self.tail = new_node

    # INSERT AT POSITION
    def insert_at_position(self, data, position):

        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            self.insert_at_beginning(data)
            return

        if self.head is None:
            print("Position out of range")
            return

        current = self.head

        for _ in range(position - 2):

            if current == self.tail:
                print("Position out of range")
                return

            current = current.next

        if current == self.tail:
            self.insert_at_end(data)
            return

        new_node = Node(data)

        new_node.next = current.next
        new_node.prev = current

        current.next.prev = new_node
        current.next = new_node

    # INSERT AFTER VALUE
    def insert_after_value(self, target, data):

        if self.head is None:
            print("List is empty")
            return

        current = self.head

        while True:

            if current.data == target:

                if current == self.tail:
                    self.insert_at_end(data)
                    return

                new_node = Node(data)

                new_node.next = current.next
                new_node.prev = current

                current.next.prev = new_node
                current.next = new_node

                return

            current = current.next

            if current == self.head:
                break

        print("Target not found")

    # DELETE FROM BEGINNING
    def delete_from_beginning(self):

        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:

            self.head = None
            self.tail = None

            return

        self.head = self.head.next

        self.head.prev = self.tail

        self.tail.next = self.head

    # DELETE FROM END
    def delete_from_end(self):

        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:

            self.head = None
            self.tail = None

            return

        self.tail = self.tail.prev

        self.tail.next = self.head

        self.head.prev = self.tail

    # DELETE AT POSITION
    def delete_at_position(self, position):

        if position < 1:
            print("Invalid position")
            return

        if self.head is None:
            print("List is empty")
            return

        if position == 1:
            self.delete_from_beginning()
            return

        current = self.head

        for _ in range(position - 1):

            if current == self.tail:
                print("Position out of range")
                return

            current = current.next

        if current == self.tail:
            self.delete_from_end()
            return

        current.prev.next = current.next

        current.next.prev = current.prev

    # DELETE BY VALUE
    def delete_by_value(self, value):

        if self.head is None:
            print("List is empty")
            return

        current = self.head

        while True:

            if current.data == value:

                if current == self.head:
                    self.delete_from_beginning()
                    return

                if current == self.tail:
                    self.delete_from_end()
                    return

                current.prev.next = current.next

                current.next.prev = current.prev

                return

            current = current.next

            if current == self.head:
                break

        print("Value not found")

    # SEARCH
    def search(self, value):

        if self.head is None:
            return -1

        current = self.head

        position = 1

        while True:

            if current.data == value:
                return position

            current = current.next

            position += 1

            if current == self.head:
                break

        return -1

    # DISPLAY FORWARD
    def display_forward(self):

        if self.head is None:
            print("List is empty")
            return

        current = self.head

        while True:

            print(current.data, end=" <-> ")

            current = current.next

            if current == self.head:
                break

        print("(Back to Head)")

    # DISPLAY BACKWARD
    def display_backward(self):

        if self.tail is None:
            print("List is empty")
            return

        current = self.tail

        while True:

            print(current.data, end=" <-> ")

            current = current.prev

            if current == self.tail:
                break

        print("(Back to Tail)")


# DRIVER CODE

dcll = DoublyCircularLinkedList()

dcll.insert_at_end(10)
dcll.insert_at_end(20)
dcll.insert_at_end(30)

dcll.insert_at_beginning(5)

dcll.insert_at_position(15, 3)

dcll.display_forward()

dcll.display_backward()

print("Position:", dcll.search(20))

dcll.delete_from_beginning()

dcll.delete_from_end()

dcll.delete_at_position(2)

dcll.delete_by_value(20)

dcll.display_forward()
```

---

# 9. TIME AND SPACE COMPLEXITY

Understanding complexity is essential for DSA examinations and interviews.

Let:

- n = Number of nodes.
- O(1) = Constant time.
- O(n) = Linear time.

## 9.1 Singly Linked List

Assuming no tail reference:

| Operation               | Time Complexity |
| ----------------------- | --------------- |
| Access first node       | O(1)            |
| Access by position      | O(n)            |
| Insertion at beginning  | O(1)            |
| Insertion at end        | O(n)            |
| Insertion at known node | O(1)            |
| Insertion at position   | O(n)            |
| Deletion at beginning   | O(1)            |
| Deletion at end         | O(n)            |
| Deletion at position    | O(n)            |
| Search                  | O(n)            |
| Display                 | O(n)            |

With a tail reference, insertion at the end becomes O(1).

## 9.2 Doubly Linked List

Assuming head and tail references:

| Operation               | Time Complexity |
| ----------------------- | --------------- |
| Access first node       | O(1)            |
| Access last node        | O(1)            |
| Access by position      | O(n)            |
| Insertion at beginning  | O(1)            |
| Insertion at end        | O(1)            |
| Insertion at known node | O(1)            |
| Insertion at position   | O(n)            |
| Deletion at beginning   | O(1)            |
| Deletion at end         | O(1)            |
| Deletion at known node  | O(1)            |
| Deletion at position    | O(n)            |
| Search                  | O(n)            |
| Display                 | O(n)            |

## 9.3 Singly Circular Linked List

Assuming head and tail references:

| Operation              | Time Complexity |
| ---------------------- | --------------- |
| Insertion at beginning | O(1)            |
| Insertion at end       | O(1)            |
| Insertion at position  | O(n)            |
| Deletion at beginning  | O(1)            |
| Deletion at end        | O(n)            |
| Deletion at position   | O(n)            |
| Search                 | O(n)            |
| Display                | O(n)            |

## 9.4 Doubly Circular Linked List

Assuming head and tail references:

| Operation              | Time Complexity |
| ---------------------- | --------------- |
| Insertion at beginning | O(1)            |
| Insertion at end       | O(1)            |
| Insertion at position  | O(n)            |
| Deletion at beginning  | O(1)            |
| Deletion at end        | O(1)            |
| Deletion at position   | O(n)            |
| Deletion at known node | O(1)            |
| Search                 | O(n)            |
| Display                | O(n)            |

## 9.5 Space Complexity

For all linked list types:

- Storage for n nodes: O(n).
- Auxiliary space for iterative traversal: O(1).
- Recursive traversal: O(n) call stack in the worst case.

Doubly linked lists use additional memory because every node stores an extra `prev` reference.

---

# 10. COMPARISON OF ALL LINKED LIST TYPES

| Feature                        | Singly LL | Doubly LL | Circular Singly LL | Circular Doubly LL |
| ------------------------------ | --------- | --------- | ------------------ | ------------------ |
| Data field                     | Yes       | Yes       | Yes                | Yes                |
| Next reference                 | Yes       | Yes       | Yes                | Yes                |
| Previous reference             | No        | Yes       | No                 | Yes                |
| Last node points to head       | No        | No        | Yes                | Yes                |
| First node points back to tail | No        | No        | No                 | Yes                |
| Forward traversal              | Yes       | Yes       | Yes                | Yes                |
| Backward traversal             | No        | Yes       | No                 | Yes                |
| Reverse deletion               | Difficult | Easier    | Difficult          | Easier             |
| Extra memory                   | Low       | Higher    | Low                | Higher             |

## Key Differences

### Singly vs Doubly Linked List

Singly Linked List:

- One link per node.
- Only forward traversal.
- Less memory.
- Deletion of a known node generally requires access to its previous node.

Doubly Linked List:

- Two links per node.
- Forward and backward traversal.
- More memory.
- Easier deletion when a reference to the target node is available.

### Singly vs Circular Singly Linked List

Singly Linked List:

- Last node points to None.
- Traversal stops at None.

Circular Singly Linked List:

- Last node points to head.
- Traversal stops when we return to head.

### Doubly vs Circular Doubly Linked List

Doubly Linked List:

- Head's previous reference is None.
- Tail's next reference is None.

Circular Doubly Linked List:

- Head's previous reference is tail.
- Tail's next reference is head.

---

# 11. COMMON MISTAKES AND EDGE CASES

These are important because most linked list bugs occur during insertion and deletion.

## 11.1 Forgetting the Empty List Condition

Incorrect:

```python
current = self.head

print(current.data)
```

If the list is empty, `self.head` is None and this produces an error.

Correct:

```python
if self.head is None:
    print("List is empty")
    return
```

## 11.2 Forgetting the Single Node Case

Suppose:

```text
10 -> None
```

Deleting the last node must make:

```python
self.head = None
```

For doubly linked lists, both head and tail must become None.

For circular linked lists, the same principle applies.

## 11.3 Wrong Order During Insertion

Suppose:

```text
10 ---> 20 ---> 30
```

We want to insert 25 after 20.

Correct:

```python
new_node.next = current.next

current.next = new_node
```

If we first execute:

```python
current.next = new_node
```

we overwrite the reference to node 30.

We may lose access to the remaining list.

Therefore, preserve the old link first.

## 11.4 Forgetting Tail Updates

If insertion or deletion changes the last node, update tail.

Examples:

```python
self.tail = new_node
```

or:

```python
self.tail = self.tail.prev
```

Otherwise, the tail reference may point to an incorrect node.

## 11.5 Infinite Loops in Circular Linked Lists

Incorrect:

```python
while current is not None:
    current = current.next
```

A circular linked list never reaches None.

Correct:

```python
while True:

    print(current.data)

    current = current.next

    if current == self.head:
        break
```

## 11.6 Forgetting Circular Connections

For a singly circular linked list:

```python
self.tail.next = self.head
```

For a doubly circular linked list:

```python
self.tail.next = self.head
self.head.prev = self.tail
```

These conditions must remain true after every modification.

## 11.7 Position Indexing

In these notes, positions start from 1.

Example:

```text
Position:  1       2       3
           |       |       |
           v       v       v
          10      20      30
```

Do not confuse 1-based positions with Python's 0-based list indexing.

---

# 12. IMPORTANT APPLICATIONS OF LINKED LISTS

## 12.1 Music Playlist

A playlist can be implemented using a doubly linked list.

- Next song: Move using next.
- Previous song: Move using prev.

A circular doubly linked list can support continuous playback.

## 12.2 Browser History

A doubly linked list can represent navigation history.

- Previous page: prev.
- Next page: next.

## 12.3 CPU Round-Robin Scheduling

Circular linked lists are useful in round-robin scheduling.

Each process receives CPU time in a repeated cycle.

```text
P1 -> P2 -> P3 -> P4
^                   |
|___________________|
```

After P4, execution returns to P1 if the processes remain active.

## 12.4 Undo and Redo Operations

Doubly linked lists can represent a sequence of states.

- Undo: Move backward.
- Redo: Move forward.

## 12.5 Implementing Stacks and Queues

Linked lists can implement:

- Stack: Push and pop operations.
- Queue: Enqueue and dequeue operations.

## 12.6 Memory Management

Linked structures can represent free blocks and other dynamically managed collections.

---

# 13. IMPORTANT DSA EXAMINATION AND INTERVIEW QUESTIONS

## A. Basic Questions

1. What is a linked list?
2. What is a node?
3. What is a pointer/reference?
4. What is the role of head?
5. What is the difference between an array and a linked list?
6. Why is linked list called a dynamic data structure?
7. What is the difference between static and dynamic memory allocation?
8. What is traversal?

## B. Singly Linked List Questions

1. Write a program to create a singly linked list.
2. Insert a node at the beginning.
3. Insert a node at the end.
4. Insert a node at a given position.
5. Delete the first node.
6. Delete the last node.
7. Delete a node containing a particular value.
8. Search for an element.
9. Count the total number of nodes.
10. Reverse a singly linked list.
11. Find the middle node.
12. Find the nth node from the end.
13. Detect a cycle in a linked list.

## C. Doubly Linked List Questions

1. Explain the structure of a doubly linked list.
2. Write a program for forward traversal.
3. Write a program for backward traversal.
4. Insert at the beginning and end.
5. Delete from the beginning and end.
6. Explain how deletion differs from a singly linked list.
7. Reverse a doubly linked list.
8. Find the length of a doubly linked list.

## D. Circular Linked List Questions

1. What is a circular linked list?
2. How is it different from a normal linked list?
3. Why does a circular linked list not contain None at the end?
4. Write a program for circular traversal.
5. Insert at the beginning.
6. Insert at the end.
7. Delete from the beginning.
8. Delete from the end.
9. Explain round-robin scheduling.
10. How can you detect when traversal is complete?

## E. Advanced Questions

1. Reverse a singly linked list iteratively.
2. Reverse a singly linked list recursively.
3. Merge two sorted linked lists.
4. Remove duplicate elements.
5. Find the intersection point of two linked lists.
6. Detect and remove a loop.
7. Implement a stack using a linked list.
8. Implement a queue using a linked list.
9. Find the length of a circular linked list.
10. Check whether a linked list is a palindrome.

---

# 14. ADDITIONAL IMPORTANT PROGRAMS

## 14.1 Count the Number of Nodes

```python
def count_nodes(self):

    count = 0

    current = self.head

    while current is not None:

        count += 1

        current = current.next

    return count
```

Time Complexity: O(n)

For a circular linked list, use a return-to-head stopping condition instead.

## 14.2 Reverse a Singly Linked List

This is one of the most important linked list problems.

### Original List

```text
10 ---> 20 ---> 30 ---> 40 ---> None
```

### Reversed List

```text
40 ---> 30 ---> 20 ---> 10 ---> None
```

### Three Important References

We use:

- `prev`: Previous node.
- `current`: Current node.
- `next_node`: Next node.

### Python Code

```python
def reverse(self):

    prev = None

    current = self.head

    while current is not None:

        next_node = current.next

        current.next = prev

        prev = current

        current = next_node

    self.head = prev
```

### Understanding the Logic

Initially:

```text
prev = None
current = 10
```

Save the next node:

```python
next_node = current.next
```

Reverse the current link:

```python
current.next = prev
```

Move prev forward:

```python
prev = current
```

Move current forward:

```python
current = next_node
```

Repeat until current becomes None.

Finally:

```python
self.head = prev
```

Time Complexity: O(n)

Space Complexity: O(1)

---

# 15. IMPORTANT LOGIC PATTERNS TO MEMORIZE

These small patterns form the foundation of almost every linked list operation.

## Pattern 1: Move to the Next Node

```python
current = current.next
```

Used in:

- Traversal
- Searching
- Insertion
- Deletion

## Pattern 2: Insert After Current Node

```python
new_node.next = current.next

current.next = new_node
```

## Pattern 3: Delete the Node After Current

```python
current.next = current.next.next
```

Always check that `current.next` exists before using it.

## Pattern 4: Move Head Forward

```python
self.head = self.head.next
```

## Pattern 5: Find the Last Node in a Normal Singly Linked List

```python
while current.next is not None:
    current = current.next
```

## Pattern 6: Find the Second-Last Node

```python
while current.next.next is not None:
    current = current.next
```

Check that the list has at least two nodes before using this pattern.

## Pattern 7: Circular Traversal

```python
current = self.head

while True:

    print(current.data)

    current = current.next

    if current == self.head:
        break
```

## Pattern 8: Doubly Linked List Connection

```python
new_node.prev = current
new_node.next = current.next

current.next.prev = new_node
current.next = new_node
```

This inserts a node between two existing nodes.

---

# 16. QUICK REVISION SHEET

## Singly Linked List

Node:

```python
self.data = data
self.next = None
```

Last node:

```python
last.next = None
```

Insertion at beginning:

```python
new_node.next = self.head
self.head = new_node
```

Deletion at beginning:

```python
self.head = self.head.next
```

Traversal:

```python
while current is not None:
    current = current.next
```

## Doubly Linked List

Node:

```python
self.prev = None
self.data = data
self.next = None
```

Insertion between nodes:

```python
new_node.prev = current
new_node.next = current.next

current.next.prev = new_node
current.next = new_node
```

Deletion of a known middle node:

```python
current.prev.next = current.next
current.next.prev = current.prev
```

## Singly Circular Linked List

Important condition:

```python
self.tail.next = self.head
```

Insertion at beginning:

```python
new_node.next = self.head
self.head = new_node
self.tail.next = self.head
```

Traversal stops when:

```python
current == self.head
```

## Doubly Circular Linked List

Important conditions:

```python
self.tail.next = self.head
self.head.prev = self.tail
```

Both must remain true.

---

# 17. FINAL CONCEPTUAL SUMMARY

| Linked List                 | Number of Links | Direction                 | Last Node      |
| --------------------------- | --------------: | ------------------------- | -------------- |
| Singly Linked List          |               1 | Forward                   | Points to None |
| Doubly Linked List          |               2 | Forward and backward      | Points to None |
| Circular Singly Linked List |               1 | Forward, circular         | Points to head |
| Circular Doubly Linked List |               2 | Both directions, circular | Points to head |

### The Most Important Things to Understand

1. A linked list is made of nodes.
2. A node stores data and references.
3. Head identifies the first node.
4. Tail identifies the last node when maintained.
5. Insertion means changing links to include a new node.
6. Deletion means changing links to bypass a node.
7. Traversal means visiting nodes one by one.
8. Searching means comparing node data with a target.
9. Doubly linked lists allow backward traversal.
10. Circular linked lists require special traversal stopping conditions.

**The fundamental principle of linked lists:**

You generally do not move elements around as you would in an array. You change the references connecting the nodes.

Once you understand how references are connected, insertion and deletion become much easier to implement.

---

**End of Linked List Note**

# Complete Notes on Linked Lists in Python

## Singly Linked List, Doubly Linked List, and Circular Linked List

> These notes cover the concepts from beginner level, pointer/reference
> logic, diagrams, Python implementations, all common insertion and
> deletion operations, searching, traversal/display, edge cases,
> complexity analysis, comparisons, and practice questions.

---

# 1. Introduction to Linked Lists

## 1.1 What is a linked list?

A **linked list** is a linear data structure in which elements (called
**nodes**) are stored in separate objects. Each node stores:

1. **Data** -- the value we want to store.
2. **Link / pointer / reference** -- a reference to another node.

Unlike an array or Python list, linked-list nodes do not need to occupy
adjacent memory locations. The links connect the nodes and establish
their order.

Example:

```text
HEAD
 |
 v
+------+------+
|  10  |  o---|---->
+------+------+
                 +------+------+
                 |  20  |  o---|---->
                 +------+------+
                                  +------+------+
                                  |  30  | None |
                                  +------+------+
```

Here: - `head` refers to the first node. - The first node stores `10`
and a reference to the second node. - The second node stores `20` and a
reference to the third node. - The last node stores `30` and its `next`
reference is `None`. - `None` means that there is no next node.

## 1.2 What is a node?

A node is the basic building block of a linked list.

A simple Python node:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

Explanation:

- `class Node`: defines a blueprint for creating nodes.
- `self.data = data`: stores the value.
- `self.next = None`: initially, the node does not point to another
  node.
- `self` refers to the current object.

Creating nodes manually:

```python
first = Node(10)
second = Node(20)
third = Node(30)

first.next = second
second.next = third

head = first
```

The resulting structure is:

```text
head
 |
 v
10 -> 20 -> 30 -> None
```

**Important:** `head` is not the data itself. It is a reference to the
first node.

## 1.3 Important terms

---

  Term                                Meaning

---

  Node                                One unit containing data and
                                      link(s)

  Data                                Value stored in a node

  Head                                Reference to the first node

  Tail                                Reference to the last node, if
                                      maintained

  Next                                Reference to the next node

  Previous (`prev`)                   Reference to the previous node in a
                                      doubly linked list

  `None`                              Indicates the absence of a
                                      node/reference

  Traversal                           Visiting nodes one by one

  Insertion                           Adding a new node

  Deletion                            Removing a node

  Searching                           Finding a node containing a target
                                      value

Empty list                          A list in which `head` is `None`
--------------------------------------------------------

## 1.4 Why do we need linke

d lists?

A normal Python list is implemented using a dynamic array. It provides
fast indexing, but inserting or deleting an element near the beginning
can require shifting other elements.

A linked list connects nodes through references. Insertion or deletion
can be efficient when the required node or its predecessor is already
known.

### Linked list vs array/Python list

---

  Feature                 Array / Python list     Linked list

---

  Storage                 Contiguous array-like   Separate node objects
                          storage internally      connected by references

  Access by index         O(1)                    O(n)

  Search (unsorted)       O(n)                    O(n)

  Insert at beginning     O(n) due to shifting in O(1)
                          a typical dynamic array

  Delete at beginning     O(n) due to shifting    O(1)

  Insert after a known    Usually requires        O(1)
  node                    shifting elements

  Extra memory            Usually less per        Extra reference(s) per
                          element                 node

  Cache locality          Usually better          Usually poorer

Implementation          Easier                  Requires link
                                                  management
------------------------------------------------------------

Python's built-in `list` is not a linked list. The classes in these
notes implement linked lists manually.

---

# 2. Types of Linked Lists

The three main types covered here are:

1. Singly Linked List
2. Doubly Linked List
3. Circular Linked List

A circular linked list can itself be singly circular or doubly circular.
Both forms are explained.

---

# 3. Singly Linked List (SLL)

## 3.1 Definition

A **singly linked list** is a linked list in which every node
contains: - Data - A reference to the next node

Each node points only in the forward direction.

```text
HEAD
 |
 v
+------+------+
|  10  | next |---->
+------+------+
                    +------+------+
                    |  20  | next |---->
                    +------+------+
                                        +------+------+
                                        |  30  | None |
                                        +------+------+
```

The last node points to `None`, so traversal stops there.

## 3.2 Structure of a singly linked-list node

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

Each node has: - `data`: the stored value. - `next`: the reference to
the next node.

## 3.3 The head reference

`head` stores the reference to the first node.

```python
head = None
```

This represents an empty list.

After inserting `10`:

```text
head
 |
 v
10 -> None
```

After inserting `20` at the end:

```text
head
 |
 v
10 -> 20 -> None
```

When the first node is deleted, `head` must be updated to the second
node.

## 3.4 Traversal

**Traversal** means visiting each node from the first node to the last
node.

Basic traversal:

```python
current = head

while current is not None:
    print(current.data)
    current = current.next
```

How it works:

1. Start at `head`.
2. Process the current node's data.
3. Move to the next node using `current.next`.
4. Repeat until `current` becomes `None`.

Never confuse these two operations:

```python
current = current.next
```

This moves the temporary reference forward.

```python
head = head.next
```

This changes the actual starting point of the list. Doing this
accidentally during display can lose access to the beginning of the
list.

## 3.5 Complete singly linked-list implementation

The following class supports: - Insertion at the beginning - Insertion
at the end - Insertion at a given zero-based position - Insertion after
a particular value - Insertion before a particular value - Deletion from
the beginning - Deletion from the end - Deletion at a given position -
Deletion by value - Searching - Displaying - Counting nodes - Reversing
the list - Finding the middle node

Positions are **zero-based**: - Position `0` means the first node. -
Position `1` means the second node. - Position `2` means the third node.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. INSERTION AT THE BEGINNING
    def insert_at_beginning(self, data):
        new_node = Node(data)

        # New node points to the old first node.
        new_node.next = self.head

        # Head now points to the new node.
        self.head = new_node

    # 2. INSERTION AT THE END
    def insert_at_end(self, data):
        new_node = Node(data)

        # If the list is empty, new node becomes the head.
        if self.head is None:
            self.head = new_node
            return

        current = self.head

        # Move to the last node.
        while current.next is not None:
            current = current.next

        # Last node points to the new node.
        current.next = new_node

    # 3. INSERTION AT A GIVEN POSITION (ZERO-BASED)
    def insert_at_position(self, data, position):
        if position < 0:
            raise IndexError("Position cannot be negative")

        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head

        # Stop at the node just before the required position.
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next

        if current is None:
            raise IndexError("Position out of range")

        new_node.next = current.next
        current.next = new_node

    # 4. INSERT AFTER THE FIRST OCCURRENCE OF A VALUE
    def insert_after_value(self, target, data):
        current = self.head

        while current is not None:
            if current.data == target:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return True

            current = current.next

        return False  # Target was not found.

    # 5. INSERT BEFORE THE FIRST OCCURRENCE OF A VALUE
    def insert_before_value(self, target, data):
        if self.head is None:
            return False

        if self.head.data == target:
            self.insert_at_beginning(data)
            return True

        current = self.head

        while current.next is not None:
            if current.next.data == target:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return True

            current = current.next

        return False

    # 6. DELETION FROM THE BEGINNING
    def delete_from_beginning(self):
        if self.head is None:
            return None

        deleted_value = self.head.data
        self.head = self.head.next
        return deleted_value

    # 7. DELETION FROM THE END
    def delete_from_end(self):
        if self.head is None:
            return None

        # Only one node exists.
        if self.head.next is None:
            deleted_value = self.head.data
            self.head = None
            return deleted_value

        current = self.head

        # Stop at the second-last node.
        while current.next.next is not None:
            current = current.next

        deleted_value = current.next.data
        current.next = None
        return deleted_value

    # 8. DELETION AT A GIVEN POSITION (ZERO-BASED)
    def delete_at_position(self, position):
        if position < 0:
            raise IndexError("Position cannot be negative")

        if self.head is None:
            return None

        if position == 0:
            return self.delete_from_beginning()

        current = self.head

        # Stop at the node before the one to delete.
        for _ in range(position - 1):
            if current.next is None:
                raise IndexError("Position out of range")
            current = current.next

        if current.next is None:
            raise IndexError("Position out of range")

        deleted_value = current.next.data
        current.next = current.next.next
        return deleted_value

    # 9. DELETION BY VALUE (FIRST OCCURRENCE)
    def delete_by_value(self, target):
        if self.head is None:
            return False

        if self.head.data == target:
            self.delete_from_beginning()
            return True

        current = self.head

        while current.next is not None:
            if current.next.data == target:
                current.next = current.next.next
                return True

            current = current.next

        return False

    # 10. SEARCHING
    def search(self, target):
        current = self.head
        position = 0

        while current is not None:
            if current.data == target:
                return position

            current = current.next
            position += 1

        return -1

    # 11. DISPLAY
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        values = []

        while current is not None:
            values.append(str(current.data))
            current = current.next

        print(" -> ".join(values) + " -> None")

    # 12. COUNT NODES
    def count_nodes(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    # 13. REVERSE THE LINKED LIST
    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next  # Save the next node.
            current.next = previous   # Reverse the link.
            previous = current        # Move previous forward.
            current = next_node      # Move current forward.

        self.head = previous

    # 14. FIND THE MIDDLE NODE
    def find_middle(self):
        if self.head is None:
            return None

        slow = self.head
        fast = self.head

        # Fast moves two nodes; slow moves one.
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow.data
```

## 3.6 Understanding insertion operations

### A. Insert at the beginning

Suppose the list is:

```text
10 -> 20 -> 30 -> None
```

Insert `5`.

Steps:

1. Create a new node containing `5`.
2. Make the new node point to the current head.
3. Update head to the new node.

```python
new_node.next = head
head = new_node
```

Result:

```text
5 -> 10 -> 20 -> 30 -> None
```

Time complexity: **O(1)**.

### B. Insert at the end

Suppose:

```text
10 -> 20 -> 30 -> None
```

Insert `40`.

Steps:

1. Create node `40`.
2. Start from the head.
3. Move until `current.next` is `None`.
4. Connect the last node to the new node.

```python
current.next = new_node
```

Result:

```text
10 -> 20 -> 30 -> 40 -> None
```

Time complexity without a tail reference: **O(n)**.

### C. Insert at a position

Insert `25` at position `2`:

```text
Before:
10 -> 20 -> 30 -> None

After:
10 -> 20 -> 25 -> 30 -> None
```

The important order is:

```python
new_node.next = current.next
current.next = new_node
```

First connect the new node to the node that used to follow `current`.
Then connect `current` to the new node.

If the order is reversed, the original remainder of the list can become
inaccessible.

### D. Insert after a value

Insert `25` after `20`:

```text
10 -> 20 -> 25 -> 30 -> None
```

Find the node containing `20`, then update two links:

```python
new_node.next = current.next
current.next = new_node
```

### E. Insert before a value

Insert `15` before `20`:

```text
10 -> 15 -> 20 -> 30 -> None
```

In a singly linked list, a node does not know its previous node.
Therefore, to insert before a target, traverse while checking
`current.next`.

---

## 3.7 Understanding deletion operations

### A. Delete from the beginning

Before:

```text
head
 |
 v
10 -> 20 -> 30 -> None
```

Operation:

```python
head = head.next
```

After:

```text
head
 |
 v
20 -> 30 -> None
```

The old first node is no longer part of the list. Python can later
reclaim it when no references remain.

Time complexity: **O(1)**.

### B. Delete from the end

Before:

```text
10 -> 20 -> 30 -> None
```

To delete `30`, we need the second-last node (`20`).

Operation:

```python
current.next = None
```

Result:

```text
10 -> 20 -> None
```

Why not simply use `current = current.next`? Because that only changes
the temporary reference, not the link in the list.

Time complexity: **O(n)**.

### C. Delete at a position

Delete position `1`:

```text
Before:
10 -> 20 -> 30 -> None

After:
10 -> 30 -> None
```

Find the node before the target and skip the target:

```python
current.next = current.next.next
```

### D. Delete by value

Delete the first node containing `20`:

```text
10 -> 20 -> 30 -> None
```

Find the predecessor and bypass the target:

```python
current.next = current.next.next
```

If the target is the head, update `head` separately.

---

# 4. Doubly Linked List (DLL)

## 4.1 Definition

A **doubly linked list** is a linked list in which every node contains:

1. Data
2. A reference to the next node (`next`)
3. A reference to the previous node (`prev`)

It supports traversal in both directions.

```text
None <- 10 <=> 20 <=> 30 -> None
         HEAD          TAIL
```

More precisely:

```text
+------+------+------+
| None |  10  | next | ---->
+------+------+------+
                 <---- +------+------+------+
                       | prev |  20  | next | ---->
                       +------+------+------+
                                        <---- +------+------+------+
                                              | prev |  30  | None |
                                              +------+------+------+
```

## 4.2 Node structure

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
```

Each node has: - `data`: stored value. - `prev`: previous node. -
`next`: next node.

## 4.3 Head and tail

A doubly linked list can maintain two references:

- `head`: first node.
- `tail`: last node.

For an empty list:

```python
self.head = None
self.tail = None
```

For a one-node list, both references point to the same node.

```text
head, tail
    |
    v
None <- 10 -> None
```

Maintaining `tail` makes insertion at the end O(1).

## 4.4 Complete doubly linked-list implementation

This implementation supports insertion and deletion at both ends, at
positions, before/after a value, searching, forward/backward display,
counting, and reversal.

```python
class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 1. INSERT AT BEGINNING
    def insert_at_beginning(self, data):
        new_node = DLLNode(data)

        if self.head is None:
            self.head = self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # 2. INSERT AT END
    def insert_at_end(self, data):
        new_node = DLLNode(data)

        if self.tail is None:
            self.head = self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    # 3. INSERT AT POSITION (ZERO-BASED)
    def insert_at_position(self, data, position):
        if position < 0:
            raise IndexError("Position cannot be negative")

        if position == 0:
            self.insert_at_beginning(data)
            return

        current = self.head

        for _ in range(position):
            if current is None:
                break
            current = current.next

        if current is None:
            if position == self.count_nodes():
                self.insert_at_end(data)
                return
            raise IndexError("Position out of range")

        new_node = DLLNode(data)
        previous_node = current.prev

        new_node.prev = previous_node
        new_node.next = current
        previous_node.next = new_node
        current.prev = new_node

    # 4. INSERT AFTER FIRST OCCURRENCE OF A VALUE
    def insert_after_value(self, target, data):
        current = self.head

        while current is not None:
            if current.data == target:
                if current is self.tail:
                    self.insert_at_end(data)
                    return True

                new_node = DLLNode(data)
                next_node = current.next

                new_node.prev = current
                new_node.next = next_node
                current.next = new_node
                next_node.prev = new_node
                return True

            current = current.next

        return False

    # 5. INSERT BEFORE FIRST OCCURRENCE OF A VALUE
    def insert_before_value(self, target, data):
        current = self.head

        while current is not None:
            if current.data == target:
                if current is self.head:
                    self.insert_at_beginning(data)
                    return True

                new_node = DLLNode(data)
                previous_node = current.prev

                new_node.prev = previous_node
                new_node.next = current
                previous_node.next = new_node
                current.prev = new_node
                return True

            current = current.next

        return False

    # 6. DELETE FROM BEGINNING
    def delete_from_beginning(self):
        if self.head is None:
            return None

        deleted_value = self.head.data

        if self.head is self.tail:
            self.head = self.tail = None
            return deleted_value

        self.head = self.head.next
        self.head.prev = None
        return deleted_value

    # 7. DELETE FROM END
    def delete_from_end(self):
        if self.tail is None:
            return None

        deleted_value = self.tail.data

        if self.head is self.tail:
            self.head = self.tail = None
            return deleted_value

        self.tail = self.tail.prev
        self.tail.next = None
        return deleted_value

    # 8. DELETE AT POSITION (ZERO-BASED)
    def delete_at_position(self, position):
        if position < 0:
            raise IndexError("Position cannot be negative")

        current = self.head

        for _ in range(position):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next

        if current is None:
            raise IndexError("Position out of range")

        if current is self.head:
            return self.delete_from_beginning()

        if current is self.tail:
            return self.delete_from_end()

        current.prev.next = current.next
        current.next.prev = current.prev
        return current.data

    # 9. DELETE BY VALUE (FIRST OCCURRENCE)
    def delete_by_value(self, target):
        current = self.head

        while current is not None:
            if current.data == target:
                if current is self.head:
                    self.delete_from_beginning()
                elif current is self.tail:
                    self.delete_from_end()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                return True

            current = current.next

        return False

    # 10. SEARCH
    def search(self, target):
        current = self.head
        position = 0

        while current is not None:
            if current.data == target:
                return position

            current = current.next
            position += 1

        return -1

    # 11. DISPLAY FORWARD
    def display_forward(self):
        current = self.head

        if current is None:
            print("List is empty")
            return

        values = []

        while current is not None:
            values.append(str(current.data))
            current = current.next

        print("None <-> " + " <-> ".join(values) + " <-> None")

    # 12. DISPLAY BACKWARD
    def display_backward(self):
        current = self.tail

        if current is None:
            print("List is empty")
            return

        values = []

        while current is not None:
            values.append(str(current.data))
            current = current.prev

        print("None <-> " + " <-> ".join(values) + " <-> None")

    # 13. COUNT NODES
    def count_nodes(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    # 14. REVERSE THE LIST
    def reverse(self):
        current = self.head

        while current is not None:
            # Swap the two links of every node.
            current.prev, current.next = current.next, current.prev
            current = current.prev  # Old next is now prev.

        self.head, self.tail = self.tail, self.head
```

## 4.5 Understanding DLL insertion

### A. Insert at beginning

Original:

```text
None <- 10 <-> 20 <-> 30 -> None
```

Insert `5`:

```text
None <- 5 <-> 10 <-> 20 <-> 30 -> None
```

Important link changes:

```python
new_node.next = self.head
self.head.prev = new_node
self.head = new_node
```

### B. Insert at end

Original:

```text
None <- 10 <-> 20 -> None
```

Insert `30`:

```python
new_node.prev = self.tail
self.tail.next = new_node
self.tail = new_node
```

Result:

```text
None <- 10 <-> 20 <-> 30 -> None
```

### C. Insert in the middle

Insert `25` between `20` and `30`.

Before:

```text
20 <-> 30
```

After:

```text
20 <-> 25 <-> 30
```

Four links must be updated:

```python
new_node.prev = previous_node
new_node.next = current
previous_node.next = new_node
current.prev = new_node
```

### D. Insert before/after a value

The key advantage over an SLL is that once the target node is found, its
previous node is directly available through `current.prev`.

---

## 4.6 Understanding DLL deletion

### A. Delete from beginning

For more than one node:

```python
self.head = self.head.next
self.head.prev = None
```

For a one-node list, both `head` and `tail` must become `None`.

### B. Delete from end

```python
self.tail = self.tail.prev
self.tail.next = None
```

Again, handle the one-node case separately.

### C. Delete a middle node

For:

```text
10 <-> 20 <-> 30
```

Delete `20`.

Update:

```python
current.prev.next = current.next
current.next.prev = current.prev
```

Result:

```text
10 <-> 30
```

A DLL requires more link updates than an SLL, but it can move backward
and directly access the predecessor of a node.

---

# 5. Circular Linked List (CLL)

## 5.1 Definition

A **circular linked list** is a linked list in which the last node links
back to the first node instead of pointing to `None`.

In a circular singly linked list:

```text
       +-------------------------+
       |                         |
       v                         |
10 -> 20 -> 30 ------------------+
^
|
HEAD
```

The last node's `next` points to `head`.

Therefore:

```python
last_node.next = head
```

There is no `None` at the end of a non-empty circular list.

## 5.2 Why is it called circular?

Because following the `next` references eventually brings you back to
the starting node.

This creates a loop.

## 5.3 Important difference from an SLL

Singly linked list:

```text
10 -> 20 -> 30 -> None
```

Circular singly linked list:

```text
10 -> 20 -> 30
^           |
|___________|
```

In a circular list, this condition is not suitable for normal traversal:

```python
while current is not None:
```

The traversal never reaches `None` because the links form a cycle.

Instead, stop when you return to the head.

## 5.4 Complete circular singly linked-list implementation

This implementation maintains both `head` and `tail`, making insertion
at the beginning and end O(1).

```python
class CLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 1. INSERT AT BEGINNING
    def insert_at_beginning(self, data):
        new_node = CLLNode(data)

        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node
            return

        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head

    # 2. INSERT AT END
    def insert_at_end(self, data):
        new_node = CLLNode(data)

        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node
            return

        new_node.next = self.head
        self.tail.next = new_node
        self.tail = new_node

    # 3. INSERT AT POSITION (ZERO-BASED)
    def insert_at_position(self, data, position):
        if position < 0:
            raise IndexError("Position cannot be negative")

        if position == 0:
            self.insert_at_beginning(data)
            return

        current = self.head
        index = 0

        while index < position - 1 and current is not self.tail:
            current = current.next
            index += 1

        if index != position - 1:
            raise IndexError("Position out of range")

        if current is self.tail:
            self.insert_at_end(data)
            return

        new_node = CLLNode(data)
        new_node.next = current.next
        current.next = new_node

    # 4. INSERT AFTER FIRST OCCURRENCE OF A VALUE
    def insert_after_value(self, target, data):
        if self.head is None:
            return False

        current = self.head

        while True:
            if current.data == target:
                if current is self.tail:
                    self.insert_at_end(data)
                    return True

                new_node = CLLNode(data)
                new_node.next = current.next
                current.next = new_node
                return True

            current = current.next

            if current is self.head:
                break

        return False

    # 5. INSERT BEFORE FIRST OCCURRENCE OF A VALUE
    def insert_before_value(self, target, data):
        if self.head is None:
            return False

        if self.head.data == target:
            self.insert_at_beginning(data)
            return True

        previous = self.head
        current = self.head.next

        while current is not self.head:
            if current.data == target:
                new_node = CLLNode(data)
                new_node.next = current
                previous.next = new_node
                return True

            previous = current
            current = current.next

        return False

    # 6. DELETE FROM BEGINNING
    def delete_from_beginning(self):
        if self.head is None:
            return None

        deleted_value = self.head.data

        if self.head is self.tail:
            self.head = self.tail = None
            return deleted_value

        self.head = self.head.next
        self.tail.next = self.head
        return deleted_value

    # 7. DELETE FROM END
    def delete_from_end(self):
        if self.head is None:
            return None

        if self.head is self.tail:
            deleted_value = self.head.data
            self.head = self.tail = None
            return deleted_value

        previous = self.head

        while previous.next is not self.tail:
            previous = previous.next

        deleted_value = self.tail.data
        self.tail = previous
        self.tail.next = self.head
        return deleted_value

    # 8. DELETE AT POSITION (ZERO-BASED)
    def delete_at_position(self, position):
        if position < 0:
            raise IndexError("Position cannot be negative")

        if self.head is None:
            return None

        if position == 0:
            return self.delete_from_beginning()

        previous = self.head
        current = self.head.next
        index = 1

        while current is not self.head and index < position:
            previous = current
            current = current.next
            index += 1

        if current is self.head:
            raise IndexError("Position out of range")

        if current is self.tail:
            return self.delete_from_end()

        previous.next = current.next
        return current.data

    # 9. DELETE BY VALUE (FIRST OCCURRENCE)
    def delete_by_value(self, target):
        if self.head is None:
            return False

        if self.head.data == target:
            self.delete_from_beginning()
            return True

        previous = self.head
        current = self.head.next

        while current is not self.head:
            if current.data == target:
                if current is self.tail:
                    self.tail = previous
                    self.tail.next = self.head
                else:
                    previous.next = current.next

                return True

            previous = current
            current = current.next

        return False

    # 10. SEARCH
    def search(self, target):
        if self.head is None:
            return -1

        current = self.head
        position = 0

        while True:
            if current.data == target:
                return position

            current = current.next
            position += 1

            if current is self.head:
                break

        return -1

    # 11. DISPLAY
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        values = []

        while True:
            values.append(str(current.data))
            current = current.next

            if current is self.head:
                break

        print(" -> ".join(values) + " -> (back to head)")

    # 12. COUNT NODES
    def count_nodes(self):
        if self.head is None:
            return 0

        count = 0
        current = self.head

        while True:
            count += 1
            current = current.next

            if current is self.head:
                break

        return count
```

## 5.5 Circular-list traversal explained

A standard SLL traversal uses:

```python
while current is not None:
    print(current.data)
    current = current.next
```

A circular traversal uses:

```python
current = head

if current is not None:
    while True:
        print(current.data)
        current = current.next

        if current is head:
            break
```

Why?

- Start at the head.
- Visit each node.
- Move forward.
- When the reference becomes the head again, one complete cycle has
  finished.

An alternative is:

```python
current = head

while current.next is not head:
    print(current.data)
    current = current.next

print(current.data)
```

This prints the last node separately.

## 5.6 Circular doubly linked list

A **circular doubly linked list** combines both ideas:

- Each node has `next` and `prev`.
- The last node's `next` points to the head.
- The head's `prev` points to the last node.

```text
       <-----------------------------+
       |                             |
HEAD -> 10 <-> 20 <-> 30 <-----------+
       +-----------------------------+
```

More precisely, the circular relationships are:

```python
tail.next = head
head.prev = tail
```

For a one-node circular doubly linked list:

```python
node.next = node
node.prev = node
```

It supports forward and backward circular traversal. Its insertion and
deletion logic combines the DLL's two-way link updates with the CLL's
circular boundary updates.

---

# 6. Insertion and Deletion: Pointer Logic to Memorise

This section summarises the most important link changes.

## 6.1 Singly linked list

---

  Operation                           Essential link update

---

  Insert at beginning                 `new.next = head`, then
                                      `head = new`

  Insert after a node                 `new.next = current.next`, then
                                      `current.next = new`

  Insert at end                       `last.next = new`

  Delete beginning                    `head = head.next`

  Delete after a predecessor          `predecessor.next = target.next`

Delete end                          `second_last.next = None`
------------------------------------

## 6.2 Doubly linked list

---

  Operation                           Essential link update

---

  Insert at beginning                 `new.next = head`; `head.prev = new`;
                                      update `head`

  Insert at end                       `new.prev = tail`; `tail.next = new`;
                                      update `tail`

  Insert in middle                    Update four links

  Delete beginning                    Move `head`; set new
                                      `head.prev = None`

  Delete end                          Move `tail`; set new
                                      `tail.next = None`

Delete middle                       `current.prev.next = current.next`;
                                      `current.next.prev = current.prev`
--------------------------------------

## 6.3 Circular singly linked list

---

  Operation                           Essential link update

---

  Insert at beginning                 New node points to old head; update
                                      head; `tail.next = head`

  Insert at end                       New node points to head; old tail
                                      points to new node; update tail

  Delete beginning                    Update head; `tail.next = head`

  Delete end                          Find predecessor of tail; update
                                      tail; `tail.next = head`

Delete middle                       Previous node skips the target
------------------------------------------------------------------

**Critical rule:** Every operation that changes the head of a circular
list must preserve `tail.next == head`.

---

# 7. Time and Space Complexity

Let `n` be the number of nodes.

## 7.1 Singly linked list

---

  Operation                          Time complexity Reason

---

  Access by position                            O(n) Must traverse from
                                                     head

  Search                                        O(n) May inspect every
                                                     node

  Insert at beginning                           O(1) Only a few reference
                                                     updates

  Insert at end                                 O(n) Must find the last
                                                     node if no tail is
                                                     maintained

  Insert at end with                            O(1) Tail is already known
  tail

  Insert after known                            O(1) Direct link update
  node

  Insert at position                            O(n) Must reach the
                                                     position

  Delete beginning                              O(1) Move head

  Delete end                                    O(n) Must find second-last
                                                     node

  Delete after known                            O(1) Direct link update
  predecessor

  Display/traversal                             O(n) Visit every node

Reverse                                       O(n) Visit every node once
------------------------------------------------------------------------

## 7.2 Doubly linked list

  Operation                            Time complexity

---

  Search                                          O(n)
  Insert at beginning                             O(1)
  Insert at end with tail                         O(1)
  Insert before/after a known node                O(1)
  Insert at position                              O(n)
  Delete beginning                                O(1)
  Delete end with tail                            O(1)
  Delete a known node                             O(1)
  Delete by value                                 O(n)
  Forward/backward display                        O(n)

## 7.3 Circular singly linked list

With both `head` and `tail` maintained:

  Operation               Time complexity

---

  Insert at beginning                O(1)
  Insert at end                      O(1)
  Search                             O(n)
  Insert at position                 O(n)
  Delete beginning                   O(1)
  Delete end                         O(n)
  Delete by value                    O(n)
  Display                            O(n)

## 7.4 Space complexity

A linked list containing `n` nodes uses **O(n)** space.

Each node stores data and one or more references: - SLL: one `next`
reference. - DLL: `prev` and `next` references. - Circular SLL: one
`next` reference. - Circular DLL: `prev` and `next` references.

A DLL generally needs more memory per node than an SLL because it stores
an additional reference.

---

# 8. Advantages and Disadvantages

## 8.1 Singly linked list

**Advantages** - Dynamic size. - Insertion at the beginning is O(1). -
Does not require shifting elements. - Uses one link per node.

**Disadvantages** - Traversal is only forward. - Cannot directly access
the previous node. - Searching and indexing require traversal. -
Deleting the last node requires finding its predecessor.

## 8.2 Doubly linked list

**Advantages** - Traversal in both directions. - Easy to move to the
previous node. - Deletion of a known node is O(1), provided its links
are valid. - Efficient insertion at both ends when head and tail are
maintained.

**Disadvantages** - More memory per node. - More references must be
updated. - More opportunities for pointer/link errors.

## 8.3 Circular linked list

**Advantages** - Traversal can continue cyclically. - Useful when
processing should repeat from the beginning. - With a tail reference,
insertion at the beginning and end can be O(1). - No `None` at the end
of a non-empty list.

**Disadvantages** - Incorrect traversal conditions can cause infinite
loops. - Boundary cases require care. - Some operations need special
handling when the list has one node.

---

# 9. Real-World Applications

---

  Type                                Applications

---

  Singly linked list                  Simple dynamic collections,
                                      adjacency lists in graphs,
                                      hash-table chaining

  Doubly linked list                  Browser navigation history,
                                      undo/redo systems, LRU cache

  Circular linked list                Round-robin CPU scheduling,
                                      repeating playlists, turn-based
                                      games

Circular doubly linked list         Applications that need repeated
                                      forward and backward navigation
---------------------------------------------------------------------

These are common conceptual applications; real software may use other
data structures or combinations of structures.

---

# 10. Common Mistakes in Linked-list Programs

1. **Forgetting to update `head`:** inserting or deleting the first
   node requires updating the head reference.
2. **Forgetting the empty-list case:** operations behave differently
   when `head is None`.
3. **Ignoring the one-node case:** after deleting the only node, both
   `head` and `tail` must be `None`.
4. **Losing the rest of the list:** when inserting, connect the new
   node to the remaining list before replacing the predecessor's link.
5. **Changing `current` instead of a node's link:**
   `current = current.next` only moves a temporary reference.
6. **Using `None` as the stopping condition in a circular list:** a
   non-empty circular list never reaches `None`.
7. **Forgetting DLL's backward link:** every `next` update may require
   a corresponding `prev` update.
8. **Forgetting the circular connection:** after changing the head or
   tail, maintain `tail.next = head`.
9. **Off-by-one position errors:** decide whether positions are
   zero-based or one-based. These notes use zero-based positions.
10. **Not handling a missing search value:** return a clear result such
    as `-1` or `False`.

---

# 11. Testing the Implementations

Run the following examples after defining the classes above.

## 11.1 Singly linked list test

```python
sll = SinglyLinkedList()

sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.display()
# 10 -> 20 -> 30 -> None

sll.insert_at_beginning(5)
sll.display()
# 5 -> 10 -> 20 -> 30 -> None

sll.insert_at_position(15, 2)
sll.display()
# 5 -> 10 -> 15 -> 20 -> 30 -> None

sll.insert_after_value(20, 25)
sll.insert_before_value(10, 7)
sll.display()
# 5 -> 7 -> 10 -> 15 -> 20 -> 25 -> 30 -> None

print("Position of 25:", sll.search(25))
print("Number of nodes:", sll.count_nodes())

sll.delete_from_beginning()
sll.delete_from_end()
sll.delete_at_position(1)
sll.delete_by_value(20)
sll.display()

sll.reverse()
sll.display()
print("Middle:", sll.find_middle())
```

## 11.2 Doubly linked list test

```python
dll = DoublyLinkedList()

dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.display_forward()
# None <-> 10 <-> 20 <-> 30 <-> None

dll.display_backward()
# None <-> 30 <-> 20 <-> 10 <-> None

dll.insert_at_beginning(5)
dll.insert_at_position(15, 2)
dll.insert_after_value(20, 25)
dll.insert_before_value(10, 7)

dll.display_forward()
dll.display_backward()

print("Position of 25:", dll.search(25))
print("Count:", dll.count_nodes())

dll.delete_from_beginning()
dll.delete_from_end()
dll.delete_at_position(1)
dll.delete_by_value(20)

dll.display_forward()
dll.reverse()
dll.display_forward()
```

## 11.3 Circular singly linked list test

```python
cll = CircularSinglyLinkedList()

cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)
cll.display()
# 10 -> 20 -> 30 -> (back to head)

cll.insert_at_beginning(5)
cll.insert_at_position(15, 2)
cll.insert_after_value(20, 25)
cll.insert_before_value(10, 7)
cll.display()

print("Position of 25:", cll.search(25))
print("Count:", cll.count_nodes())

cll.delete_from_beginning()
cll.delete_from_end()
cll.delete_at_position(1)
cll.delete_by_value(20)
cll.display()
```

---

# 12. Dry Run: How Links Change

Suppose we start with an empty SLL and perform:

1. Insert `10` at end.
2. Insert `20` at end.
3. Insert `5` at beginning.
4. Insert `15` at position `2`.
5. Delete the node at position `1`.

   Step Operation                 Result

---

       0 Initial                   Empty
       1 Insert 10 at end          `10 -> None`
       2 Insert 20 at end          `10 -> 20 -> None`
       3 Insert 5 at beginning     `5 -> 10 -> 20 -> None`
       4 Insert 15 at position 2   `5 -> 10 -> 15 -> 20 -> None`
       5 Delete position 1         `5 -> 15 -> 20 -> None`

The most important part is understanding which reference changes at each
step.

---

# 13. Frequently Asked Viva and Examination Questions

### Q1. What is a linked list?

A linked list is a linear data structure made of nodes, where each node
stores data and one or more references connecting it to other nodes.

### Q2. What is the difference between an array and a linked list?

An array supports direct indexing, while a linked list generally
requires traversal to reach a particular position. Linked lists make
insertion and deletion at known locations easier because elements do not
need to be shifted.

### Q3. What is the head of a linked list?

The head is the reference to the first node.

### Q4. What does `None` represent in an SLL?

It indicates that a node has no next node. It is normally found in the
last node's `next` field.

### Q5. Why is insertion at the beginning O(1)?

Because only the new node's `next` reference and the head reference need
to be updated.

### Q6. Why is searching O(n)?

Because in the worst case, every node must be checked.

### Q7. What is the main difference between SLL and DLL?

An SLL stores only the next reference, while a DLL stores both previous
and next references.

### Q8. Why does a DLL use more memory?

Every node stores an additional `prev` reference.

### Q9. What is a circular linked list?

A linked list in which the last node points back to the first node.

### Q10. Why can a circular-list traversal become infinite?

Because there is no `None` at the end. The traversal must explicitly
stop when it returns to the starting node.

### Q11. Can a circular linked list contain only one node?

Yes. Its `next` reference points to itself.

### Q12. What is the advantage of maintaining a tail?

It allows direct access to the last node. This makes insertion at the
end O(1) in the implementations described here.

### Q13. What is the difference between deleting by position and deleting by value?

Deletion by position removes the node at a specified index. Deletion by
value searches for a matching value and removes its first occurrence.

### Q14. Can a linked list be reversed?

Yes. In an SLL, reverse each `next` link. In a DLL, swap the `next` and
`prev` references of every node and swap head and tail.

### Q15. Which linked list supports traversal in both directions?

A doubly linked list and a circular doubly linked list.

---

# 14. Quick Revision Sheet

---

  Feature           SLL               DLL               Circular SLL

---

  References per    `next`            `prev`, `next`    `next`
  node

  Forward traversal Yes               Yes               Yes

  Backward          No                Yes               No
  traversal

  Last node points  `None`            `None`            `head`
  to

  Head's previous   Not present       `None`            Not present
  link

  Can loop forever  Less likely       Less likely       Yes
  if traversal is
  wrong?

Extra memory      Baseline          More              Baseline
  compared with SLL
-------------------

### Essential code patterns

```python
# SLL: move forward
current = current.next

# SLL: insert after current
new_node.next = current.next
current.next = new_node

# SLL: delete after current
current.next = current.next.next

# DLL: connect two neighbouring nodes
left.next = right
right.prev = left

# Circular SLL: maintain circular connection
tail.next = head

# Circular DLL: maintain both circular connections
tail.next = head
head.prev = tail
```

### Complexity to remember

- Search: O(n)
- Display: O(n)
- Access by index: O(n)
- Insert at beginning: O(1)
- Delete at beginning: O(1)
- SLL insertion at end: O(n) without tail, O(1) with tail
- DLL insertion at end: O(1) with tail
- DLL deletion of a known node: O(1)
- Reverse: O(n)

---

# 15. Practice Problems

Try solving these without looking at the code first.

## Beginner

1. Create a singly linked list containing `10, 20, 30`.
2. Display all elements.
3. Count the total number of nodes.
4. Search for `20` and return its position.
5. Insert `5` at the beginning.
6. Insert `40` at the end.

## Intermediate

7. Insert a value at a given position.
8. Delete a node by value.
9. Delete the last node.
10. Find the middle node.
11. Reverse a singly linked list.
12. Display a doubly linked list backward.

## Advanced

13. Implement a circular singly linked list with a tail reference.
14. Delete the last node of a circular singly linked list.
15. Check whether a linked list contains a cycle.
16. Find the nth node from the end.
17. Remove duplicate values from a linked list.
18. Merge two sorted singly linked lists.

---

# 16. Final Conceptual Summary

A linked list is a collection of nodes connected through references.

- **Singly linked list:** each node points to the next node. The last
  node points to `None`.
- **Doubly linked list:** each node points to both the previous and
  next nodes. It supports forward and backward traversal.
- **Circular singly linked list:** the last node points back to the
  head. Traversal must stop when it returns to the starting node.
- **Circular doubly linked list:** combines two-way links with
  circular connections.

The central skill in linked-list programming is not memorising every
method. It is understanding how references change.

For every insertion or deletion, ask: 1. Which node comes before the
changed position? 2. Which node comes after it? 3. Which reference(s)
must be updated? 4. Does the operation change `head` or `tail`? 5. Is
the list empty or does it contain only one node? 6. If it is circular,
is the circular connection still intact?

If you can answer these questions, you can construct most linked-list
operations yourself.
