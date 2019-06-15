###MOLOR means

class Student:
    def __init__(self):
        print("Auto method")

    def add(self,a,b):
        #self.a=a
        #self.b=b
        #s=self.a+self.b
        s=a+b
        #print(s)1
        return s

s1=Student()
#s1.mlo(2,3)    1
print(s1.add(2,3))


class Stud:
    def __init__(self):
        print("ByAuto")

    def mlo(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s

t1=Stud()
print(t1.mlo(10,11,12))

########Method overiding###########

class A:
    def show(self):
        print("In A Show")

class B(A):
    def show(self):
        print("In B Show")

a1=B()
a1.show()


