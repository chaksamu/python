import requests





c=dict()
line="the clown ran after the acre and the acre ran into the tent and the tent fell down on the clown and the car"
words=line.split()
print(words)

for word in words:
    c[word]=c.get(word,0)+1
print(c)
