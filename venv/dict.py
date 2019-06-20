Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print (Dict['Tiffany'])

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print((Dict['Tiffany']))


Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
studentX=Boys.copy()
studentY=Girls.copy()
print(studentX)
print(studentY)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print(Dict)
Dict.update({"Sarah":9})
print(Dict)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print(Dict)
del Dict ['Charlie']
print(Dict)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print( "Students Name: %s " % Dict.items() )

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("Students Name: %s" % list(Dict.items()))


Dict={'Chakri': 20, 'Chandu': 21, 'Jaya': 22, 'Asu': 23}
#Boys={'Chakri': 20, 'Chandu': 21, 'Jaya': 22}
#Girls={'Asu': 23}
Students=list(Dict.keys())
Students.sort()
for S in Students:
    print(":".join((S,str(Dict[S]))))


Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("Length : %d" % len (Dict))

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("variable Type: %s" %type (Dict))

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("printable string:%s" % str (Dict))
