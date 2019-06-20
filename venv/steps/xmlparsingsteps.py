import xml.etree.ElementTree as ET
tree = ET.parse('data.xml.txt')
root = tree.getroot()

# all items data
print('Expertise Data:')

for elem in root:
   for subelem in elem:
      print(subelem.text)


data = '''<dat>
   <items>
      <item name="expertise1">SQL</item>
      <item name="expertise2">Python</item>
   </items>
</dat>'''
tree = ET.fromstring(data)


# all items data
print('Expertise Data:')

for elem in tree:
   for subelem in elem:
      print(subelem.text)