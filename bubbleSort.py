l = []
n = int(input("Enter the size of the array : "))
for i in range(n):
    x = int(input())
    l.append(x)
for i in range(n-1):
    for j in range(n-1):
        if(l[j]>=l[j+1]):
            temp = l[j]
            l[j] = l[j+1]
            l[j+1] = temp
    print(i,"th passes : ")
    print(l)
print("Print our list in ascending order : ")          
print(l)