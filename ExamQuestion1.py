def rotateKthTerm(arr,term):
    term = term%len(arr)
    list1 = []
    
    for i in range(term, len(arr)):
        list1.append(arr[i])
    for j in range(0,term):
        list1.append(arr[j])
    return list1
    
arr = []
n = int(input("Enter the size of the array : "))
for i in range(n):
    v = int(input())
    arr.append(v)
term  = int(input("Enter the number of term for rotating : "))
anslist=[]
anslist = rotateKthTerm(arr,term)
print(anslist)