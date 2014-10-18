import xml.etree.ElementTree as ET

tree = ET.parse('country.xml')

root = tree.getroot()

#######################################################

print root.tag
print root.attrib

#######################################################

for child in root:
    print child.tag, child.attrib
    
#######################################################
    
print root[0][1].text

#######################################################

for neighbor in root.iter('neighbor'):
    print neighbor.attrib
    

#######################################################


for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print name, rank    
    
#######################################################
    
for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')

tree.write('output.xml')    
    
#######################################################    
    
for country in root.findall('country'):
    rank = int(country.find('rank').text)
	if rank > 50:
	    root.remove(country)

tree.write('output.xml')    
    
    
    
    
    
    