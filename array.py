from numpy import *
# arr = array([1,2,3,4,5,6])
# # print(arr)
# # print(arr.shape)
# arr1 = array([[1,2,3],[4,5,6],[7,8,9]])
# arr2 = array([[3,2,1],[6,5,4],[9,8,7]])
# #append method is used for insert our value in row and column wise 
# #if axis = 0 then our matrix insert in from last row
# #if axis =1 then our matrix insert from last column
# #if axis = none then our matrix insert then our matrix make a 1-d array
# arr3 = append(arr1,arr2,axis=0)
# arr4 = append(arr1,arr2,axis=1)
# #insert method is used for inserting our matrix in axis wise
# #syntax for inserting insert(firstarray , row\column , secondarray , axis=0/1)
# arr5 = insert(arr1,2,arr2,axis=1)
# # print(arr5)
# # print(arr1)
# array_1 = array([1,2,3,4,5])
# arr=insert(arr,2,array_1)
# # print(arr)
# # row,column = (arr1.shape).split()
# print(len(arr1))
# for i in range(3):
#     for j in range(3):
#         print(arr1[i][j])
# array_1 = delete(array_1,2)
# print(array_1)
arr = array([2,3,4,5,6,7,8])
n  = int(input("Enter your target :"))
for i in range(len(arr)-1):
    l=[]
    for j in range(i,len(arr)):
        if(arr[i]+arr[j] == n):
            l.append(arr[i])
            l.append(arr[j])
            print(l)


