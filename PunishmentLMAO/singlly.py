class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # Insert at a specific position (1-based)
    def insert_position(self, data, position):
        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            self.insert_beginning(data)
            return

        new_node = Node(data)
        temp = self.head

        for i in range(position - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        temp.next = None

    # Delete from specific position (1-based)
    def delete_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            self.delete_beginning()
            return

        temp = self.head

        for i in range(position - 2):
            if temp.next is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next

    # Search an element
    def search(self, key):
        temp = self.head
        position = 1

        while temp is not None:
            if temp.data == key:
                print("Element found at position", position)
                return

            temp = temp.next
            position += 1

        print("Element not found")

    # Count nodes
    def count(self):
        temp = self.head
        total = 0

        while temp is not None:
            total += 1
            temp = temp.next

        print("Total nodes:", total)

    # Display linked list
    def display(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main program
ll = SinglyLinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

ll.display()

ll.insert_beginning(5)
ll.display()

ll.insert_position(15, 3)
ll.display()

ll.delete_beginning()
ll.display()

ll.delete_end()
ll.display()

ll.delete_position(2)
ll.display()

ll.search(20)
ll.count()