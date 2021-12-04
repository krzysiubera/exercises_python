import xml.dom.minidom


xml_file_handler = xml.dom.minidom.parse("files/example_xml.xml")
people = xml_file_handler.documentElement.getElementsByTagName('person')

name_person = people[0].getElementsByTagName('name')[0].childNodes[0].data
surname_person = people[0].getElementsByTagName('surname')[0].childNodes[0].data

print(f"Person: {name_person} {surname_person}")

# change name of person to something else
people[0].getElementsByTagName('name')[0].childNodes[0].data = 'changed'
with open('files/example_xml_changed.xml', 'w+') as new_file:
    new_file.write(xml_file_handler.toxml())
