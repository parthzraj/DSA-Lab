queue=[]
def heapify(queue):
    for i in range(1,len(queue)):
        smallest=i
        parent=(smallest-1)//2
        while smallest>0:
            if queue[parent]>queue[smallest]:
                queue[smallest],queue[parent]=queue[parent],queue[smallest]
                smallest=parent
                parent=(smallest-1)//2
            else:
                break
    print(queue)


def push(data):
    queue.append(data)
    heapify(queue)
def pop():
    if len(queue)==0:
                print("empty")
    else:
        queue.pop(0)
    heapify(queue)
def peek():
    if len(queue)==0:
            print("empty")
    else:
        print(queue[0])
def display():
    if len(queue)==0:
        print("empty")
    else:
        print(queue)
while True:
    print("1.push\n2.pop\n3.peek\n4.display\n5.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        data=int(input("enter the element to push:"))
        push(data)
    elif choice==2:
        pop()
    elif choice==3:
        peek()
    elif choice==4:
        display()
    elif choice==5:
        break
    else:
        print("invalid choice")