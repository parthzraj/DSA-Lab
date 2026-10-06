class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class circular_linked_list:
    def __init__(self):
        self.head=None

    def insert(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            new_node.next=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head
    def delete(self,data):
        if self.head==None:
            print("list is empty")
        else:
            if self.head.data==data:
                if self.head==self.head.next:
                     self.head=None
                else:
                     temp=self.head
                     while temp.next!=self.head:
                          temp=temp.next
                     temp.next=self.head.next
                     self.head=self.head.next
                print("deleted")
                return 
            temp=self.head
            while temp.next!=self.head:
                if temp.next.data==data:
                    temp.next=temp.next.next
                    print("node deleted successfully")
                    return 
                temp=temp.next
    def search(self,data):
        if self.head==None:
                    print("list is empty")
        else:
                temp=self.head
                position=1
                if self.head.data==data:
                     print("the node is found at",position)
                     return 
                while temp.next!=self.head:
                        if temp.data==data:
                            print("the node is found at",position)
                            return 
                        temp=temp.next
                        position+=1
                print("element not found.")
    def display(self):
         if self.head==None:
                print("list is empty")
         else:
            temp=self.head
            while temp.next!=self.head:
                print(temp.data,end="->")         
                temp=temp.next
            print(temp.data)
cll=circular_linked_list()
while True:
    print("\n1.push\n2.pop\n3.highest_priority_element\n4.display\n5.exit")
    choice=int(input("enter the choice:"))
    if choice==1:
        data=int(input("enter the element:"))
        cll.insert(data)
    elif choice==2:
        data=int(input("enter the element:"))
        cll.delete(data)
    elif choice==3:
        data=int(input("enter the element:"))
        cll.search(data)
    elif choice==4:
        cll.display()
    elif choice==5:
        break
    else:
        print("invalid choice")