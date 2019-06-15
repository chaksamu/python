#variable

#1)Instance Variable 2) Class / Static variable are same
#If we define variable inside Init then it will become instance variable
#if we define variable outside Init and inside Class then it wil become Class Static variable

#namespace is an area where you can store objetcs /varaibles
#1)Class namespace will store class variables
#2)Object /instance namespace will store instance variables or object variables



class Car:

    wheels = 4                     #Class or Static Variable variable which is defined outside method and inside class. if we change the variable will change the value of varibales for all objects

    def __init__(self):
        self.mil = 10               #instance variable   variable which is defined inside method....  changing variable for obejct will afect other objects.
        self.com = "Hyundai"        #instance  variable

c1=Car()
c2=Car()

c1.mil=8

Car.wheels = 8

print(c1.mil, c1.com,c1.wheels)
print(c2.mil, c2.com,c2.wheels)