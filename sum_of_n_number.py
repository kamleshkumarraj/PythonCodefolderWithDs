def prin(n,a=1):
    if n==a:
        return n
    else:
        print(a)
        
        return prin(n,a=a+1)
print(prin(10))