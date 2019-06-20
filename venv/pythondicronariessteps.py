#in dictonaries, we have label them key is lable and value is thing  key is wallet value is money
#list is linear collections index by 0,1,2,3,
#dict very powerful data collection


purse=dict()
purse['money']=12
purse['candy']=7
purse['tissues']=100
print(purse)

print(purse['candy'])

purse['candy']=purse['candy']+3

print(purse['candy'])

print(purse)

#difference between list and dict    dict use hasing(means random storage) that makes dict fast response then list

l=list()
d=dict()
l.append(21)
d['age']=21
l.append(70)
d['weight']=70
print(l)
print(d)
l[0]=23
print(l)
d['age']=31
print(d)

l=['csev','zhen','cwen','cwen','marquard','csev','marquad','zhen','zhen','marquad','csev','zhen','zhen']
d=dict()
for name in l:
    print(name)
    if name not in d:
        d[name]=1
    else:
        d[name]=d[name]+1
print(d)

#name='chakri'
if name in d:
    print(d[name])
else:
    print(0)


print(d.get(name,0))

l=['csev','zhen','cwen','cwen','marquard','csev','marquad','zhen','zhen','marquad','csev','zhen','zhen']
d=dict()
for name in l:
    print(name)
    d[name]=d.get(name, 0)+1
print(d)

c=dict()
line="the clown ran after the acre and the acre ran into the tent and the tent fell down on the clown and the car"
words=line.split()
print(words)

for word in words:
    c[word]=c.get(word,0)+1
print(c)

for key in c:
    print(key, c[key])

print(list(c))
print(c.keys())
print(c.values())
print(c.items())
print(c)

for i,k in c.items():
    print(i,k)


c=dict()
#line="the clown ran after the acre and the acre ran into the tent and the tent fell down on the clown and the car"
line="one two three three three three two two two two two two two"
words=line.split()
print(words)

for word in words:
    c[word]=c.get(word,0)+1
print(c)

bc=None
bw=None
for word,count in c.items():
    if bc is None or count > bc:
        bw=word
        bc=count
print(bw,bc)

