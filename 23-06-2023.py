class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class CLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        if self.head is None:
            print("CLL is empty,add ele")
        else:
            temp=self.head
            print(temp.data,"-->",end=" ")
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data,"-->",end=" ")
            print(temp.next.data)
            
            
    def insert_begin(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
            self.tail.next=self.head
        else:
            newnode.next=self.head
            self.head=newnode
            self.tail.next=self.head
            
            
    def insert_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
            self.tail.next=newnode
        else:
            self.tail.next=newnode
            newnode.next=self.head
    def insert_pos(self,pos,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
            self.tail.next=self.head
        else:
            if pos==1:
                inserr_begin(data)
            else:
                temp=self.head
                for i in range(1,pos-1):
                    temp=temp.next
                newnode.next=temp.next
                temp.next=newnode
    def delete_begin(self):
        if self.head is None:
            print("cll is not existing")
        else:  
            temp=self.head
            self.head=temp.next
            temp.next=None
            self.tail.next=self.head
    def delete_end(self):
        temp1=sself.head.next
        prev=self.head
        while temp1 !=self.head:
            temp1=self.head.next
            prev=self.head
            temp1.next= None
            self.tail=prev
            self.tail.next=self.head
        else:  
            temp=self.head
            self.head=temp.next
            temp.next=None
            self.tail.next=self.head
            
    def delete_pos(self,pos):
        if self.head is None:
            print("CLL is empty")
        elif pos==1:
            delete_end()
        else:
            temp = self.head.next
            prev = self.head
            for i in range(1,pos-1):
                temp = temp.next
                prev = prev.next
            prev.next = temp.next
            
    
    
    
cl=CLL()
node_1=Node(10)
node_2=Node(20)
node_3=Node(30)

cl.head=node_1
cl.tail=node_1
cl.tail.next=cl.head

node_1.next=node_2
cl.tail=node_2
cl.tail.next=cl.head

node_2.next=node_3
cl.tail=node_3
cl.tail.next=cl.head
cl.insert_begin(40)
cl.display()
cl.insert_end(50)


#cl.delete_begin()
cl.insert_pos(2,"vinnu")
#cl.display()
#cl.delete_pos(3)
cl.display()