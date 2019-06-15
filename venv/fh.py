from time import sleep
f=open('MyData.txt','r')
#print(f.readline(4),end="")
#print(f.readline(),end="")
#print(f.read())

f1=open('MyWork','w')
#f1.write("This Is Latha and I'm chakri's crush")

#f3=open('Mywork','a')
#f3.write("This is onemoretime")
#sleep(2)
#f2=open('Mywork','r')
#print(f2.read())

for data in f:
    print(data)
    f1.write(data)

f4=open('IMG_9237.JPG','rb')
#or i in f4:
#   print(i)

f5=open('SAMHITHA.JPG','wb')
for i in f4:
    f5.write(i)
