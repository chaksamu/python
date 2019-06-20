def main():
    fruit='banana'
    letter=fruit[1]
    print(letter)
    lett=len(fruit)
    print(lett)
    lettt=fruit[lett-1]
    print(lettt)

    index=0
    while index < len(fruit):
        letter=fruit[index]
        print(index,letter)
        index=index+1

    big=max(fruit)      #big letter
    small=min(fruit)    #small letter
    print(big,small)
    print(fruit[0:4])   #slicing
    print(fruit[:])
    for i in fruit:
        print(i)

    a= 'hello'
    b= 'THERE'
    c=a+b
    print(c)

    print(c.upper())
    print(c.lower())

    pos=fruit.find('na')
    print(pos)
    pos = fruit.find('z')
    print(pos)

    veg=fruit.replace('ana','carrot')
    print(veg)

    veg1=veg.replace('o','O')
    print(veg1)

    veggg=' dsfgfdg '
    print(veggg)
    print(veggg.strip())
    print(veggg.lstrip())
    print(veggg.rstrip())

    line='Please make a note of this one'
    if line.startswith('please'):
        print("True")
    print("False")

    data='xyz@gmail.com S'
    atpos=data.find('@')
    print(atpos)

    sppos=data.find(' ',atpos)
    print(sppos)

    host=data[atpos+1:sppos]
    print(host)








main()