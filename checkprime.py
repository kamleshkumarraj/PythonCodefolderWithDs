def check(n,p,a):
    if p==0:
        return a
    if n%p==0:
        a=a+1
    return check(n,p-1,a)
n=int(input("enter n : "))
p=n
c=check(n,p,0)
print(c)
if c==2:
    print("given no. is a prime number : ")
else:
    print("given number is not a prime number :")