class myClass():
    def method1(self):
        print("Chakri")
    def method2(self,somestring):
        print( somestring)
    def method3(self):
        print("Test")
def main():
    print("Main function Calling/Called")
    c = myClass()
    c.method1()
    c.method2("Testing is fun")
    c.method3()
main()

#Inheritenance

class myTree():
    def method1(self):
        print("Chakr3")
    def method2(self,somestring):
        print( somestring)
    def method3(self):
        print("Test")
class mysubTree():
    def method4(self):
        print("syniverse")
    def method1(self):
        print("Chakr3")
def main():
    print("Main function Calling/Called")
    c = mysubTree()
    c.method1()
   # c.method2("Testing is hard")
   # c.method3()
    c.method4()
main()

######Constructors
class User:
    name = ""

    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print("Welcome to Guru99, " + self.name)

c = User("Chakri")
c.sayHello()

