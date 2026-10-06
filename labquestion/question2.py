class Node:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.left = None
        self.right = None

def insert(root, roll_no, name):
    if root is None:
        return Node(roll_no, name)

    if roll_no < root.roll_no:
        root.left = insert(root.left, roll_no, name)

    elif roll_no > root.roll_no:
        root.right = insert(root.right, roll_no, name)

    else:
        print("Roll number already exists")

    return root

def search(root, roll_no):
    if root is None:
        return None

    if root.roll_no == roll_no:
        return root

    if roll_no < root.roll_no:
        return search(root.left, roll_no)

    return search(root.right, roll_no)

def preorder(root):
    if root is not None:
        print("Roll No:", root.roll_no, "| Name:", root.name)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print("Roll No:", root.roll_no, " Name:", root.name)
        inorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print("Roll No:", root.roll_no, " Name:", root.name)

root = None

while True:
    print("\n===== Student Record Management System =====")
    print("1. Add Student Record")
    print("2. Search Student")
    print("3. Display Preorder")
    print("4. Display Inorder")
    print("5. Display Postorder")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll_no = int(input("Enter student roll number: "))
        name = input("Enter student name: ")

        root = insert(root, roll_no, name)
        print("Student record added successfully.")

    elif choice == 2:
        roll_no = int(input("Enter roll number to search: "))

        result = search(root, roll_no)

        if result is not None:
            print("\nStudent Found!")
            print("Roll No:", result.roll_no)
            print("Name:", result.name)
        else:
            print("Student not found.")

    elif choice == 3:
        print("\n--- Preorder Traversal ---")
        preorder(root)

    elif choice == 4:
        print("\n--- Inorder Traversal ---")
        inorder(root)

    elif choice == 5:
        print("\n--- Postorder Traversal ---")
        postorder(root)

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
