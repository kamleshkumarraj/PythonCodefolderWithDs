def find(b):
    k=0
    l=[]
    i=0
    while(i<len(b)):
        p=b[i]
        count=0 
        if p=="0":
            for j in range(i,len(b)):
                if p==b[j]:
                    count=count+1
                else:
                    break
            l.append(count)
            i=i+count
        else:
            i=i+1
    print("The Biggest Number Of Consecutive String Is : ",max(l))
b=(input("enter binary number : "))
find(b)
    


