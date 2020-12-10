import codecs

def import_html(filename):
    f=codecs.open(filename, 'r')
    return f.read().split("\n")