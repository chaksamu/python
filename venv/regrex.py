import re
xx="chakri is fun and love"
output=re.findall(r"^\w",xx)
print(output)
output=re.findall(r"^\w+",xx)
print(output)
output=re.findall(r"\w+",xx)
print("The",output)
output=re.findall(r"\w",xx)
print("The ooo ",output)
output=re.findall(r'[\w\.-]+',xx)
print("The he he ",output)
print((re.split(r'\s',xx)))
print((re.split(r's',xx)))



def main():

 yy={"chakri get", "chakri go", "chakri gone"}
 for i in yy:
    z=re.match("(c\w+)\W(g\w+)", i)
    if z:
        print(z.groups())
main()

def main():
    pat=['chakri', 'chandu']
    text='chakri is too good'

    for p in pat:
        print('Looking of "%s" in "%s" -->' %(p, text), end=' ')

        if re.search(p, text):
            print("found a match")
        else:
            print('no match')
main()


#def main():
   # zz={'123@gmail.com', '456@gmail.com'}
   # output=re.findall(r'[\w\.-]+@[\w\.-]+',zz)
   # for op in output:
   #    print(op)
#main()


xx = """guru99
careerguru99
selenium"""
k1 = re.findall(r"^\w", xx)
k2 = re.findall(r"^\w", xx, re.MULTILINE)
print(k1)
print(k2)

yy= """carrer
syniverse
tvis"""
he=re.findall(r"^\w", yy)
print(he)
k2=re.findall(r"^\w", yy, re.MULTILINE)
print(k2)
