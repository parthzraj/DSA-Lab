#push ,pop , display ,peek
stack=[]
size=int(input("enter the size of the stack:"))
def push(data):
    if len(stack)==size:
        print("stack overflow")
    else:
        stack.append(data)
def pop():
    if len(stack)==0:
        print("stack underflow")
    else:
        stack.pop()
def peek():
    if len(stack)==0:
        print("stack is empty")
    else:
        print("top element is:",stack[-1])
def display():
    if len(stack)==0:
        print("stack is empty")
    else:
        print("elements in stack are:",stack)

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