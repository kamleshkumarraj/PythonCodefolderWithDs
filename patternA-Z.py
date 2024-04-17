def patternA():
    for r in range(7):
        for c in range(5):
            if(r==0) and (c in {1,2,3}):
                print("❤️",end=" ")
            elif(r in {1,2,4,5,6}) and (c in {0,4}):
                print("❤️",end=" ")
            elif(r==3):
                print("❤️",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()
    print()
        
def patternB():
    for row in range(7):
        for col in range(5):
            if(row in {0,6}) and (col in{0,1,2,3}):
                print("❤️",end=" ")
            elif(row in {1,2,4,5}) and (col in {0,4}):
                print("❤️",end=" ")
            elif(row == 3) and (col in {0,1,2,3}):
                print("❤️",end =" ")
            else:
                print(" ",end=" ")
        print()
    print()
    print()
        
def patternC():
    for row in range(7):
        for col in range(5):
            if(row in {0,6}) and (col in {1,2,3,4}):
                print("❤️",end=" ")
            elif(row in {1,2,3,4,5}) and (col==0):
                print("❤️",end=" ")
            else:
                print(" ",end =" ")
        print()
    print()
    print()
        
def patternD():
    for row in range(7):
        for col in range(5):
            if(row in {0,6}) and (col in {0,1,2,3}):
                print("❤️",end=" ")
            elif(row in {1,2,3,4,5}) and (col in {1,4}):
                print("❤️",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()
    print()
        
def patternE():
    for row in range(7):
        for col in range(5):
            if(col==0):
                print("❤️",end=" ")
            elif(row in {0,3,6}) and (col in {1,2,3,4}):
                print("❤️",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()
    print()
        
def patternF():
    for row in range(7):
        for col in range(5):
            if(col==0):
                print("❤️",end=" ")
            elif(row in {0,3}) and (col in {1,2,3,4}):
                print("❤️",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()
    print()

def patternG():
    for row in range(7):
        for col in range(5):
            if(row == 0) and (col in {1,2,3,4}):
                print("❤️",end=" ")
            elif(row in {1,2,3,4,5}) and (col==0):
                print("❤️",end = " ")
            elif(row==6) and (col in {1,2,3}):
                print("❤️",end=" ")
            elif(row in {4,5,3}) and (col==4):
                print("❤️",end =" ")
            elif(row==3) and (col in {2,3}):
                print("❤️",end= " ")
            else:
                print(" ",end=" ")
        print()
    print()
    print()    
    
    
def patternH():
    for row in range(7):
        for col in range(5):
            if(row in {0,1,2,3,4,5,6}) and (col in {0,4}):
                print("❤️",end= " ")
            elif(row==3) and (col in {1,2,3}):
                print("❤️",end= " ")
            else:
                print(" ",end=" ")
        print()
    print()
    print()


def patternI():
    for row in range(7):
        for col in range(5):
            if(row in {0,6}):
                print("❤️",end=" ")
            elif(col==2):
                print("❤️",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()
    print()
    
    
def patternJ():
    for row in range(7):
        for col in range(5):
            if(col==4) and (row in {0,1,2,3,4,5}):
                print("❤️",end=" ")
            elif(row in {0,6}) and (col in {1,2,3}):
                print("❤️",end=" ")
            elif(col==0) and (row in {3,4,5}):
                print("❤️",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()
    print()
    
    
def patternK():
    a=4
    print()
    for row in range(7):
        for col in range(5):
            if(col==0):
                print("❤️",end=" ")
            elif(row in {0,1,2,3}) and (col==a):
                print("❤️",end=" ")
                a=a-1
            elif(row==4 and col==2) or (row==5 and col==3 ) or (row==6 and col==4) :
                print("❤️",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()
    print()
    
    
def patternL():
    for row in range(7):
        for col in range(5):
            if(col==0):
                print("❤️",end=" ")
            elif(row==6):
                print("❤️",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()
    print()
    
    
def patternM():
    for row in range(7):
        for col in range(7):
            if(col in {0,6}):
                print("❤️",end=" ")
            elif(row==1 and col==1) or (row==2 and col==2) or (row==3 and col==3) or (row==2 and col==4) or (row==1 and col==5):
                print("❤️",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()
    print()
        

def patternN():
    a=1
    for row in range(7):
        for col in range(7):
            if(col in {0,6}):
                print("❤️",end=" ")
            elif(row==a and col==a) :
                print("❤️",end=" ")
                a=a+1
            else:
                print(" ",end=" ")
        print()
    print()
    print()
    
        
def patternO():
    for row in range(7):
        for col in range(5):
            if(row in {1,2,3,4,5}) and (col in {0,4}):
                print("❤️",end=" ")
            elif(row in {0,6}) and (col in {1,2,3}):
                print("❤️",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()
    print()
    
    
def patternP():
    for row in range(7):
        for col in range(5):
            if(col==0):
                print("❤️",end=" ")
            elif(row in {0,3}) and (col in{0,1,2,3}):
                print("❤️",end=" ") 
            elif(row in {1,2}) and (col==4):
                print("❤️",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()
    print()
                

def patternQ():
    for row in range(7):
        for col in range(6):
            if(row in {0,5}) and (col in {1,2,3}):
                print("❤️",end=" ")
            elif(col in {0,4}) and (row in {1,2,3,4}):
                print("❤️",end=" ")
            elif(row==4 and col==3) or (row==5 and col==4 ) or (row==6 and col==5):
                print("❤️",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()
    print() 
    
    
def patternR():
    a=4
    b=2
    for row in range(7):
        for col in range(5):
            if(col==0):
                print("❤️",end=" ")
            elif(row in {0,3}) and (col in{0,1,2,3}):
                print("❤️",end=" ")
            elif(row in {1,2}) and (col==4):
                print("❤️",end=" ")
            elif(row==a and col==b):
                print("❤️",end=" ")
                a=a+1
                b=b+1
                
            else:
                print(" ",end=" ")
        print()
    print()
    print()
    

def patternS():
    for row in range(7):
        for col in range(5):
            if(row==0) and (col in {1,2,3,4}):
                print("❤️",end=" ")
            elif(col==0) and (row in {1,2}):
                print("❤️",end=" ")
            elif(row==3) and (col in {1,2,3}):
                print("❤️",end=" ")
            elif(col==4) and (row in {4,5}):
                print("❤️",end=" ")
            elif(row==6) and (col in {0,1,2,3}):
                print("❤️",end=" ")
            else:
                print(" ",end=" ")
                pass
        print()
    print()
                  
    

patternD()
patternH()
patternE()
patternE()
patternR()
patternA()
patternJ()
            
