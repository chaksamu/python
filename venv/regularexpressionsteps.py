#regex or regexp
#^ mathes begging of a line
#$ matches end of the line
#. matches any charcter
#\s macthes whitespace
#\S matches non whitespace charcter
#* Repeats a charcter zero or more times
#*? Repeats a charcter zero or more times(non-greedy
#+ Repeats a charcter one or more times
#+? Repeats a charcter one or more times(non-greedy)
#[aeiou] matches a single charcter in the listed set
#[^xyz] matches a single charcter not in the listed set
#[a-z0-9] the set of charcters can include is to start
#( indicates where string extraction is to start
#) indicates where string extraction is to end


#to make use of regular expression
#first import re lib
#using re.search() like find

import re

f=open('data.txt','r')
for line in f:
    if line.find('From') >=0:
        print(line)

f = open('data.txt', 'r')
for l in f:
    if re.search('From',l):
        print(l,end="")


f = open('data.txt', 'r')
for l in f:
    if re.search('^From',l):
        print(l)


#^F.*
#^F-\S+:

x='My 2 fav numbers are 19 and 42'
y=re.findall('[0-9]+',x)
print(y)

x='My 2 fav numbers are 19 and 42'
y=re.findall('[AEIOU]+',x)
print(y)

x='My 2 fav numbers are 19 and 42'
y=re.search('[AEIOU]+',x)
print(y)

f=open('data.txt','r')
for l in f:
    if re.search('^F\S+:',l):
        print(l)


f=open('data.txt','r')
for l in f:
    if re.findall('^F\S+?:',l):
        print(l)

