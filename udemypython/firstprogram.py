mystring = "chakri"
print(mystring[1])

a = 5
b = 6
print(a + b)

name = "Dog"

last_letters = name[1:]

print('G' + last_letters)

print(2+3)
print('2'+'3')

print(mystring.split('a'))

name = "Imverybadfellow"

last_letters = name[::-1]

print(last_letters)

last_letters = name[-1]

print(last_letters)

last_letters = name[5::]

print(last_letters)

last_letters = name[1:3]

print(last_letters)

last_letters = name[::3]

print(last_letters)

print('##########################################formats################################')

print('The string is {}'.format('INSERTED'))

print('The {} {} {}'.format('dog', 'rat', 'bat'))

print('The {2} {1} {0}'.format('dog', 'rat', 'bat'))

print('The {2} {2} {2}'.format('dog', 'rat', 'bat'))

print('The {t} {r} {d}'.format(d='dog', r='rat', t='bat'))

#Float formating follows "{value:width.precision f}"

result = 100/777

print(result)

print('The result is :', result)

print('The result is : {}'.format(result))

print('The result is : {r}'.format(r=result))

print('The result is : {r:1.3f}'.format(r=result))

print('The result is : {r:10.3f}'.format(r=result))

#fstrings

name = 'jose'
age = '3'
print('Hello, what is your name: My name is', name)

print(f'Hello, what is your name: My name is {name}')

print(f'Hello, what is your name: My name is {name} and my age is {age}')

print('{}'.format('Python rules!'))

print('I like %s' % 'apples')

print('##########################################list################################')

my_list = [1, 2, 3]

len(my_list)

my_num = ['one', 'two', 'three']

my_list_num = my_list + my_num

print(my_list_num)

my_list_num[-1] = 'new'

print(my_list_num)

my_list_num[1::]

print(my_list_num)


my_list_num.append('four')

print(my_list_num)

new_list_num = my_list_num.pop(0)

print(new_list_num)

new_list = [10, 1, 2, 9, 8, 3, 4, 7, 6, 5]

new_num = ['a', 'z', 'b', 'y', 'c', 'w', 'd']

print(new_list[0])

new_list.sort()

new_num.sort()

print(new_list)

print(new_num)

new_list.reverse()

new_num.reverse()

print(new_list)

print(new_num)

print('1', 'two', '3.14')

new_list = [10, 1, 2, 9, 8, 3, 4, 7, 6, 5]

new_num = ['a', 'z', 'b', 'y', 'c', 'w', 'd']

new_list[0] = 21

print(new_list) #this is muttable

new_num[6] = 'M'

print(new_num) #this is muttable

new_list = [10, 1, 2, 9, 8, 1, 4, 7, 6, 1]

print(new_list.count(1))

print(new_list.index(1))

new_num = ['a', 'd', 'b', 'd', 'c', 'w', 'd']

print(new_num.count('d'))

print(new_num.index('d'))

list4 = [5,3,4,6,1]

list4.sort()

print(list4)

print('##########################################dict################################')

my_dict = {'a': 'apple', 'b': 'bat'}

print(my_dict['a'])

d = {'apple': 100, 'onion': {'mas': 100, 'blr': 90, 'hyd': 80}, 'banana': [1, 2, 3], 'letters': ['a', 'B', 'z']}

print(d['apple'])

print(d['banana'])

print(d['onion'])

print(d['banana'][2])

print(d['onion']['hyd'])

print(d.keys())

print(d.values())

print(d.items())

my_list_d = d['banana']

my_letters_d = d['letters']

print(my_list_d)

print(my_list_d[2])

print(my_letters_d[2])

print(my_letters_d[2].upper())

print(my_letters_d[1])

print(my_letters_d[1].lower())

print('#########################################tuples################################')

t = (1, 2, 3)

print(t)

#t[0] = 4

#print(t)

tt = ('a', 'a', 'z')

print(tt)

print(type(tt))

print(len(tt))

ttt = ('one', 2, '3.14')

print(ttt)

print(ttt[0])

print(ttt[-1])

print(tt.count('a'))

print(tt.index('a'))

print(tt.index('z'))

tup = (1, 2, [4, 5, 6])

print(tup[0])

print(tup[2][2])

print(tup[2][0])

print('#########################################set################################')

myset = set()

myset.add(1)

print(myset)

myset.add(2)

print(myset)

myset.add(1)

print(myset)

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3,3]

print(set(mylist))

myset = {1,2,3,4,5,5,4,3,2,1,1,2,3,4,5}

print(myset)

print(set('Mississippi'))

print(set([1,1,2,3]))

print('#########################################boolean################################')

print(1 == 1)

print(1 <= 1)

print(1 >= 1)

print(1 >= 2)

print(type(1 >= 2))


