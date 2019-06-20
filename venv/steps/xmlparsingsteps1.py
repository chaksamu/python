import xml.etree.ElementTree as ET

data = '''<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>'''

tree = ET.fromstring(data)

for ele in tree:
    for sub in ele:
        print(sub.text)
for child in tree:
    print(child.tag, child.attrib)

for neighbor in tree.iter('neighbor'):
    print(neighbor.attrib)

for country in tree.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)
