class Node:
     def __init__(self,data):
         self.data=data
         self.next=None

class singly_linked_list:
 def __init__(self):
        self.head=None

 def insert(self,data):
    new_node=Node(data)
    if self.head==None:
        self.head=new_node
    else:
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node
        print("Element inserted successfully.")
 def delete(self,data):
    if self.head==None:
        print("list is empty.")
    else:
        if self.head.data==data:
            self.head=self.head.next
            print("Node deleted successfully.")
            return
        temp=self.head
        while temp.next!=None:
            if temp.next.data==data:
                temp.next=temp.next.next
                print("Node deleted successfully.")
                return
            temp=temp.next
        print("Node not found.")
 def search(self,data):
        if self.head==None:
            print("list is empty.")
        else:
            temp=self.head
            position=1
            while temp!=None:
                if temp.data==data:
                    print("Node found as position ", position)
                    return
                temp=temp.next
                position+=1
            print("Node not found.")
 def display(self):
    if self.head==None:
            print("list is empty.")
    else:
        temp=self.head
        while temp!=None:
                print(temp.data,end="->")
                temp=temp.next
sll=singly_linked_list()
while True:
    print("\n1.push\n2.pop\n3.highest_priority_element\n4.display\n5.exit")
    choice=int(input("enter the choice:"))
    if choice==1:
        data=int(input("enter the element:"))
        sll.insert(data)
    elif choice==2:
        data=int(input("enter the element:"))
        sll.delete(data)
    elif choice==3:
        data=int(input("enter the element:"))
        sll.search(data)
    elif choice==4:
        sll.display()
    elif choice==5:
        break
    else:
        print("invalid choice")