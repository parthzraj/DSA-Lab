# Complete Notes on Linked Lists in Python

## Singly Linked List, Doubly Linked List, and Circular Linked List

> These notes cover the concepts from beginner level, pointer/reference
> logic, diagrams, Python implementations, all common insertion and
> deletion operations, searching, traversal/display, edge cases,
> complexity analysis, comparisons, and practice questions.

------------------------------------------------------------------------

# 1. Introduction to Linked Lists

## 1.1 What is a linked list?

A **linked list** is a linear data structure in which elements (called
**nodes**) are stored in separate objects. Each node stores:

1.  **Data** -- the value we want to store.
2.  **Link / pointer / reference** -- a reference to another node.

Unlike an array or Python list, linked-list nodes do not need to occupy
adjacent memory locations. The links connect the nodes and establish
their order.

Example:

``` text
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

``` python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

Explanation:

-   `class Node`: defines a blueprint for creating nodes.
-   `self.data = data`: stores the value.
-   `self.next = None`: initially, the node does not point to another
    node.
-   `self` refers to the current object.

Creating nodes manually:

``` python
first = Node(10)
second = Node(20)
third = Node(30)

first.next = second
second.next = third

head = first
```

The resulting structure is:

``` text
head
 |
 v
10 -> 20 -> 30 -> None
```

**Important:** `head` is not the data itself. It is a reference to the
first node.

## 1.3 Important terms

  -----------------------------------------------------------------------
  Term                                Meaning
  ----------------------------------- -----------------------------------
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
  -----------------------------------------------------------------------

## 1.4 Why do we need linked lists?

A normal Python list is implemented using a dynamic array. It provides
fast indexing, but inserting or deleting an element near the beginning
can require shifting other elements.

A linked list connects nodes through references. Insertion or deletion
can be efficient when the required node or its predecessor is already
known.

### Linked list vs array/Python list

  -----------------------------------------------------------------------
  Feature                 Array / Python list     Linked list
  ----------------------- ----------------------- -----------------------
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
  -----------------------------------------------------------------------

Python's built-in `list` is not a linked list. The classes in these
notes implement linked lists manually.

------------------------------------------------------------------------

# 2. Types of Linked Lists

The three main types covered here are:

1.  Singly Linked List
2.  Doubly Linked List
3.  Circular Linked List

A circular linked list can itself be singly circular or doubly circular.
Both forms are explained.

------------------------------------------------------------------------

# 3. Singly Linked List (SLL)

## 3.1 Definition

A **singly linked list** is a linked list in which every node
contains: - Data - A reference to the next node

Each node points only in the forward direction.

``` text
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

``` python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

Each node has: - `data`: the stored value. - `next`: the reference to
the next node.

## 3.3 The head reference

`head` stores the reference to the first node.

``` python
head = None
```

This represents an empty list.

After inserting `10`:

``` text
head
 |
 v
10 -> None
```

After inserting `20` at the end:

``` text
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

``` python
current = head

while current is not None:
    print(current.data)
    current = current.next
```

How it works:

1.  Start at `head`.
2.  Process the current node's data.
3.  Move to the next node using `current.next`.
4.  Repeat until `current` becomes `None`.

Never confuse these two operations:

``` python
current = current.next
```

This moves the temporary reference forward.

``` python
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

``` python
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

``` text
10 -> 20 -> 30 -> None
```

Insert `5`.

Steps:

1.  Create a new node containing `5`.
2.  Make the new node point to the current head.
3.  Update head to the new node.

``` python
new_node.next = head
head = new_node
```

Result:

``` text
5 -> 10 -> 20 -> 30 -> None
```

Time complexity: **O(1)**.

### B. Insert at the end

Suppose:

``` text
10 -> 20 -> 30 -> None
```

Insert `40`.

Steps:

1.  Create node `40`.
2.  Start from the head.
3.  Move until `current.next` is `None`.
4.  Connect the last node to the new node.

``` python
current.next = new_node
```

Result:

``` text
10 -> 20 -> 30 -> 40 -> None
```

Time complexity without a tail reference: **O(n)**.

### C. Insert at a position

Insert `25` at position `2`:

``` text
Before:
10 -> 20 -> 30 -> None

