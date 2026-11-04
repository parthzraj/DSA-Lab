"""
============================================================
              INTRODUCTION TO TREE DATA STRUCTURE
============================================================

1. WHAT IS A TREE?
------------------
A Tree is a NON-LINEAR, HIERARCHICAL data structure that
consists of a collection of NODES connected through EDGES.

Unlike arrays, stacks and queues, where elements are
generally arranged sequentially, a tree stores data in
a hierarchical parent-child relationship.

A tree starts with one special node called the ROOT.

REAL-LIFE EXAMPLES:
- Folder and file organization in a computer.
- Family hierarchy.
- Organization structure of a company.
- HTML DOM structure.
- Decision-making systems.
- Database indexing.

EXAMPLE:

                  A                 <- ROOT
                /   \\
               B     C               <- CHILDREN OF A
              / \\   / \\
             D   E F   G             <- LEAF NODES

Here:
- A is the ROOT.
- B and C are children of A.
- A is the parent of B and C.
- D, E, F and G are leaf nodes.

2. IMPORTANT CHARACTERISTICS OF A TREE
---------------------------------------
- A tree is a NON-LINEAR data structure.
- It contains NODES and EDGES.
- It has exactly ONE ROOT in a rooted tree.
- Every node except the root has exactly ONE parent.
- A node can have zero or more children.
- A tree does not contain CYCLES.
- There must be exactly one path between any two nodes.
- A tree containing n nodes has exactly n - 1 edges.
- Every node is reachable from the root.

IMPORTANT:
A tree is a connected and acyclic graph.

3. BASIC TERMINOLOGIES OF TREE
------------------------------

A. NODE
-------
A node is an individual element that stores data in a tree.

Example:
In the tree A -> B, A and B are nodes.

B. ROOT NODE
------------
The topmost node of a tree is called the ROOT.

Example:
        A
       / \\
      B   C

A is the root node.

A tree has only ONE root.

C. PARENT NODE
--------------
A node that has one or more children is called a PARENT.

Example:
        A
       / \\
      B   C

A is the parent of B and C.

D. CHILD NODE
-------------
A node directly connected below another node is called
its CHILD.

Example:
        A
       / \\
      B   C

B and C are children of A.

E. SIBLINGS
-----------
Nodes that share the same parent are called SIBLINGS.

Example:
        A
       / \\
      B   C

B and C are siblings.

F. LEAF NODE / EXTERNAL NODE
----------------------------
A node that does not have any children is called a LEAF.

Example:
        A
       / \\
      B   C
     / \\
    D   E

C, D and E are leaf nodes.

G. INTERNAL NODE
----------------
A node that has at least one child is called an INTERNAL
NODE.

Example:
        A
       / \\
      B   C
     /
    D

A and B are internal nodes.
C and D are leaf nodes.

H. EDGE
-------
An edge is the connection between two nodes.

Example:
        A
       /
      B

The connection between A and B is an edge.

I. DEGREE OF A NODE
-------------------
The DEGREE of a node is the number of children it has.

Example:
        A
      / | \\
     B  C  D

Degree of A = 3
Degree of B = 0

J. DEGREE OF A TREE
-------------------
The maximum degree of any node in the tree is called
the DEGREE OF THE TREE.

Example:
If the maximum number of children of any node is 3,
then the degree of the tree is 3.

K. LEVEL
--------
Level represents the position of a node in the tree.

In this note, the root is considered to be at LEVEL 0.

Example:

             A             Level 0
           /   \\
          B     C          Level 1
         / \\   /
        D   E F            Level 2

L. DEPTH OF A NODE
------------------
Depth is the number of EDGES from the ROOT to that node.

Example:
             A
            /
           B
          /
         C

Depth of A = 0
Depth of B = 1
Depth of C = 2

M. HEIGHT OF A NODE
-------------------
Height is the number of EDGES in the longest downward
path from that node to a leaf.

- Height of a leaf node = 0.
- Height of a parent = 1 + maximum height of its children.

N. HEIGHT OF A TREE
-------------------
The height of a tree is the height of its ROOT.

It is the maximum number of edges from the root to
any leaf.

O. ANCESTORS
------------
All the nodes that appear on the path from the root to
a particular node are its ANCESTORS (excluding itself).

Example:
        A
       /
      B
     /
    C

Ancestors of C = A, B

P. DESCENDANTS
--------------
All nodes below a particular node are called its
DESCENDANTS (including children, grandchildren, etc.).

Example:
        A
       / \\
      B   C
     / \\
    D   E

Descendants of A = B, C, D, E

Q. SUBTREE
----------
A subtree is a smaller tree formed by a node and all
its descendants.

Example:
        A
       / \\
      B   C
     / \\
    D   E

The subtree rooted at B contains B, D and E.

R. FOREST
---------
A collection of DISJOINT TREES is called a FOREST.

If the root of a tree is removed, the remaining subtrees
form a forest.

============================================================
                  TYPES OF TREE
============================================================

4. GENERAL TREE
----------------
A General Tree is a tree in which a node can have ANY
NUMBER OF CHILDREN.

There is no fixed limit on the number of children.

EXAMPLE:

              A
          /   |   \\
         B    C    D
        / \\       /|\\
       E   F     G H I

Here:
- A has 3 children.
- B has 2 children.
- D has 3 children.

APPLICATIONS:
- File systems.
- Organization charts.
- HTML document structure.
- Family trees.

5. BINARY TREE
--------------
A Binary Tree is a tree in which each node can have
AT MOST TWO CHILDREN.

The two children are called:

1. LEFT CHILD
2. RIGHT CHILD

EXAMPLE:

              A
             / \\
            B   C
           / \\
          D   E

Here:
- A has left child B and right child C.
- B has left child D and right child E.
- C has no children.

IMPORTANT:
A binary tree can have:
- Zero children.
- One child.
- Two children.

It can NEVER have more than two children per node.

APPLICATIONS:
- Searching.
- Sorting.
- Expression evaluation.
- Decision-making systems.

6. FULL BINARY TREE (STRICT BINARY TREE)
----------------------------------------
A Full Binary Tree is a binary tree in which EVERY NODE
has either:

- ZERO children (leaf node), OR
- EXACTLY TWO children.

No node can have only ONE child.

EXAMPLE:

              A
             / \\
            B   C
           / \\
          D   E

This is a FULL BINARY TREE.

WHY?
- A has 2 children.
- B has 2 children.
- C, D and E have 0 children.

NOT A FULL BINARY TREE:

              A
             /
            B

WHY?
A has only ONE child.

IMPORTANT PROPERTY:
In a non-empty full binary tree:

Number of leaf nodes = Number of internal nodes + 1

7. COMPLETE BINARY TREE
-----------------------
A Complete Binary Tree is a binary tree in which:

- All levels except possibly the LAST level are completely
  filled.
- The last level must be filled from LEFT TO RIGHT.
- There must be no gaps between nodes at the last level.

EXAMPLE:

              A
             / \\
            B   C
           / \\
          D   E

This is a COMPLETE BINARY TREE.

WHY?
- Level 0 is completely filled.
- Level 1 is completely filled.
- The last level is filled from left to right.

NOT COMPLETE:

              A
             / \\
            B   C
               /
              D

WHY?
The last level has a gap on the left before node D.

APPLICATIONS:
- Binary Heap.
- Priority Queue.
- Heap Sort.

8. PERFECT BINARY TREE
----------------------
A Perfect Binary Tree is a binary tree in which:

- Every INTERNAL NODE has exactly TWO children.
- All LEAF NODES are at the SAME LEVEL.
- Every level is completely filled.

EXAMPLE:

                A
              /   \\
             B     C
            / \\   / \\
           D   E F   G

This is a PERFECT BINARY TREE.

IMPORTANT FORMULAS:

Maximum number of nodes at level L:

             2^L

Total number of nodes in a perfect binary tree
of height h:

             2^(h + 1) - 1

Number of leaf nodes:

             2^h

Number of internal nodes:

             2^h - 1

Example:
For height h = 2:

Total nodes = 2^(2 + 1) - 1
            = 8 - 1
            = 7

Leaf nodes = 2^2 = 4

Internal nodes = 2^2 - 1 = 3

9. BALANCED BINARY TREE
-----------------------
A Balanced Binary Tree is a tree whose height is kept
relatively small compared to the number of nodes.

The purpose is to prevent the tree from becoming too deep.

In an AVL-style balanced binary tree, the height difference
between the left and right subtrees of EVERY node must
not exceed 1.

EXAMPLE:

              A
             / \\
            B   C
           / \\   \\
          D   E   F

A balanced arrangement keeps the height small.

APPLICATIONS:
- Efficient searching.
- Database indexing.
- AVL Trees.
- Red-Black Trees.

IMPORTANT:
The exact definition of balance depends on the type of
balanced tree.

10. SKEWED BINARY TREE
----------------------
A Skewed Binary Tree is a binary tree in which every
internal node has ONLY ONE CHILD.

There are two types:

A. LEFT SKEWED BINARY TREE
--------------------------

             A
            /
           B
          /
         C
        /
       D

Every node has only a LEFT CHILD.

B. RIGHT SKEWED BINARY TREE
---------------------------

       A
        \\
         B
          \\
           C
            \\
             D

Every node has only a RIGHT CHILD.

IMPORTANT:
A skewed tree behaves similarly to a linked list.

Its height can become n - 1 for n nodes.

Searching can take O(n) time.

11. DEGENERATE BINARY TREE
--------------------------
A Degenerate Tree is a tree in which every parent node
has exactly ONE child.

It behaves like a linked list because there is only
one possible path from the root to the last node.

Example:

        A
         \\
          B
         /
        C
         \\
          D

IMPORTANT:
A skewed tree is a special type of degenerate tree
where the nodes consistently extend in one direction.

12. BINARY SEARCH TREE (BST)
----------------------------
A Binary Search Tree is a special type of binary tree
that follows a specific ORDERING PROPERTY.

RULES:

- All values in the LEFT SUBTREE are smaller than the
  node's value.
- All values in the RIGHT SUBTREE are greater than the
  node's value.
- Both left and right subtrees must also follow BST rules.

EXAMPLE:

                 50
               /    \\
             30      70
            / \\     / \\
           20  40   60  80

Here:
- 30 is smaller than 50.
- 70 is greater than 50.
- 20 and 40 are correctly placed in the left subtree.
- 60 and 80 are correctly placed in the right subtree.

SEARCHING EXAMPLE:
Search for 60:

Step 1:
Compare 60 with 50.
60 > 50, so move RIGHT.

Step 2:
Compare 60 with 70.
60 < 70, so move LEFT.

Step 3:
60 is found.

IMPORTANT:
BST is defined by its ordering property, not by its shape.

APPLICATIONS:
- Searching.
- Maintaining sorted data.
- Dictionaries and sets.
- Efficient insertion and deletion.

13. M-ARY TREE
--------------
An M-ARY TREE is a tree in which each node can have
AT MOST M CHILDREN.

Example:
A 3-ARY TREE allows a maximum of 3 children per node.

A 4-ARY TREE allows a maximum of 4 children per node.

A binary tree is a special case of an M-ARY tree
where M = 2.

============================================================
                TREE REPRESENTATION
============================================================

14. WHAT IS TREE REPRESENTATION?
--------------------------------
Tree Representation means storing the nodes and their
relationships in computer memory.

There are different ways to represent a tree.

The most common representations are:

1. Array Representation.
2. Linked Representation.
3. Parent Array Representation.
4. Children List Representation.
5. First Child - Next Sibling Representation.

15. ARRAY REPRESENTATION OF BINARY TREE
----------------------------------------
In Array Representation, tree nodes are stored inside
an ARRAY.

Each node is stored at a specific index.

For a COMPLETE BINARY TREE, array representation is
particularly efficient.

EXAMPLE TREE:

              A
             / \\
            B   C
           / \\ / \\
          D  E F  G

ARRAY REPRESENTATION:

Index:  0  1  2  3  4  5  6
Value:  A  B  C  D  E  F  G

IMPORTANT FORMULAS (0-BASED INDEXING):

For a node at index i:

LEFT CHILD:

             2 * i + 1

RIGHT CHILD:

             2 * i + 2

PARENT:

             (i - 1) // 2

EXAMPLE:
Node A is at index 0.

Left child:
2 * 0 + 1 = 1
Node B is at index 1.

Right child:
2 * 0 + 2 = 2
Node C is at index 2.

For node B at index 1:

Left child:
2 * 1 + 1 = 3
Node D is at index 3.

Right child:
2 * 1 + 2 = 4
Node E is at index 4.

NOTE:
These formulas work when the tree is stored using the
standard complete-tree array positions.

16. ARRAY REPRESENTATION USING 1-BASED INDEXING
-----------------------------------------------
Sometimes tree representation starts from index 1
instead of index 0.

For a node at index i:

LEFT CHILD:

             2 * i

RIGHT CHILD:

             2 * i + 1

PARENT:

             i // 2

EXAMPLE:

Index:  1  2  3  4  5  6  7
Value:  A  B  C  D  E  F  G

NOTE:
Always identify whether indexing starts from 0 or 1
before applying the formulas.

17. ADVANTAGES AND DISADVANTAGES OF ARRAY REPRESENTATION
--------------------------------------------------------

ADVANTAGES:
- Simple to implement.
- Direct access using indexes.
- Efficient for complete binary trees.
- No need to store explicit pointers.

DISADVANTAGES:
- Can waste memory for sparse trees.
- Insertion and deletion may be inconvenient.
- Fixed-size arrays can limit tree growth.
- Skewed trees may require many unused positions.

18. LINKED REPRESENTATION OF BINARY TREE
----------------------------------------
In Linked Representation, every node is stored as an
individual object.

Each node contains THREE main parts:

1. DATA  -> Stores the value.
2. LEFT  -> Stores the reference to the left child.
3. RIGHT -> Stores the reference to the right child.

STRUCTURE:

        +------+------+-------+
        | LEFT | DATA | RIGHT |
        +------+------+-------+

EXAMPLE:

              10
             /  \\
            20   30

Each node contains:
- Its own data.
- Reference to its left child.
- Reference to its right child.

If a child does not exist, its reference is None.

PYTHON IMPLEMENTATION:

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

CREATING A TREE:

root = Node(10)

root.left = Node(20)
root.right = Node(30)

root.left.left = Node(40)

TREE CREATED:

              10
             /  \\
            20   30
           /
          40

ACCESSING ELEMENTS:

root.data       -> 10
root.left.data  -> 20
root.right.data -> 30
root.left.left.data -> 40

IMPORTANT:
- root is the starting node of the tree.
- left stores the reference to the left child.
- right stores the reference to the right child.
- None indicates that a child does not exist.

19. ADVANTAGES AND DISADVANTAGES OF LINKED REPRESENTATION
---------------------------------------------------------

ADVANTAGES:
- Dynamic memory allocation.
- Tree can grow and shrink easily.
- No need to reserve unused array positions.
- Suitable for irregular and sparse trees.
- Insertion and deletion are flexible.

DISADVANTAGES:
- Extra memory is required for references.
- Direct index-based access is not available.
- Implementation is more complex than arrays.
- Traversal requires following references.

20. PARENT ARRAY REPRESENTATION
-------------------------------
In Parent Array Representation, every node stores the
INDEX of its parent.

The root node has no parent, so it is usually represented
using -1.

EXAMPLE TREE:

              A
             / \\
            B   C
           / \\
          D   E

ARRAY:

Node:    A   B   C   D   E
Index:   0   1   2   3   4
Parent: -1   0   0   1   1

EXPLANATION:

A -> -1 (Root has no parent)
B -> 0  (Parent is A)
C -> 0  (Parent is A)
D -> 1  (Parent is B)
E -> 1  (Parent is B)

ADVANTAGES:
- Simple representation.
- Easy to find the parent of a node.
- Useful for disjoint-set and tree-related problems.

DISADVANTAGES:
- Finding all children of a node requires searching
  the parent array.
- Does not directly store child relationships.

21. CHILDREN LIST REPRESENTATION
-------------------------------
In this representation, every node stores a LIST of
its children.

It is especially useful for GENERAL TREES where a node
can have any number of children.

EXAMPLE:

              A
          /   |   \\
         B    C    D
        / \\
       E   F

REPRESENTATION:

A -> [B, C, D]
B -> [E, F]
C -> []
D -> []
E -> []
F -> []

PYTHON EXAMPLE:

tree = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': [],
    'E': [],
    'F': []
}

ACCESSING CHILDREN:

tree['A'] gives ['B', 'C', 'D']

tree['B'] gives ['E', 'F']

ADVANTAGES:
- Suitable for general trees.
- Easy to find the children of a node.
- Flexible number of children.
- Easy to implement using Python dictionaries.

DISADVANTAGES:
- Finding the parent may require searching.
- Extra list storage is needed for child relationships.

22. FIRST CHILD - NEXT SIBLING REPRESENTATION
---------------------------------------------
This representation is used to represent GENERAL TREES
using only TWO references per node.

Each node contains:

1. DATA
2. FIRST CHILD
3. NEXT SIBLING

FIRST CHILD:
Points to the first child of the current node.

NEXT SIBLING:
Points to the next child of the SAME parent.

EXAMPLE:

              A
          /   |   \\
         B    C    D
        / \\
       E   F

REPRESENTATION:

A.first_child = B

B.next_sibling = C
C.next_sibling = D

B.first_child = E
E.next_sibling = F

IMPORTANT:
This representation converts a general tree into a
binary-link structure.

It is also called:
LEFT-CHILD RIGHT-SIBLING REPRESENTATION.

============================================================
              COMPARISON OF REPRESENTATIONS
============================================================

ARRAY REPRESENTATION:
- Stores nodes using array indexes.
- Best suited for complete binary trees.
- Child positions are calculated using formulas.
- Can waste memory in sparse trees.

LINKED REPRESENTATION:
- Uses nodes and references.
- Best suited for dynamically changing binary trees.
- Each node stores data, left and right references.
- Memory is allocated as needed.

PARENT ARRAY:
- Stores the parent index of each node.
- Easy to find the parent.
- Finding children requires searching.

CHILDREN LIST:
- Stores a list of children for every node.
- Suitable for general trees.
- Easy to find children.

FIRST CHILD - NEXT SIBLING:
- Uses two references per node.
- Suitable for general trees.
- Represents multiple children using linked relationships.

============================================================
              IMPORTANT EXAM POINTS
============================================================

1. A tree is a NON-LINEAR data structure.

2. A tree containing n nodes has n - 1 edges.

3. A node with zero children is called a LEAF NODE.

4. The topmost node is called the ROOT.

5. A node can have at most TWO children in a BINARY TREE.

6. A FULL BINARY TREE has either ZERO or TWO children
   for every node.

7. A COMPLETE BINARY TREE fills levels from LEFT TO RIGHT.

8. A PERFECT BINARY TREE has all levels completely filled.

9. A SKEWED TREE has only one child per internal node.

10. A BST follows:
    LEFT < ROOT < RIGHT

11. Array representation is efficient for COMPLETE
    BINARY TREES.

12. Linked representation uses DATA, LEFT and RIGHT.

13. A general tree can have any number of children.

14. A tree does not contain cycles.

15. There is exactly one path between any two nodes
    in a tree.

============================================================
                    QUICK REVISION
============================================================

TREE:
Non-linear hierarchical data structure.

ROOT:
Topmost node.

PARENT:
Node having children.

CHILD:
Node directly below a parent.

SIBLINGS:
Nodes having the same parent.

LEAF:
Node having zero children.

INTERNAL NODE:
Node having at least one child.

DEGREE:
Number of children of a node.

HEIGHT:
Longest downward path measured in edges.

DEPTH:
Distance from root measured in edges.

SUBTREE:
A node and all its descendants.

GENERAL TREE:
Any number of children.

BINARY TREE:
At most two children.

FULL BINARY TREE:
Every node has 0 or 2 children.

COMPLETE BINARY TREE:
Last level filled from left to right.

PERFECT BINARY TREE:
All levels completely filled.

BALANCED TREE:
Height is kept relatively small.

SKEWED TREE:
Every internal node has only one child,
consistently extending to the left or right.

BST:
Left subtree values are smaller and right subtree
values are greater than the root value.

ARRAY REPRESENTATION:
Stores nodes at calculated indexes.

LINKED REPRESENTATION:
Stores data and child references.

============================================================
"""

