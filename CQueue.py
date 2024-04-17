class CircularQueue:
    front = -1
    rear = -1
    arr = [None]*5
    count = 0
    def enqueue(self,data):
        if(len(self.arr)==self.size()):
            print("Capacity of Queue is Full ! ")
        elif(self.size()==0):
            self.rear = self.front = 0
            self.arr[self.rear] = data
            self.count = self.count+1
        elif(self.rear>=0 and  self.rear<len(self.arr)-1):
             self.rear = self.rear+1
             self.arr[self.rear] = data
             self.count = self.count+1
        else:
            self.arr[self.rear]  =data
            self.rear = 0
            self.count = self.count+1
            
    def dequeue(self):
        if(self.size()==0):
            print("Condition underFolw Becuase Queue is already empty ! ")
        elif(self.front>=0 and self.front<len(self.arr)-1):
            self.front = self.front+1
            self.count = self.count-1
        else:
            self.front = 0
            self.count = self.count-1
            
    def display(self):
        if(self.size()==0):
            print("[ ]")
        elif(self.front<=self.rear):
            print("[ ",end=" ")
            for i in range(self.front,self.rear+1):
                print(self.arr[i],end=" ")
            print("]")
        else:
            print("[ ",end=" ")
            for i in range(self.front,len(self.arr)):
                print(self.arr[i],end=" ")
            for i in range(self.rear+1):
                print(self.arr[i],end=" ")
            print("]")       
                
            
    def size(self):
        return self.count
               
cq = CircularQueue()
cq.enqueue(45)
cq.enqueue(23)
cq.enqueue(21)
cq.enqueue(32)
cq.enqueue(31)
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
# cq.dequeue()

cq.display()

cq.enqueue(67)
cq.enqueue(34)
cq.enqueue(21)
cq.enqueue(22)
cq.enqueue(45)

# cq.dequeue()
cq.display()