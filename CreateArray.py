class Array:
    def __init__(self):
        self.idx = 0
        self.count = 0
        self.l = [None]*5
    
    def add(self,data):
        self.l[self.idx] = data
        self.data = data
        self.idx = self.idx+1
        self.count = self.count+1
        if(self.count==len(self.l)):
            self.reinitialize()
            
    def reinitialize(self):
       oldArr = self.l
       self.l = [None]*(len(self.l)*2)
       self.idx = 0
       self.count = 0
       for i in oldArr:
           self.l[self.idx] = i
           self.idx = self.idx+1
           self.count = self.count+1
       
    def printArr(self):
        print("[ ",end="")
        for i in range(self.count):
            print(self.l[i],end=" ")
        print("]")
        
    def size(self):
        return self.count
        