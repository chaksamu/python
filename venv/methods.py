#Methods

#1) Instance Methods
#Accessor Methods fetch the values will use Accessor Methods   get
#Mutator Methods if we want to modify the values will use Mutator methods  set

#2) Class Methods
#    @classmethod
#    def getSchool(cls):
#        return cls.school


#3) static Methods

 #   @staticmethod
  #  def info():
   #     print("This Static Method insideclass")



class Student:

    school = 'Kings'

    def __init__(self,m1,m2,m3):
        self.mat = m1
        self.sce = m2
        self.soc = m3

    def avg(self):
        return (self.mat+self.sce+self.soc)/3
        #print(s1.return)
        #print(s2.return)

    def get_m1(self):
        return self.m1
        #self.phy = value1
        #self.che = value2
        #self.bio = value3
        #print(self.phy, self.che, self.bio)
        #print(self.phy)

    def set_m1(self,value):
        self.m1 = value

    @classmethod
    def getSchool(cls):
        return cls.school
    @staticmethod
    def info():
        print("This Static Method insideclass")


s1=Student(10,20,30)
s2=Student(40,50,60)

s1.avg()
s2.avg()

#s1.get_m1(100)
Student.info()

print(s1.avg())
print(s2.avg())
print(Student.getSchool())
#print(self.phy)

