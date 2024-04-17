import keyword
def check(str,k):
    for i in k:
       if str in k:
           print("Invalid variable : ")
           return
    if(str[0]>="0" and str[0]<="9"):
        print("Invalid variable : ")
        return
    for i in str:
        if " " in str:
            print("invalid Variable : ")
        else:
             print("valid Variable : ")
        return
str=input("enter your string : ")
k=keyword.kwlist
check(str,k)
# print(k)


