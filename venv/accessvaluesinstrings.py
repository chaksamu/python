var1="Guru99!"
var2="Python"

print("var1[0]",var1[0])
print("var2[1]",var2[1])

print("var1[1:3]",var1[1:3])
print("var2[4:6]",var2[0:6])

#print("u") in var1
#print("y") not in var2

#print(%s %d) % (var1,var2)

print(var1*2)

print(var1+var2)

var3="Hello,World!"
print(var3[0:5] + "INDIA")

var4="I Like INDIA"
var5=var4.replace('Like','love')
print(var5)

var6="my name is chakri"
print(var6.upper())

var7="MY NAME IS CHAKSAMU"
print(var7.lower())

print(":".join("SAMUD"))

var8="CHAKRA"
print(''.join(reversed(var8)))

var9="my:name:is:chakrad"
print(var9.split(':'))
print(var9.split('m'))

var10="syniverse"
var10=var10.replace("syniverse","SYNIVERSE")
print(var10)

modules=('alarm','query','report','nodediscovery','tablecleaner','autodiscovery','autocreate','bif','dailyreport','trafficmonitor')
print(modules[0])
print(modules[0:4])
print(modules[0-4])


var11=("Guru99","90","Education")
(company, emp, profile) = var11

print(company)
print(emp)
print(profile)

a=(5,6)
b=(1,4)
if (a>b):print("a is bigger")
else: print("b is bigger")

a=(5,6)
b=(5,4)
if (a>b):print("a is bigger")
else: print ("b is bigger")

a=(5,6)
b=(6,4)
if (a>b):print("a is bigger")
else: print("b is bigger")


a = {'x':100, 'y':200}
b = list(a.items())
print(b)


x = ("a", "b","c", "d", "e")
print(x[2:4])




