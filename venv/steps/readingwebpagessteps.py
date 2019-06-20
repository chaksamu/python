import requests
import re
r = requests.get('http://www.dr-chuck.com/page1.htm')
print(r.text)
c= r.text
r.close()

counts = dict()
print(len(c))
print(c[0:30])
for line in r:
    print(line.strip())
    words = line.split()
    for word in words:
        print(word)
        #ounts[word] = counts.get(word,0)+1
        if re.search('href', word):
            print(word)
