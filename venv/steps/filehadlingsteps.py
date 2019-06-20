def main():
    fhand=open('MyWork')
    print(fhand)
    count=0
    for line in fhand:
        count+=1
    print('No of lines in the file',count)

    stuff='hello\nworld'
    print(len(stuff))
    print(stuff)

main()

def mainn():
    fh=open('MyData.txt','r')
    for line in fh:
        line =line.rstrip()
        print(line)
        if line.startswith('Good'):
            print(line)

    print(fh.read())


mainn()


def mai():
    fh=open('MyData.txt','r')
    print(fh.read())


mai()



def maain():
    fh=open('MyData.txt','r')
    for line in fh:
        line =line.rstrip()
        #print(line)
        if not line.startswith('Hi'):
            continue
        print(line)


maain()




def fh():
    name=str(input("Enter the File Name: "))
    f=open(name,'r')
    count=0
    for line in f:
        if line.startswith('Hi'):
            count+=1
    print('There were',count,'Hi in',name)


fh()


def fh1():
    name=str(input("Enter the File Name: "))

    try:
        f=open(name,'r')
    except FileNotFoundError as e:
        print("Please provide the correct file name",e)
    except FileExistsError as e:
        print("Please provide the correct file name", e)
    except Exception as e:
        print("Please check the file name format",e)

    finally:
        print("TEST")

    count=0
    for line in f:
        if line.startswith('Hi'):
            count+=1
    print('There were',count,'Hi in',name)



fh1()