l = []
n = int(input("Enter the number of the element : "))
for i in range(n):
    val = int(input())
    l.append(val)
val = int(input("Enter the value for searching : "))
count = 0
for i  in range(len(l)):
    if(l[i]==val):
        print("Searching is found : ")
        print("Index  = ",i)
    else:
        count = count+1
if(count==len(l)):
    print("Searching is not found ! ")