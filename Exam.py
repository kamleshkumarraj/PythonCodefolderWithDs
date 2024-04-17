class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertAtLast(self,data):
        temp = Node(data)
        if(self.head==None):
            self.head = temp
            self.tail = temp
            return self.head
        else:
            self.tail.next = temp
            self.tail = temp
            return self.head
    def dispList(self):
        temp = self.head
        print("[",end=" ")
        while(temp!=None):
            print(temp.data,end=" ")
            temp = temp.next
        print("]")

def MergeTwoList(head1,head2,l3):
    while(head1!=None or head2!=None):
        l3.insertAtLast(head1.data)
        l3.insertAtLast(head2.data)
        head1 = head1.next
        head2 = head2.next

l1 = Linked_list()
head1 = l1.insertAtLast(1)
l1.insertAtLast(2)
l1.insertAtLast(3)
l1.insertAtLast(4)
l1.insertAtLast(5)
print("Our First Linked_List : ")  
l1.dispList()   

l2 = Linked_list()
head2 = l2.insertAtLast(6)
l2.insertAtLast(7)
l2.insertAtLast(8)
l2.insertAtLast(9)
l2.insertAtLast(10) 
print("Our Second Linked_List : ")
l2.dispList()     
l3= Linked_list()
MergeTwoList(head1,head2,l3)
print("Print Our Answer List : ")
l3.dispList()          
        