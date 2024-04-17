class car():
    Model=""
    price=0
    color=""
    year=""
    def __init__(self,m,p,c,y):
        self.Model=m
        self.price=p
        self.color=c
        self.year=y
def thirdcardetails():
    print("cost of third car = ",car3.price)
    print("year of third car = ",car3.year)
    print("color of third car = ",car3.color)
    print("model of third car = ",car3.Model)

m=input("enter the model of the car : ")
p=int(input("enter the price of the car : "))
c=input("enter the color of the car : ")
y=int(input("enter the year of the car : "))
m2=input("enter the model of the car2 : ")
p2=int(input("enter the price of the car2 : "))
c2=input("enter the color of the car2 : ")
y2=int(input("enter the year of the car2 : "))
m3=input("enter the model of the car3 : ")
p3=int(input("enter the price of the car3 : "))
c3=input("enter the color of the car3 : ")
y3=int(input("enter the year of the car3 : "))
car1=car(m,p,c,y)
car2=car(m2,p2,c2,y2)
car3=car(m3,p3,c3,y3)
#without constructur assign the value on car class
# car3.Model="xyz"
# car3.price=50000
# car3.year="2026"
# car3.color="green"
thirdcardetails()

