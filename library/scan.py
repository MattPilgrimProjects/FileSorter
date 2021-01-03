import glob
import library.json
import library.file
import ntpath
from pathlib import Path
import os
import stat
import time

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

def import_json_from_directory_recursively_items(filepath):
    array=[]
    for filename in scan_file_recursively(filepath):

        for schema in library.json.import_json(filename).items():
            array.append({
                "filename":filename,
                "data":schema
                })

    return array

def scan_files_in_directory(filepath):
    return_dictionary=[]
    file_count=0


    for filename in library.scan.scan_file_recursively(filepath):

        file_count = file_count+1

        return_dictionary.append({
            "file_count":file_count,
            "filepath":filename,
            "filename":ntpath.basename(filename),
            "filesize":Path(filename).stat().st_size,
            "file_last_modified":time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(filename))),
            "directory":filename.replace(ntpath.basename(filename),""),
            "file_created":time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getctime(filename)))
        })


    return {
        "overall_count":str(file_count),
        "data":return_dictionary
    }



def scan_directory(filepath,match_file):
    return_dictionary=[]
    file_count=0
    file_exist_count=0
    file_does_not_exist_count=0

    for filename in library.scan.scan_file_recursively(filepath+"*.json"):

        file_count = file_count+1

        file_exist = match_file+ntpath.basename(filename)

        file_exist = library.file.file_exists(file_exist)

        if file_exist==True:
            file_exist_count = file_exist_count+1
        
        if file_exist==False:
            file_does_not_exist_count = file_does_not_exist_count+1


        return_dictionary.append({
            "file_count":file_count,
            "filepath":filename,
            "filename":ntpath.basename(filename),
            "filesize":Path(filename).stat().st_size,
            "file_exists":file_exist,
            "match_file":match_file+ntpath.basename(filename),
            "file_does_not_exist_count":file_does_not_exist_count,
            "file_exist_count":file_exist_count
        })


    return {
        "overall_count":str(file_count),
        "file_exists_count":str(file_exist_count),
        "file_does_not_exist_count":str(file_does_not_exist_count),
        "data":return_dictionary
    }

