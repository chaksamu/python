class School:
    def teachers(self):
        print("Teachers Method")

    def students(self):
        print("Students Method")

class Playground:
    def studentspg(self):
        print("Studentsplayarea Method")
    def teacherspg(self):
        print("teachersplayarea Method")

##Single Level Inheritance
class Garden(Playground):
    def studentspgg(self):
        print("Studentsgarden Method")
    def teacherspgg(self):
        print("teachersgarden Method")

##Multi Level Inheritance
class Gym(Garden):
    def studentspggg(self):
        print("Studentsgym Method")
    def teacherspggg(self):
        print("teachersgym Method")



###Multiple Inheritance
class City(School,Playground):
    def studentspgc(self):
        print("Studentscity Method")
    def teacherspgc(self):
        print("teacherscity Method")

t1=School()
t2=School()

t1.teachers()
t1.students()
t2.students()
t2.teachers()

t1=Playground()
t2=Playground()
t1.studentspg()
t1.teacherspg()


t1=City()
t1.studentspgc()
t1.studentspg()
t1.students()

t1=Garden()
t1.teacherspg()
t1.teacherspgg()

t1=Gym()
t1.studentspggg()
t1.studentspgg()
t1.studentspg()