#inside heap memory , you will get objects
#Objects has 2 things 1)Variable and 2)Methods
#class -design-blueprint
#object - instance - entities
#class - attributes-->variables
#class - behavior--> methods(functions)
#Specialvariable _name_
#Specialmethod _init_
#attributes   properties(hieght, age, name, )
#behaviour  actions(talking, walking, eating) definds    use methods(functions in objects will call them as methods)


class Computer:

    def config(self):
        print("chakri")

    def addd(self):
        print('i8','20gb','2TB')


com1=Computer()
com2=Computer()
com3=Computer()

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
