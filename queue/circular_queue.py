queue=[]
size=int(input("enter the size of the circular queue"))
queue=[None]*size
rear=-1
front=-1
def enqueue(data):
    global front , rear
    if (rear+1)%size==front:
          print("queue is full")
    elif front==-1:
         front=0
         rear=0
         queue[front]=data
    else :
        rear=(rear+1)%size 
        queue[rear]=data
def dequeue():
    global front ,rear
    if queue[front]==None:
              print(" queue is empty")
    else:
        print("popped item",{queue[front]})
        front=(front+1)%size
def peek():
    if queue[front]==None:
              print(" queue is empty")
    else:
            print(queue[front])
def display():
     if queue[front]==None:
          print(" queue is empty")
     else:
        print(queue)

while True:
    print("1.enqueue\n2.dequeue\n3.peek\n4.display\n5.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        data=int(input("enter the element to push:"))
        enqueue(data)
    elif choice==2:
        dequeue()
    elif choice==3:
        peek()
    elif choice==4:
        display()
    elif choice==5:
        break
    else:
        print("invalid choice")



          