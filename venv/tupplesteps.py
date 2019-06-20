#difference between Tupple and List
#Tupple () lists [] dict {}
#Tupple are not muttable ; Lists are muttable
# l=list()
#dir(l) [append,count, extend, index, insert, pop, remove, reverse, sort]=
#t=tupple()
#dir(t)  [count, index)
#dict is key value pair
#


(x,y)=(4,'friend')
print(x,y)
(x,y,z)=(4,'friend',10)
print(x,y,z)


d=dict()
d['cs']=2
d['cv']=4
for i,j in d.items():
    print(i,j)

cs=7
cv=6
tups=d.items()
print(tups)


d={'d':10,'c':1,'b':20}
t=sorted(d.items())
print(t)


c={'d':10,'c':1,'b':20}
t=list()
for i,j in c.items():
    t.append((j,i))
print(t)



c={'d':10,'c':1,'b':20}
print(sorted([(v,k) for k,v in c.items()]))
a=sorted([(v,k) for k,v in c.items()])
print(a[0])
a=sorted([(k,v) for k,v in c.items()])
print(a[0])