print('#########################################FILE I/O################################')

print('pwd')

myfile = open('myfile.txt')

print(myfile.read())

print(myfile.seek(0))

print(myfile.read())

print(myfile.seek(0))

contents = myfile.read()

print(contents)

print(myfile.seek(0))

print(myfile.read())

print(contents)

myfile = open('myfile.txt')

content = myfile.readlines()

print(content)

myfile.close()

print('######################')

mf = open('C:\\Users\\g706427\\Desktop\\python\\udemypython\\myfile.txt')

contentt = mf.read()

print(contentt)

with open('C:\\Users\\g706427\\Desktop\\python\\udemypython\\myfile.txt') as fm:
    contentts = fm.read()
    print(contentts)

with open('text.txt', mode='w') as f:
    f.write('I created the file')

with open('text.txt', mode='r') as f:
    print(f.read())

with open('text.txt', mode='a') as f:
    f.write('\nOne in First')

with open('text.txt', mode='r') as f:
    print(f.read())

with open('text.txt', mode='r+') as f:
    print(f.read())
    f.write('\nTwo in Second')
    print(f.seek(0))
    print(f.read())

with open('text.txt', mode='w+') as f:
    print(f.read())
    f.write('\nThree in Third')
    print(f.seek(0))
    print(f.read())


print('#########################################examples###############################')


d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d['k1'][0]['nest_key'][1])

l = [1, 2, [3, 4, [6, 7]]]

print(l[2][2][1])

ll = [1,{'k1':['this',['that']]}]

print(ll[1]['k1'][0])


d2 = {'k1':[9,10], 'k2':[8,7]}

print(d2['k1'][1])
print(d2['k2'][1])


d = {'k1':1,'k2': 2}
print(d['k1'])
print(d['k2'])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2])



print('#########################################comparision###############################')
print('####==###')
print(2 == 2)
print(2.0 == 2)
print('2' == '2')
print('2' == 2)
print('bye' == 'Bye')
print('two' == 2)
print('hello' == 'hello')

print('#### > ###')

print(2 > 3)
print('hello' > 'olleh')
print('hello' > 'hello')
print(3 > 1)
print(3 > 3)

print('#### >= ###')

print(2 >= 3)
print('hello' >= 'olleh')
print('hello' >= 'hello')
print(3 >= 1)
print(3 >= 3)
print('bye' >= 'Bye')

print('#### <= ###')

print(2 <= 3)
print('hello' <= 'olleh')
print('hello' <= 'hello')
print(3 <= 1)
print(3 <= 3)
print('bye' <= 'Bye')


print('#### < ###')

print(2 < 3)
print('hello' < 'olleh')
print('hello' < 'hello')
print(3 < 1)
print(3 < 3)
print('bye' < 'Bye')

print('#########################################logical operators###############################')
print('#### and ###')

print(2 < 3 and 1 > 3)

print('chak' == 'chak' and '2' == 2)

print('chak' == 'chak' and 2 == 2)

print('#### or ###')

print(2 < 3 or 1 > 3)

print('chak' == 'chak' or '2' == 2)

print('chak' == 'chak' or 2 == 2)

print('#### not ###')

print(not 2 < 3)

print(not 'chak' == 'chak')

print(not '2' == 2)


print('#########################################if elif and else###############################')

if True:
    print('Its True!')

if 3>2:
    print('Its True!')

hungry = True
if hungry:
    print('Its True!')

hungry = False
if hungry:
    print('Its True!')
else:
    print("Its False")

hungry = 'no'
if hungry == 'no':
    print('Not Hungry!')
else:
    print("Hungry")

hungry = 'now'
if hungry == 'no':
    print('Not Hungry!')
elif hungry == 'now':
    print('Feeling Hungry')
else:
    print("Hungry")

hungry = 'nope'
if hungry == 'no':
    print('Not Hungry!')
elif hungry == 'now':
    print('Feeling Hungry')
elif hungry == 'nope':
    print('Not Feeling Hungry')
else:
    print("Hungry")

name = 'chkri'
if name == 'chakri':
    print('Hello Chakri!')
elif name == 'chandu':
    print('Hello Chandu!')
elif name == 'Aslesh':
    print('Hello Aslesh')
else:
    print('what is your name?')

print('#########################################for loops###############################')

l = [1,2,3]
for ll in l:
    print(ll)

l = [1,2,3]
for ll in l:
    print('hello')

word = 'chakri'
for w in word:
    print(w)

t = (4,5,6)
for tt in t:
    print(tt)

d = {'k1':1,'k2':2,'k3':3}
for k in d.keys():
    print(k)
for k in d.values():
    print(k)
for k in d.items():
    print(k)

s = {1, 'two', 3.14}
for ss in s:
    print(ss)

