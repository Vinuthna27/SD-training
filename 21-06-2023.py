#stack operations
stc=[]
def push_element():
    if len(stc)==n:
        print("stack is full")
    else:
        element=input("enter element ")
        stc.append(element)
        print(stc)

def pop_element():
    if not stc:
        print("stack is empty")
    else:
        e=stc.pop()
        print("removed")
        print(stc)

n=int(input("enter the size"))
while True:
    print("select option 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push_element()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("enter correct option")

# Queue operations
def enqueque():
    if len(queue)==n:
        print("stack is full")
    else:
        element=input("enter element ")
        queue.append(element)
        print(queue)
        
def dequeue():
    if not queue:
        print("stack is empty")
    else:
        e=queue.pop(0)
        print(e,"removed")
        print(queue)
        
n=int(input("enter the size"))
while True:
    print("select option 1.enqueue 2.dequeue 3.quit")
    choice=int(input())
    if choice==1:
        enqueque()
    elif choice==2:
        dequeue()
    elif choice==3:
        break
    else:
        print("enter correct option")
        
