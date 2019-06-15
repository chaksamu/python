class School:
    def __init__(self):
        print("Init School")
    def teachers(self):
        print("Teachers Method")

    def students(self):
        print("Students Method")

class Playground:
    def __init__(self):
        print("Init Playground")
        #super().__init__()
    def studentspg(self):
        print("Studentsplayarea Method")
    def teacherspg(self):
        print("teachersplayarea Method")

class City(Playground,School):
    def __init__(self):
        super().__init__()                  #here the order will check left to right School has first pereference and they why we got o/p Init School and Init City
        print("Init City")
    def studentspgc(self):
        print("Studentscity Method")
    def teacherspgc(self):
        print("teacherscity Method")


t1=City()
t1.students()
