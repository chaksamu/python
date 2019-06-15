#Polymorhishm will come into picture
#loose coupling ; Dependency Injection ; Interface
#4 ways of Impleneting 1) Duck Typing 2) Operator Overloading 3) Method Overloading 4)Method Overridding
################DUCK TYPING#############


class Room:
    def execute(self):
        print("Test55")
        print("Test66")





class Laptop:
    def __init__(self,ram,cpu):
        self.ram= ram
        self.cpu = cpu
        print("Message from Code Method Laptop Class",self.ram,self.cpu)
        print(self.ram,self.cpu)

    def execute(self):
        print("Test1")
        print("Test2")
        print("Test3")
        print("Test4")

    def code(self,ide):
        ide.execute()

    def cream(self,dock):
        dock.execute()

ide=Laptop('i10',100)
ide.execute()

#t3=Laptop('i10',100)
#t3.code(ide)

dock=Room()
t2=Laptop('i20',500)
t2.cream(dock)


t1=Laptop('i5',30)
#t1.code()
#print(t1.ram)
