import xml.etree.ElementTree as ET
import xmltodict

def importXML(filename):
    tree = ET.parse(filename)
    return tree.getroot()

def xml_to_dictionary(filename):
    with open(filename,encoding='utf8') as fd:
        return xmltodict.parse(fd.read())