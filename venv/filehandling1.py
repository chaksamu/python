def main():
    f=open("chakri.txt","w+")
    for i in range(0,10):
        f.write("This is line is %d\n" %(i+1))
    f.close()
main()


def main():
    f=open("chakri.txt","r")
    #if(f.mode=='r'):
        #contents=f.read()
       # print(contents)
    f1=f.readlines()
    for x in f1:
        print(x)
main()

def main():
    f=open("chakri.txt","r")
    if(f.mode=='r'):
       contents=f.read()
       print(contents)

main()

def main():
    f=open("syniverse.txt","w")
    for i in range(5):
        f.write("This is test %d\n" %(i+1))
    f.close()
main()