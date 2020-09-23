import xml.etree.ElementTree as ET

def importXML(filename):
    tree = ET.parse(filename)
    return tree.getroot()