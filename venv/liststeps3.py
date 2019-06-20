name=str(input("Enter the Filename: "))
f=open(name,'r')
#ff=f.read()
#print(ff)
#gg=(ff.split())
#print(gg)
for line in f:
    if not line.startswith('From'):
        continue
    tt=line.split()
    print(tt[1])
    yy=tt[1]
    zz=yy.split('@')
    print(zz)
#4:13:00
