from __pycache__ import *
n=(int(input("enter binary number=")))

i=n
decimal=0
k=0
while(i>0):
    a=i%10
    decimal=decimal+a*(2**k)
    k=k+1
    i=i//10
print("decimal=",decimal)
add()

