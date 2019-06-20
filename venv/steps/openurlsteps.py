import requests

r = requests.get('http://www.py4inf.com/code/romeo.txt')

bigcount=None
bigword=None
counts = dict()

for line in r:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) +1
        for wodr, count in counts.items():
            if bigcount is None or count > bigcount:
                bigword = wodr
                bigcount = count






print(counts)
print(bigcount, bigword)




#bigcount=None
    #bigword=None

    #for word.count in count.items():
    #    if bigcount is None or count > bigcount:
     #       bigword=word
     #       bigcount=count
    # print(bigcount,bigword)

f=open('data.txt','r')
for line in f:
    if line.find('From') >=0:
        print(line)