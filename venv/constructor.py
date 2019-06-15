
class Cook:
    def __init__(self):
        self.name = "Chakri"
        self.age = 32
    def update(self):
        self.age=40
        self.name= "Guru"
        print(c5.age)
        print(c5.name)

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
#####Constructo###Define Object
c3=Cook()
c4=Cook()
c5=Cook()

c3.name = "chandu"
c3.age = 32

print(c3.name)
print(c3.age)

print(c4.name)
print(c4.age)

######update method will be called here
c5.update()

if c3.compare(c4):
    print("They are Same")
else:
    print("They are different")