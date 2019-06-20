name=str(input("Enter the Filename: "))
f=open(name,'r')
ff=f.read()
print(ff)
gg=(ff.split())
print(gg)

i=None
bw=None
for j in range(len(gg)):
    if i is None or i< j:
        i=j
        if bw is None or len(bw) < len(gg[i]):
            bw=gg[i]
            k=i
            #print(i,bw)

print(k,bw)
