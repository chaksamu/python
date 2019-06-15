pos=-1 #global varibale
def search(list,s):
    i=0
    while i < len(list):
        if list[i]==s:
            globals()['pos']=i #local variable
            return True
        i+=1
    return False

def look(list,s):
    i=0
    for i in range(len(list)):
        if list[i]==s:
            globals()['pos']=i
            return True
    return False

list=[1,2,3,4,5,6,7,8,9,0]
s=int(input("Enter the number you are looking for: "))

if look(list,s):
    print("Found", pos)
else:
    print("Not Found")