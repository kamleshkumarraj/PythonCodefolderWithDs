# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None
        
# class Tree:
#     def __init__(self):
#         self.root = None
#     def add(self,root):
#         if(root==None):
#             x = int(input("enter value : "))
#             root = Node(x)
#         if(x==-1):
#             return self.root
#         print("Enter left child : ")
#         root.left = self.add(root.left)
#         print("Enter right child : ")
#         root.right = self.add(root.right)
        
#         return root
        
#     def printTreeIn(self,root):
#         if(root==None): return
#         self.printTreeIn(root.left)
#         print(root.data,end=" ")
#         self.printTreeIn(root.right)
# class Btree:
#     def __init__(self):
#         self.root  = None
#     def insert(self,root,data):
#         if(root==None):
#             root = Node(data)
#             return root
#         if(root.data>data):
#             if(root.left==None):
#                 temp = Node(data)
#                 root.left = temp
#                 return root
#             self.insert(root.left,data)
#         if(root.data<data):
#             if(root.right==None):
#                 temp = Node(data)
#                 root.right = temp
#                 return root  
#             self.insert(root.right,data)
        
#     def printIn(self,root):
#         if(root):
#             print(root.data,end = " --> ")
#             if(root.left is not None):
#                 print(root.left.data,end = " ")
#             else:
#                 print(None,end=" " )
#             if(root.right is not None):
#                 print(root.right.data,end=" ")
#             else:
#                 print(None,end=" ")
#             print()
#             self.printIn(root.left)
#             self.printIn(root.right)
# def search(root,data,c):
#     if(root==None): return False
#     if(root.data==data): return True,c
#     if(root.data>data):
#         return search(root.left,data,c=c+1)
#     if(root.data<data):
#         return search(root.right,data,c=c+1)
  
        
                
# tree = Tree()
# # root1 = tree.add(tree.root)
# # print(root)
# btree = Btree()
# root = btree.insert(btree.root,78)
# btree.insert(root,89)
# btree.insert(root,67)
# btree.insert(root,23)
# btree.insert(root,90)
# btree.insert(root,95)
# btree.insert(root,92)
# btree.insert(root,45)
# btree.insert(root,55)
# btree.insert(root,91)
# btree.insert(root,63)
# btree.insert(root,43)
# c=0
# print(search(root,63,c))
# btree.printIn(root)

