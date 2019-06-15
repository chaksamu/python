if True:
    print("imright")

if False:
    print("imright")
else:
    print("Imwrong")
print("Bye")

x=3
r=x%2
if r==0:
    print("Even")
else:
    print("Odd")


x=int(input("Enter the number:"))

if x>5:
    print("Given number is greater than 5")
elif x==5:
    print("Given number is equal to 5")
elif x<=3:
    print("Given number is less than or equal to 3")
else:
    print("the given number is 4")





i=1
while i<=5:
    print("Chakri",end=" ")
    j = 1
    while j<=5:
        print("Chandu",end=" ")
        j+=1
    i+=1
    print()

x=['chakri',32,72]
for i in x:
    print(i)

x='Chakri'
for i in x:
    print(i)

for i in [2,6,'paul']:
    print(i)

for i in range(10):
    print(i)

for i in range(10,21,2):
    print(i)

for i in range(30,19,-2):
    print(i)
print("BYE")
for i in range(30,19,-1):
    if i%5!=0:
        print(i)
    else:
        print(i)

for i in range(1,101):
    if i%3==0 or i%5==0:
        continue
    print(i)

for j in range(4):
    for i in range(4):
        print("# ",end="")
    print()
print("BYE")

for j in range(4):
    for i in range(j+1):
        print("# ",end="")
    print()

print("BYE")


for j in range(4):
    for i in range(4-j):
        print("# ",end="")
    print()