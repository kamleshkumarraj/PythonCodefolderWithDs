string=input("enter your string= ")
c_v=0
c_s=0
for i in string:
    if(i>="a" and i<="z") or (i>="A" and i<="Z"):
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='U' or i=='I' or i=='O'):
            c_v=c_v+1
        else:
            c_s=c_s+1
# print("No. of consonant=",c_s)
# print("No. of Vowel=",c_v)
