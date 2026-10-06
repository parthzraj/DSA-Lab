size=int(input("enter the size of the queue:"))
deque=[]

def push_front(data):
    if len(deque)==size:
        print("deque is full")
    elif len(deque)==0:
          deque.append(data)
    else:
       deque.insert(0,data)
def push_back(data):
    if len(deque)==size:
            print("deque is full")
    else:
        deque.append(data)
def pop_front():

    if len(deque)==0:
              print("deque is empty")
    else:
             deque.pop()
def pop_back():
    if len(deque)==0:
                print("deque is empty")
    else:
               deque.pop()
def front():
    if len(deque)==0:
                      print("deque is empty")
    else:
        print(deque[0])
def display():
        if len(deque)==0:
            print("deque is empty")
        else:
            print(deque)
       

    

while True:
    print("1.push_front\n2.push_back\n3.pop_front\n4.pop_back\n5.front\n6.display\n7.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        data=int(input("enter the element to push:"))
        push_front(data)
    elif choice==2:
        data=int(input("enter the element to push:"))
        push_back(data)
    elif choice==3:
        pop_front()
    elif choice==4:
          pop_back()
    elif choice==5:
        front()
    elif choice==6:
        display()
    elif choice==7:
        break
    else:
        print("invalid choice")