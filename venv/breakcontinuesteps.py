def main():
    while True:
        line=str(input("Enter the strring: "))
        if line == 'done':
            break
        print(line)


main()

def main():
    while True:
        line=int(input("Enter the number:"))
        if line == 5:
            continue
            print(line)
        if line == 1:
            break
        print(line)


main()


for i in [1,2,3,4,5]:
    print(i)

friends=['chakri','chandu','aslesh']

for friend in friends:
    print('Happy New year',friend)


i=0
z=0
s=0
for j in [10,8,20,2,30,1]:
    print(i,j)
    z+=1
    s=s+j

    if j > i:
        i=j
    print(i,j)
avg=s/z
print("The largest number from the series is ",i)
print("The number contains in the loop: ",z)
print("The totak sum of the loop is ", s)
print("the average of the loop is ", int(avg))
smallest=None
for s in [10,2,3,34,5,1]:
    if smallest is None:
        smallest = s
    elif s < smallest:
        smallest = s
print("smallest value from the loop is ", smallest)