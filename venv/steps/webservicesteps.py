import xml.etree.ElementTree as ET

data = '''<family>
	<person>
		<name>chakri</name>
		<age>32</age>
	</person>
</family>'''
tree = ET.fromstring(data)


# all items data
print('Expertise Data:')

for elem in tree:
    for sub in elem:
        #print('Name:', sub.find('name').text)
        print(sub.text)
