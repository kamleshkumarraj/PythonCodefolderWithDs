class Queue:
    front  = -1
    rear = -1
    l = [None]*10
    count = 0
    def enqueue(self,data):
        if(self.rear==len(self.l)-1):
            print("Your Queue is already full ! ")
        elif(self.rear==-1 and self.front==-1):
            self.front=self.rear=0
            self.l[0] = data
            self.count = self.count+1
        else:
            self.rear = self.rear+1
            self.l[self.rear] = data
            self.count = self.count+1
    def dequeue(self):
        if(self.rear==-1 and self.rear==self.front):
            print("condition Underflow becuase queue is empty ! ")
        else:
            k = self.l[self.front]
            self.front = self.front+1
            self.count = self.count-1
            return k
    def size(self):
        return self.count
    def display(self):
        if(self.front==-1 and self.rear==-1):
            print("Given queue is empty : ")
        else:
            print("[ ",end="")
            for i in range(self.front , self.rear+1):
                print(self.l[i],end=" ")
            print(" ]")
    def capacity(self):
        return len(self.l)
q1 = Queue()
q1.enqueue(89)
q1.enqueue(45)
q1.enqueue(32)
q1.enqueue(12)
q1.enqueue(56)
q1.display()