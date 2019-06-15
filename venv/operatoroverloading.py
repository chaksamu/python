###########Operator overloading -means add, sub, mul will remain same. here operator will remain same but operands will change

class Student:
    def __init__(self,m1,m2):
        self.m6=m1
        self.m3=m2
    def __add__(self, other):
        m5=self.m6+other.m6
        m4=self.m3+other.m3
        s3=Student(m5,m4)
        return s3

    def __gt__(self, other):
        r1=self.m6+self.m3
        r2=other.m6+other.m3
        print('r1 is:', r1,'r2 is:', r2)
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        #return self.m3,self.m6
        return '{} {}'.format(self.m6,self.m3)


s1=Student(10,20)
s2=Student(30,40)

s3=s1+s2

print(s3.m6,s3.m3)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

#print(s1.__str__())
#print(s2.__str__())
print(s1,s2)
