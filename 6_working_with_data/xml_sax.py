import xml.sax


class SaxHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.current_data = ""
        self.name = ""
        self.surname = ""

    def startElement(self, tag, attributes):
        self.current_data = tag
        if self.current_data == "person":
            print(f"Person number: {attributes['number']}")

    def characters(self, attributes):
        if self.current_data == "name":
            self.name = attributes
        elif self.current_data == "surname":
            self.surname = attributes

    def endElement(self, attributes):
        if self.current_data == "name":
            print(f"Name: {self.name}")
        elif self.current_data == "surname":
            print(f"Surname: {self.surname}")
        self.current_data = ""


# create an XMLReader
parser = xml.sax.make_parser()

# turn off namepsaces
parser.setFeature(xml.sax.handler.feature_namespaces, 0)

# override the default ContextHandler
sax_handler = SaxHandler()
parser.setContentHandler(sax_handler)
parser.parse("files/example_xml.xml")
