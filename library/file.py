import os
import shutil

def file_exists(filename):
    if os.path.exists(filename):
        return True
    else:
        return False

def file_does_not_exists(filename):
    if os.path.exists(filename):
        return False
    else:
        return True

def createFile(file,content):
    f = open(file, "wb")
    f.write(content)
    f.close()

def file_remove(filename):
    return shutil.rmtree(filename)

def move_file(original_location,new_location):
    return shutil.move(original_location,new_location)