str=input("enter your String : ")
k=""
for i in str:
    k=k+(i+".")
print(k)
p=""
for i in range(len(k)):
    if i%2==0:
        p=p+k[i]
print(p)