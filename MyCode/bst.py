# Binary Search Tree (BST)
# Insertion and Searching

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert a node into BST
def insert(root, data):
    if root is None:
        return Node(data)

    if root.data == data:
        return root

    if data < root.data:
        root.left = insert(root.left, data)

    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# Search for an element in BST
def search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True

    elif key < root.data:
        return search(root.left, key)

    else:
        return search(root.right, key)


# Inorder traversal
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


# Main program
root = None

elements = [50, 30, 70, 20, 40, 60, 80]

for value in elements:
    root = insert(root, value)

print("BST Inorder Traversal:")
inorder(root)

key = int(input("\nEnter element to search: "))

if search(root, key):
    print(key, "is found in BST")
else:
    print(key, "is not found in BST")