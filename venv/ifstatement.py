def main():
    x,y= 2,4

    if (x>y):
        st = "x is bigger"
        print(st)
    else:
        st ="y is bigger"
        print(st)

    if (x!=y):
        st="x is not equal to y"
        print(st)
    else:
        st="x is equal to y"
        print(st)
main()

def cha():
    x,y = 2,4
    if(x>y):
        print("x is bigger")
    elif(x<y):
        print("y is bigger")
    else:
        print("x and y has same identity")
cha()

def nestedif():
     x="AU"
     y=100
     if(y<50):
            print("the prices is 50")
     elif(y<=100):
            print("the prices is 100")
     elif(y<=150):
            print("the price is 150")
     else:
             print("Free")
nestedif()

def SwitchExample(argument):
    switcher = {
        0: " This is Case Zero ",
        1: " This is Case One ",
        2: " This is Case Two ",
    }
    return switcher.get(argument, "nothing")
#if __name__ == "__main__":
argument = 1
print(SwitchExample(argument))
