import json

def import_json(filename):
    jsonFile = open(filename, 'r')
    config = json.load(jsonFile)
    jsonFile.close()
    return config

def export_json(filename,array):
    with open(filename, 'w') as json_file:
        return json.dump(array, json_file,indent=4) 

