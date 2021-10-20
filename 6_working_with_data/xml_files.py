import xml.etree.ElementTree


file_path = 'files/example_xml.xml'

# parse input file
root = xml.etree.ElementTree.parse(file_path)

# find all 'name' tages
for elem in root.findall('name'):
    # change contents of this tag to 'changed'
    elem.text = 'changed'

root.write('files/changed_file.xml')
