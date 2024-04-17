class Node:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None

    
def printTree(root):
    if(root==None): return
    print(root.data,end=" --> ")
    if(root.left==None): print("null",end=" ")
    else: print(root.left.data,end=" ")
    if(root.right!=None): print(root.right.data,end = " ")
    else: print("null",end=" ")
    print()
    printTree(root.left)
    printTree(root.right)
    
root = Node(1)
a = Node(2)
b = Node(3)
root.left = a
root.right = b
c = Node(4)
d = Node(5)
a.left = c
b.right = d
e = Node(6)
f = Node(7)
c.right = e
d.left = f
g = Node(8)
h = Node(9)
i = Node(10)
j = Node(11)
e.left = g
e.right = h
f.left = i
f.right = j
printTree(root)