After:
10 -> 20 -> 25 -> 30 -> None
```

The important order is:

``` python
new_node.next = current.next
current.next = new_node
```

First connect the new node to the node that used to follow `current`.
Then connect `current` to the new node.

If the order is reversed, the original remainder of the list can become
inaccessible.

### D. Insert after a value

Insert `25` after `20`:

``` text
10 -> 20 -> 25 -> 30 -> None
```

Find the node containing `20`, then update two links:

``` python
new_node.next = current.next
current.next = new_node
```

### E. Insert before a value

Insert `15` before `20`:

``` text
10 -> 15 -> 20 -> 30 -> None
```

In a singly linked list, a node does not know its previous node.
Therefore, to insert before a target, traverse while checking
`current.next`.

------------------------------------------------------------------------

## 3.7 Understanding deletion operations

### A. Delete from the beginning

Before:

``` text
head
 |
 v
10 -> 20 -> 30 -> None
```

Operation:

``` python
head = head.next
```

After:

``` text
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

``` text
10 -> 20 -> 30 -> None
```

To delete `30`, we need the second-last node (`20`).

Operation:

``` python
current.next = None
```

Result:

``` text
10 -> 20 -> None
```

Why not simply use `current = current.next`? Because that only changes
the temporary reference, not the link in the list.

Time complexity: **O(n)**.

### C. Delete at a position

Delete position `1`:

``` text
Before:
10 -> 20 -> 30 -> None

After:
10 -> 30 -> None
```

Find the node before the target and skip the target:

``` python
current.next = current.next.next
```

### D. Delete by value

Delete the first node containing `20`:

``` text
10 -> 20 -> 30 -> None
```

Find the predecessor and bypass the target:

``` python
current.next = current.next.next
```

If the target is the head, update `head` separately.

------------------------------------------------------------------------

# 4. Doubly Linked List (DLL)

## 4.1 Definition

A **doubly linked list** is a linked list in which every node contains:

1.  Data
2.  A reference to the next node (`next`)
3.  A reference to the previous node (`prev`)

It supports traversal in both directions.

``` text
None <- 10 <=> 20 <=> 30 -> None
         HEAD          TAIL
```

More precisely:

``` text
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

``` python
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

-   `head`: first node.
-   `tail`: last node.

For an empty list:

``` python
self.head = None
self.tail = None
```

For a one-node list, both references point to the same node.

``` text
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

``` python
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

``` text
None <- 10 <-> 20 <-> 30 -> None
```

Insert `5`:

``` text
None <- 5 <-> 10 <-> 20 <-> 30 -> None
```

Important link changes:

``` python
new_node.next = self.head
self.head.prev = new_node
self.head = new_node
```

### B. Insert at end

Original:

``` text
None <- 10 <-> 20 -> None
```

Insert `30`:

``` python
new_node.prev = self.tail
self.tail.next = new_node
self.tail = new_node
```

Result:

``` text
None <- 10 <-> 20 <-> 30 -> None
```

### C. Insert in the middle

Insert `25` between `20` and `30`.

Before:

``` text
20 <-> 30
```

After:

``` text
20 <-> 25 <-> 30
```

Four links must be updated:

``` python
new_node.prev = previous_node
new_node.next = current
previous_node.next = new_node
current.prev = new_node
```

### D. Insert before/after a value

The key advantage over an SLL is that once the target node is found, its
previous node is directly available through `current.prev`.

------------------------------------------------------------------------

## 4.6 Understanding DLL deletion

### A. Delete from beginning

For more than one node:

``` python
self.head = self.head.next
self.head.prev = None
```

For a one-node list, both `head` and `tail` must become `None`.

### B. Delete from end

``` python
self.tail = self.tail.prev
self.tail.next = None
```

Again, handle the one-node case separately.

### C. Delete a middle node

For:

``` text
10 <-> 20 <-> 30
```

Delete `20`.

Update:

