# def pass_check(password):
#     for i in password:
#         if(i>='a' and i<='z')or(i>'A' and i<'Z'):
#             print("password set successful")
#             break
#         else:
#             print("plz enter correct password")


# password = input("enter pasword = ")
# if(len(password)>=6 and len(password)<=12):
#     pass_check(password)
# else:
#     print("plz enter correct pasword")
# cook your dish here
t = int(input())
for i in range(t):
    r = int(input())
    c= int(input())
    n = int(input())
    rn = r+n
    print(rn*c)