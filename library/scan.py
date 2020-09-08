import glob

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