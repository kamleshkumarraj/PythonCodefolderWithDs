def sum(n):
    if n<=9:
        return n
    else:
        a=n%10
        return (a+sum(n//10))
n=5234
print("sum= ",sum(n))