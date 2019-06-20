abc="the is interesting the is boring the is annoying the is troubling"
stuff=abc.split()
print(stuff)
print(len(stuff))
deg="the:is:interesting:the:is:boring:the:is:annoying:the:is:troubling"
stuff=deg.split()
print(stuff)
print(len(stuff))
deg="the:is:interesting:the:is:boring:the:is:annoying:the:is:troubnnnnnnnnnling"
stuff=deg.split(':')


print(stuff[0])
print(len(stuff))
print(range(len(stuff)))
i=None
bw=None
for j in range(len(stuff)):
    if i is None or i< j:
        i=j
        if bw is None or len(bw) < len(stuff[i]):
            bw=stuff[i]
            k=i
            #print(i,bw)

print(k,bw)


