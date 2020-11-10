import glob
import library.json

def scanFilesRecursively(folder):
    array=[]
    for filename in glob.iglob( folder, recursive=True):
        array.append(filename)
    pass
    return array

def scan_file_recursively(folder):
    array=[]
    for filename in glob.iglob(folder, recursive=True):
        array.append(filename)
    pass
    return array

def import_json_from_directory_recursively(filepath):
    array=[]
    for filename in scan_file_recursively(filepath):

        for schema in library.json.import_json(filename):
            array.append(schema)

    return array