import os
import shutil
from pathlib import Path

import library.parser
import library.file
import library.comment

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

def create_temp_file(filename):
    return Path(filename).touch()


def file_remove(filename):
    return shutil.rmtree(filename)

def move_file(original_location,new_location):
    try:
        shutil.move(original_location,new_location)
    except FileNotFoundError:
        library.comment.returnMessage("File does not exist")
    else:
        return shutil.move(original_location,new_location)

def execute(filename):
    return os.system(filename)


def file_update(filename,content):

    with open('S:\\Desktop\\results.txt') as books:
        lines = books.readlines()

    for line in content:
        lines.append("\n"+line)

    with open('S:\\Desktop\\results.txt', 'w') as sortedbooks:
        sortedbooks.writelines(lines)

def import_midi_files(url,midi_location):

    library.cron.delay(5)

    library.comment.returnMessage("Processing: "+url)

    midi = library.parser.request_data_from_url(url)
    library.file.createFile(midi_location,midi.content)

    return library.comment.returnMessage("Track Added: "+midi_location)

def copy_file(from_location,to_location):
    return shutil.copyfile(from_location,to_location)