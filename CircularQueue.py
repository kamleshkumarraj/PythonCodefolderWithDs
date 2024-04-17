class CircularQueue:
    front = -1
    rear = -1
    count = 0
    l = [None]*5
    def enqueue(self , data):
        if(self.size()==len(self.l)):
            print("You can't insert any value becuase queue is already full !")
        elif(self.size()==0):
            self.rear = self.front = 0
            self.l[0] = data
            self.count = self.count+1
        elif(self.rear>=0 and self.rear<len(self.l)-1):
            self.rear = self.rear+1
            self.l[self.rear] = data
            self.count = self.count+1
        elif(self.front>0 and self.rear==len(self.l)-1):
            self.rear = 0
            self.l[0] = data
            self.count = self.count+1

    def dequeue(self):
        if(self.size()==0):
            print("Given Queue is already empty !")
        elif(self.front>=0 and self.front<len(self.l)-1):
            self.front = self.front+1
            self.count = self.count-1
        elif(self.front==len(self.l)-1):
            self.front = 0
            self.count = self.count-1

    def display(self):
        if(self.size()==0):
            print("[ ]")
            return
        print("[ ",end="")
        if(self.front<=self.rear):
            for i in range(self.front , self.rear+1):
                print(self.l[i],end=" ")
        else:
            for i in range(self.front , len(self.l)):
                print(self.l[i],end=" ")
            for i in range(self.rear+1):
                print(self.l[i],end=" ")
        print("]")
                
                        
    def size(self):
        return self.count

cq = CircularQueue()
cq.enqueue(90)
cq.enqueue(34)
cq.enqueue(32)
cq.enqueue(12)
cq.enqueue(35)
cq.display()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.enqueue(78)
cq.enqueue(21)
cq.enqueue(22)
cq.enqueue(12)
cq.display()
