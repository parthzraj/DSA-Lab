heap=[]
def push(data):
    heap.append(data)
    i=len(heap)-1
    while i>0:
        parent=(i-1)//2
        if heap[i]<heap[parent]:
             heap[i],heap[parent]=heap[parent],heap[i]
             i=parent
        else:
            break
def pop():
    if len(heap)==0:
        print("heap is empty")
    else:
        deleted=heap[0]
        heap[0]=heap[-1]
        heap.pop()
        i=0
        while True:
            left=2*i+1
            right=2*i+2
            smallest=i
            if left<len(heap) and heap[smallest]>heap[left]:
                heap[smallest],heap[left]=heap[left],heap[smallest]
                smallest=left
            if right<len(heap) and heap[smallest]>heap[right]:
                heap[smallest],heap[right]=heap[right],heap[smallest]
                smallest=right
            if smallest!=i:
                i=smallest
            else:
                break

def peek():
        if len(heap)==0:
                print("heap is empty")
        else:
            print("highest priority element:",heap[0])
def display():
        if len(heap)==0:
                        print("heap is empty")
        else:
            print("the heap is ",heap)




while True:
    print("\n1.push\n2.pop\n3.highest_priority_element\n4.display\n5.exit")
    choice=int(input("enter the choice:"))
    if choice==1:
        push(int(input("enter the element")))
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
