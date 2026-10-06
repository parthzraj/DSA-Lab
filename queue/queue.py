queue=[]
size=int(input("enter the size of queue"))
def enqueue(data):
    if len(queue)==size:
        print("stack overflow")
    else:
        queue.append(data)
def dequeue():
    if len(queue)==0:
        print("stack underflow")
    else:
        queue.pop(0)
        print(queue)
def front():
    if len(queue)==0:
        print("stack underflow")
    else:
        print(queue[0])
def display():
    if len(queue)==0:
        print("stack underflow")
while True:
    print("1.enqueue\n2.dequeue\n3.front\n4.display\n5.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        data=int(input("enter the element to push:"))
        enqueue(data)
    elif choice==2:
        dequeue()
    elif choice==3:
        front()
    elif choice==4:
        display()
    elif choice==5:
        break
    else:
        print("invalid choice")

