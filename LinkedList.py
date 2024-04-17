class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0
    def insertAtFirst(self,data):
        temp = Node(data)
        self.count = self.count+1
        if(self.head==None):
            self.tail = temp
        else:
            temp.next = self.head
        self.head = temp
        
    def inserAtLast(self,data):
        temp = Node(data)
        self.count = self.count+1
        if(self.head==None):
            self.head = temp
        else:
            self.tail.next = temp
        self.tail = temp
        
    def insertAtIndex(self,data,idx):
        temp = Node(data)
        t = self.head
        if(idx==0):
            self.insertAtFirst(data)
            return
        if(idx ==self.size()):
            self.inserAtLast(data)
            return
        if(idx<0 or idx>self.size()):
            print("Please Enter valid index osition ! ")
            return
        for i in range(1,idx):
            t = t.next
        temp.next = t.next
        t.next = temp
        self.count = self.count+1
        
    def displayList(self):
        temp = self.head
        print("[ ",end="")
        while(temp!=None):
            print(temp.data,end=" ")
            temp = temp.next
        print("]")
        
    def deleteAtLast(self):
        if(self.size()==1):
            self.head=None
            self.tail=None
            self.count = self.count-1
            return
        temp  = self.head
        while(temp.next.next!=None):
            temp = temp.next
        temp.next = None
        self.tail = temp
        self.count = self.count-1
        
    def deleteAtFirst(self):
        if(self.size()==1):
            self.head = None
            self.tail = None
            self.count = self.count-1
            return
        self.head = self.head.next
        self.count = self.count-1
        
    def deleteAtIndex(self,idx):
        if(idx==0):
            self.deleteAtFirst()
            return
        if(idx==self.size()-1):
            self.deleteAtLast
            return
        if(idx<0 or idx>self.size()):
            print("Please Enter valid Index !")
            return
        temp = self.head
        for i in range(1,idx):
            temp = temp.next
        temp.next = temp.next.next
        self.count = self.count-1
        
    def size(self):
        return self.count
    
    def get(self,idx):
        if(idx==0):
            return self.head.data
        if(idx==self.size()-1):
            return self.tail.data
        if(idx>=1 and idx<self.size()-1):
            temp = self.head.next
            for i in range(1,idx):
               temp = temp.next
            return temp.data
        else:
            print("Invalid Index ! ")
            
l1 = Linked_List()
l1.inserAtLast(1)
l1.inserAtLast(2)
l1.inserAtLast(3)
l1.inserAtLast(4)
l1.inserAtLast(5)
l1.inserAtLast(6)

l2 = Linked_List()
l2.inserAtLast(9)
l2.inserAtLast(2)
l2.inserAtLast(5)
l2.inserAtLast(8)
l2.inserAtLast(6)
l2.inserAtLast(4)
l2.inserAtLast(1)

l3 = Linked_List()
for i in range(l1.size()):
    count = 0
    for j in range(l2.size()):
        if(l1.get(i)==l2.get(j)):
            l3.inserAtLast(l1.get(i))
            count = 1
    if(count==0):
        l3.inserAtLast(l1.get(i))
        
for i in range(l2.size()):
    count = 0
    for j in range(l1.size()):
        if(l2.get(i)==l1.get(j)):
            count = 1
    if(count==0):
        l3.inserAtLast(l2.get(i))
                   
l3.displayList()


