class Student:
    def __init__(self,name,rollno):
        self.N = name
        self.R = rollno
        self.L = self.Laptop()

    def show(self):
        print(self.N,self.R)
        self.L.show()

    class Laptop:
        def __init__(self):
            self.brand = 'hp'
            self.cpu = 'i8'
            self.ram = 20
            #print(self.brand)
            #print(self.cpu)

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1=Student('chakri',1)
s2=Student('chandu',2)

print(s1.N,s1.R)
print(s2.N,s2.R)

s1.show()
s2.show()

#one way
s1.L.brand
s2.L.cpu

#other way
l1=s1.L
l2=s2.L

print(l1.cpu)
print(l2.ram)

print(id(l1))
print(id(l2))


lap1 = Student.Laptop()
