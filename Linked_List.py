class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertAtLast(self , data):
        temp = Node(data)
        if(self.head==None):
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
    def disply(self):
        temp = self.head
        print("[ ",end="")
        while(temp!=None):
            print(temp.data,end=" ")
            temp = temp.next
        print(']')
list = Linked_List()
list.insertAtLast(12)
list.insertAtLast(14)
list.insertAtLast(16)
list.insertAtLast(17)
list.insertAtLast(18)
list.disply()

               