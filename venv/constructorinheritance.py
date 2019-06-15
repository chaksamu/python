class School:
    def __init__(self):
        print("Init School")
    def teachers(self):
        print("Teachers Method")

    def students(self):
        print("Students Method")

class Playground(School):
    def __init__(self):
        print("Init Playground")
        super().__init__()
    def studentspg(self):
        print("Studentsplayarea Method")
    def teacherspg(self):
        print("teachersplayarea Method")


t1=Playground()       #First it will call Init of Playground if not exists then will call from Init School. If we want call both the use super().





