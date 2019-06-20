def main():
    x=5
    while x>0:
        print("#")
        x-=1
    #print("#")


    #for  x in {1,2,3,4,5}:
    for x in range(1,10,1):
    #for x in range(1,10,2):
    #for x in range(10,1,-1):
        print("Round",x)
    print("Out of Round", x+1)
    #print("Out of Round",x-1)

main()
