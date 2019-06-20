#many values in single variable
cousins=['chakri','chandu','aslesh']
age=[32,33,31]
family=(cousins,age)
family1=[cousins,age]
print(cousins,age)
print(family)
print(family1)
cousinsage=['chakri',32,'chandu',33,'aslesh',31]
print(cousinsage)
nc=cousins+age
print(nc)


for c in cousins:
    print(c)
    print("happy new year", c)

for c in [len(cousins)]:
    print(c)


for c in range(len(cousins)):
    print(c)

for c in range(len(cousins)):
    print(c,cousins[c])

for c in range(len(cousinsage)):
    print(c,cousinsage[c])

print(1,[3,9],10)

print(cousins[0:2])
print(cousins[2])


#append,count,extend,index,insert, pop, remove, reverse,sort

cousins.append('jaya')
print(cousins)
cousins.append('java')
print(cousins)
cousins.sort()
print(cousins)
cousins.remove('java')
print(cousins)

print(len(age))
print(max(age))
print(min(age))
print(sum(age))
print(sum(age)/len(age))

def main():
    c=0
    t=0
    while True:
        inp=input("Enter thw Numbers to add")
        if inp=='done':
            break
        value=float(inp)
        t=t+value
        c=c+1
    avg=t/c
    print(avg)

main()

def main1():
    numlist=list()
    while True:
        inp=input("Enter thw Numbers to add")
        if inp=='done':
            break
        value=int(inp)
        #value = float(inp)
        numlist.append(value)
    print(numlist)
    print(sum(numlist)/len(numlist))

main1()