``` python
current.prev.next = current.next
current.next.prev = current.prev
```

Result:

``` text
10 <-> 30
```

A DLL requires more link updates than an SLL, but it can move backward
and directly access the predecessor of a node.

------------------------------------------------------------------------

# 5. Circular Linked List (CLL)

## 5.1 Definition

A **circular linked list** is a linked list in which the last node links
back to the first node instead of pointing to `None`.

In a circular singly linked list:

``` text
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

``` python
last_node.next = head
```

There is no `None` at the end of a non-empty circular list.

## 5.2 Why is it called circular?

Because following the `next` references eventually brings you back to
the starting node.

This creates a loop.

## 5.3 Important difference from an SLL

Singly linked list:

``` text
10 -> 20 -> 30 -> None
```

Circular singly linked list:

``` text
10 -> 20 -> 30
^           |
|___________|
```

In a circular list, this condition is not suitable for normal traversal:

``` python
while current is not None:
```

The traversal never reaches `None` because the links form a cycle.

Instead, stop when you return to the head.

## 5.4 Complete circular singly linked-list implementation

This implementation maintains both `head` and `tail`, making insertion
at the beginning and end O(1).

``` python
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

``` python
while current is not None:
    print(current.data)
    current = current.next
```

A circular traversal uses:

``` python
current = head

if current is not None:
    while True:
        print(current.data)
        current = current.next

        if current is head:
            break
```

Why?

-   Start at the head.
-   Visit each node.
-   Move forward.
-   When the reference becomes the head again, one complete cycle has
    finished.

An alternative is:

``` python
current = head

while current.next is not head:
    print(current.data)
    current = current.next

print(current.data)
```

This prints the last node separately.

## 5.6 Circular doubly linked list

A **circular doubly linked list** combines both ideas:

-   Each node has `next` and `prev`.
-   The last node's `next` points to the head.
-   The head's `prev` points to the last node.

``` text
       <-----------------------------+
       |                             |
HEAD -> 10 <-> 20 <-> 30 <-----------+
       +-----------------------------+
```

More precisely, the circular relationships are:

``` python
tail.next = head
head.prev = tail
```

For a one-node circular doubly linked list:

``` python
node.next = node
node.prev = node
```

It supports forward and backward circular traversal. Its insertion and
deletion logic combines the DLL's two-way link updates with the CLL's
circular boundary updates.

------------------------------------------------------------------------

# 6. Insertion and Deletion: Pointer Logic to Memorise

This section summarises the most important link changes.

## 6.1 Singly linked list

  -----------------------------------------------------------------------
  Operation                           Essential link update
  ----------------------------------- -----------------------------------
  Insert at beginning                 `new.next = head`, then
                                      `head = new`

  Insert after a node                 `new.next = current.next`, then
                                      `current.next = new`

  Insert at end                       `last.next = new`

  Delete beginning                    `head = head.next`

  Delete after a predecessor          `predecessor.next = target.next`

  Delete end                          `second_last.next = None`
  -----------------------------------------------------------------------

## 6.2 Doubly linked list

  -------------------------------------------------------------------------
  Operation                           Essential link update
  ----------------------------------- -------------------------------------
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
  -------------------------------------------------------------------------

## 6.3 Circular singly linked list

  -----------------------------------------------------------------------
  Operation                           Essential link update
  ----------------------------------- -----------------------------------
  Insert at beginning                 New node points to old head; update
                                      head; `tail.next = head`

  Insert at end                       New node points to head; old tail
                                      points to new node; update tail

  Delete beginning                    Update head; `tail.next = head`

  Delete end                          Find predecessor of tail; update
                                      tail; `tail.next = head`

  Delete middle                       Previous node skips the target
  -----------------------------------------------------------------------

**Critical rule:** Every operation that changes the head of a circular
list must preserve `tail.next == head`.

------------------------------------------------------------------------

# 7. Time and Space Complexity

Let `n` be the number of nodes.

## 7.1 Singly linked list

  ------------------------------------------------------------------------
  Operation                          Time complexity Reason
  --------------------- ---------------------------- ---------------------
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
  ---------------------------------- -----------------
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
  --------------------- -----------------
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

