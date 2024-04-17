class Stack:
    list1 = [None]*100
    top = -1
    count = 0
    def push(self,data):
        self.top = self.top+1
        self.list1[self.top] = data
        self.count = self.count+1
    def pop(self):
        k = self.list1[self.top]
        self.top = self.top-1
        self.count = self.count-1
        return k
    def peek(self):
        return  self.list1[self.top]
    def size(Self):
        return Self.count
    def IsEmpty(self):
        if(self.top==-1): return True
        else: return False
    def display(self):
        for i in range(self.top+1):
            print(self.list1[i],end=" ")
str = input("Enter your expression in Infix : ")
valueStack = Stack()
operatorStack = Stack()
for i in str:
    k = ord(i)
    if(k>=48 and k<=57):
        k = k-48
        k = int(k)
        valueStack.push(k)
    elif(operatorStack.IsEmpty):
        operatorStack.push(i) 
    elif(i=='-' or i=='+'):
        while(operatorStack.size()!=0):
            v2 = valueStack.pop()
            v1 = valueStack.pop()
            o = operatorStack.pop()
            if(o=='+'): valueStack.push(v1+v2)
            if(o=='-'): valueStack.push(v1-v2)
            if(o=='*'): valueStack.push(v1*v2)
            if(o=='/'): valueStack.push(v1/v2)
            
    elif(i=='*' or i=='/'):
        v2 = valueStack.pop()
        v1 = valueStack.pop()
        o = operatorStack.peek()
        if(o=='*' or o=='/'):
            if(o=='*'): valueStack.push(v1*v2)
            if(o=='/'): valueStack.push(v1/v2)
            operatorStack.pop()
        else:
            operatorStack.push(i)
while(operatorStack.size()!=0):
    v2 = valueStack.pop()
    v1 = valueStack.pop()
    print(type(valueStack.pop()))
    o = operatorStack.pop()
    a = v1+v2
    b = v1-v2
    c = v1*v2
    d = v1/v2
    if(o=='+'): valueStack.push(a)
    if(o=='-'): valueStack.push(b)
    if(o=='*'): valueStack.push(c)
    if(o=='/'): valueStack.push(d)
print("Our Final Answer = ",valueStack.peek())                
            
        
   