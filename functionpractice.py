def check(n):
    if n==0:
        return
    print("first = ",n)
    check(n-1)
    print("second = ",n)
    check(n-1)
    print("third = ",n)
n=2
check(n)