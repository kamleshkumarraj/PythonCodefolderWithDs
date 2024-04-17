str=input("enter your string is : ")
count=1
for i in range(len(str)-1):
    if str[i]==str[i+1]:
        count=count+1
        break
if(count==2):
    print(f"{str[i]} is twice in row : ")
else:
    print(f"does not have two identical letter in a row : ")
        
            
