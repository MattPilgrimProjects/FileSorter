import os
import library.comment
import shutil
import glob


def create_recursive_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
    except OSError:
        pass
    else:
        return os.makedirs(path, exist_ok=True)

def remove_directory(directory):
    for filename in glob.glob(directory+"/*.*"):
        os.remove(filename)
        library.comment.returnMessage("Removing "+filename)
        pass
    
    library.comment.returnMessage("Removing " + directory)
    return shutil.rmtree(directory)