------------------------------------------------------------------------

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

------------------------------------------------------------------------

# 9. Real-World Applications

  -----------------------------------------------------------------------
  Type                                Applications
  ----------------------------------- -----------------------------------
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
  -----------------------------------------------------------------------

These are common conceptual applications; real software may use other
data structures or combinations of structures.

------------------------------------------------------------------------

# 10. Common Mistakes in Linked-list Programs

1.  **Forgetting to update `head`:** inserting or deleting the first
    node requires updating the head reference.
2.  **Forgetting the empty-list case:** operations behave differently
    when `head is None`.
3.  **Ignoring the one-node case:** after deleting the only node, both
    `head` and `tail` must be `None`.
4.  **Losing the rest of the list:** when inserting, connect the new
    node to the remaining list before replacing the predecessor's link.
5.  **Changing `current` instead of a node's link:**
    `current = current.next` only moves a temporary reference.
6.  **Using `None` as the stopping condition in a circular list:** a
    non-empty circular list never reaches `None`.
7.  **Forgetting DLL's backward link:** every `next` update may require
    a corresponding `prev` update.
8.  **Forgetting the circular connection:** after changing the head or
    tail, maintain `tail.next = head`.
9.  **Off-by-one position errors:** decide whether positions are
    zero-based or one-based. These notes use zero-based positions.
10. **Not handling a missing search value:** return a clear result such
    as `-1` or `False`.

------------------------------------------------------------------------

# 11. Testing the Implementations

Run the following examples after defining the classes above.

## 11.1 Singly linked list test

``` python
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

``` python
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

``` python
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

------------------------------------------------------------------------

# 12. Dry Run: How Links Change

Suppose we start with an empty SLL and perform:

1.  Insert `10` at end.
2.  Insert `20` at end.
3.  Insert `5` at beginning.
4.  Insert `15` at position `2`.
5.  Delete the node at position `1`.

    Step Operation                 Result
  ------ ------------------------- -------------------------------
       0 Initial                   Empty
       1 Insert 10 at end          `10 -> None`
       2 Insert 20 at end          `10 -> 20 -> None`
       3 Insert 5 at beginning     `5 -> 10 -> 20 -> None`
       4 Insert 15 at position 2   `5 -> 10 -> 15 -> 20 -> None`
       5 Delete position 1         `5 -> 15 -> 20 -> None`

The most important part is understanding which reference changes at each
step.

------------------------------------------------------------------------

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

------------------------------------------------------------------------

# 14. Quick Revision Sheet

  -----------------------------------------------------------------------
  Feature           SLL               DLL               Circular SLL
  ----------------- ----------------- ----------------- -----------------
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
  -----------------------------------------------------------------------

### Essential code patterns

``` python
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

-   Search: O(n)
-   Display: O(n)
-   Access by index: O(n)
-   Insert at beginning: O(1)
-   Delete at beginning: O(1)
-   SLL insertion at end: O(n) without tail, O(1) with tail
-   DLL insertion at end: O(1) with tail
-   DLL deletion of a known node: O(1)
-   Reverse: O(n)

------------------------------------------------------------------------

# 15. Practice Problems

Try solving these without looking at the code first.

## Beginner

1.  Create a singly linked list containing `10, 20, 30`.
2.  Display all elements.
3.  Count the total number of nodes.
4.  Search for `20` and return its position.
5.  Insert `5` at the beginning.
6.  Insert `40` at the end.

## Intermediate

7.  Insert a value at a given position.
8.  Delete a node by value.
9.  Delete the last node.
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

------------------------------------------------------------------------

# 16. Final Conceptual Summary

A linked list is a collection of nodes connected through references.

-   **Singly linked list:** each node points to the next node. The last
    node points to `None`.
-   **Doubly linked list:** each node points to both the previous and
    next nodes. It supports forward and backward traversal.
-   **Circular singly linked list:** the last node points back to the
    head. Traversal must stop when it returns to the starting node.
-   **Circular doubly linked list:** combines two-way links with
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
