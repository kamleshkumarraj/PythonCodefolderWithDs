if __name__ == '__main__':
    n = int(input())
    sum=0
    for i in range(1,n+1):
        
        
        if(i>=10 and i<=99):
            sum = sum*100+i
        elif(i>=100):
            sum = sum*1000+i
        else:
            sum = sum*10+i
    print(sum)

# cube = lambda x:x*x*x # complete the lambda function 

# def fibonacci(n):
#     # return a list of fibonacci numbers
#     l1= [] 
#     # l1[0]=0
#     # l1[1]=1
#     a=0
#     b=1
#     l1.append(a)
#     l1.append(b)
#     for i in range(n-2):
        
#         c=a+b
#         a=b
#         b=c
#         l1.append(c) 
#     print(l1)
#     return l1


# cube = lambda x : x*x*x
# if __name__ == '__main__':
#     n = int(input())
#     print(list(map(cube, fibonacci(n))))
   