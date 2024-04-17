class DoublyQueue:
    front  = -1
    rear = -1
    l = [None]*10
    count = 0
    def insertAtRear(self,data):
        if(self.size()==len(self.l)):
            print("Capacity is full !")
            return
        if(self.size()==0):
            self.front=self.rear=0
            self.l[self.rear] = data
            self.count = self.count+1
        else:
            self.rear = self.rear+1
            self.l[self.rear] = data
            self.count = self.count+1
    
    def insertAtFront(self,data):
        if(self.size()==len(self.l)):
            print("Capacity is full !")
        elif(self.front>0):
            self.front = self.front-1
            self.l[self.front] = data
            self.count = self.count+1
        else:
            self.front = len(self.l)-1
            self.l[self.front] = data
            self.count = self.count+1
            
    def deleteAtFront(self):
        if(self.size==0):
            print("Queue is already empty !")
            return
        if(self.front>=0 and self.front<=len(self.l)-1):
            self.front = self.front+1
            self.count = self.count-1
    
    def deleteAtRear(self):
        if(self.size()==0):
            print("Queue is already empty !")
            return
        if(self.rear>=0 and self.rear<=len(self.l)-1):
            self.rear = self.rear-1
            self.count = self.count-1
            
    def displayQueue(self):
        if(self.size()==0):
            print("[ ]")
            return
        print("[ ",end="")
        if(self.front>=self.rear):
            for i in range(self.front,len(self.l)):
                print(self.l[i],end=" ")
            for i in range(self.rear+1):
                print(self.l[i],end=" ")
        else:
            for i in range(self.front , self.rear+1):
                print(self.l[i],end=" ")
        print("]")            
            
        
    def size(self):
        return self.count

q = DoublyQueue()
n  =int(input("enter the number of the element "))
for i in range(n):
    n = int(input("if you want to insert in front then press 1 and for rear press 2 "))
    if(n==1):
        k = int(input("Enter data : "))
        q.insertAtFront(k)
    else:
        k = int(input("Enter data : "))
        q.insertAtRear(k)
q.displayQueue()       
p = int(input("if you want to delete then press 1 otherwise press 2 "))
if(p==1):
    n = int(input("Enter the number of element for delete : "))
    for i in range(n):
        s = int(input("for deleting from front press 1 and for rear press 2 "))
        if(s==1):
            q.deleteAtFront()
            q.displayQueue()
        if(s==2):
            q.deleteAtRear()
            q.displayQueue()
        
    
