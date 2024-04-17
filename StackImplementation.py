# stackClass = []
# def addElement(value):
#     stackClass.append(value)  
# def removeElement():
#     stackClass.pop()
# newlist = []
# string = input("Enter your String : ")
# for i in string:
#     addElement(i)
# a = len(stackClass)-1
# for i in range(a , -1 , -1):
#     newlist.append(stackClass[i])
# newString = ""
# for s in newlist:
#     newString = newString+s
# print("Our New String is : ",newString)

#you are given an array of prices where prices[i] is the price of a given stock on the ith day. you want to maximize your profit by chhosing a single day to buy one stock and choosing a diffrent day in the future to sell that stock . return the maximum profit you can achieve from this transaction . if you can't achieve any profit return 0.

# arr = [4,3,2,1,9]
# list = []
# max= -1
# count = 0
# for i in range(len(arr)-1):
#     for j in range(i  , len(arr)):
#         if(arr[i]<arr[j]):
#             c = arr[j] - arr[i]
#             count = count+1
#             if(c>max):
#                 list = []
#                 max = c
#                 list.append(i)
#                 list.append(j)

# if(count==0): print("No profit : ")            
# else:           
#     ansList = [arr[list[0]] , arr[list[1]]]
#     print(ansList)
#     print("Total profit = ",ansList[1]-ansList[0])

class stack:
    list=[None]*10
    top = -1
    count = 0
    def insertAtFirst(self , value):
        self.top+=1
        self.list[self.top] = value
        self.count+=1
    def size(self):
        return self.count
stack1 = stack()
stack1.insertAtFirst(23)
stack1.insertAtFirst(43)
stack1.insertAtFirst(53)
stack1.insertAtFirst(63)
for i in range(stack1.size()):
    print(stack1.list[i],end=" ")


                
            
            


     