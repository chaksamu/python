#difference between the init method and other methods
#init methods will called automatically
#other methods need to call them manually and define inside the class


class Computer:
    def __init__(self,vcpu,vram):
        self.cpu=vcpu
        self.ram=vram
        print("Init method n number of times based on objects configured")
    def config(self):
        print("chakri", self.cpu, self.ram)

    def addd(self):
        print('i8','20gb','2TB')


com1=Computer('i5',16)
com2=Computer('i8',32)
com3=Computer('i10',48)

Computer.config(com1)
Computer.config(com2)

com1.config()
com2.config()

x=9
print(id(x))
print(type(x))

a=5
a.bit_length()

com3.addd()
