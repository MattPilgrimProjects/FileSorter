import json
import library.parser

def import_json(filename):
    jsonFile = open(filename, 'r',encoding='utf-8')
    config = json.load(jsonFile)
    jsonFile.close()
    return config

def export_json(filename,array):
    with open(filename, 'w', encoding='utf8') as json_file:
        return json.dump(array, json_file,ensure_ascii=True,indent=4) 

def import_json_items(filename):
    return_tuples = import_json(filename).items()

    return library.parser.convert_tuples_to_dictionary(return_tuples)

def update_json(filename,content):
    data = import_json(filename) 
    data.update(content)
    export_json(filename,data)

def remove_key(key):
    try:
        key
    except KeyError:
        pass
    else:
        del key


