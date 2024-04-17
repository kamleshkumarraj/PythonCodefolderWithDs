import math
class friction():
    def __init__(self,c,d):
        self.a=c
        self.b=d
    def hcf(self,p,q):
        for i in range(p,0,-1):
            if(p%i==0 and q%i==0):
             break        
        return i
    def simplyfy(self,p,q):
        k=self.hcf(p,q)
        p=p//k
        q=q//k
        return p,q
    def __add__(self,other):
        p=f1.a*f2.b+f1.b*f2.a
        q=f1.b*f2.b
        p,q=self.simplyfy(p,q)
        # print(f"Sum Of Two Fraction={p}/{q}")
        return p,q


# def hcf(p,q):
#     for i in range(p,0,-1):
#         if(p%i==0 and q%i==0):
#             break        
#     return i
# def simplyfy(p,q):
#     k=hcf(p,q)
#     p=p//k
#     q=q//k
#     return p,q
# def add():
#     p=f1.a*f2.b+f1.b*f2.a
#     q=f1.b*f2.b
#     p,q=simplyfy(p,q)
#     return p,q

a=int(input("enter a="))
b=int(input("enter b="))
a1=int(input("enter a1="))
b1=int(input("enter b1="))
f1=friction(a,b)
f2=friction(a1,b1)
a,b=f1+f2
# a,b=add()
print(f"Sum Of Two Fraction={a}/{b}")


        