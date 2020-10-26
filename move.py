import app
import csv
import library.tb
import shutil
import datetime
import os

tb = library.tb

def importCSV(filename):
    with open(filename,newline="") as csvfile:

        for row in csv.DictReader(csvfile):

            for library in returnLibraryDetails():

                if row["FILE_EXTENSION"] in library["FILE_EXTENSION_ARRAY"]:

                    original_filename = row["PATH"]
                    move_directory = sortFilePath(library["SORT_FILEPATH"],row)
                    move_filename = move_directory+row["NAME"]+row['FILE_EXTENSION']

                    if tb.file_does_not_exists(move_filename) and tb.file_exists(original_filename) and "%" not in move_filename:
                        
                        

                        try:
                            library.create_recursive_directory(move_directory)
                        except(FileNotFoundError):
                            tb.returnMessage("Unable to create Directory")

                        try:
                            shutil.move(original_filename,move_filename)
                            tb.returnMessage("Moved => "+move_filename)
                        except(FileNotFoundError):
                            tb.returnMessage("File Error => "+move_filename)
                         
    pass

def returnLibraryDetails():

    result=[]

    settings = tb.import_file("settings.json")

    for LibraryTitle in settings["Library"]:

        LibraryDirectory = settings["Library"][LibraryTitle]

        result.append({
            "LIBRARY":LibraryTitle,
            "SORT_FILEPATH":LibraryDirectory["sort_filepath"],
            "FILE_EXTENSION_ARRAY":LibraryDirectory["file_extensions"]
            })
        pass

    return result

def sortFilePath(sort_filepath,row):

    for target_list in ["MEDIA_CREATED","DATE_TAKEN","DATE_CREATED"]:
        
        if "%"+target_list+"_YEAR%" in sort_filepath and row[target_list] != "":

            year = row[target_list].split("/")[2].split(" ")[0]

            year_return = datetime.datetime.strptime(year, '%y').strftime('%Y')

            sort_filepath = sort_filepath.replace("%"+target_list+"_YEAR%",year_return)

        if "%"+target_list+"_MONTH%" in sort_filepath and row[target_list] != "":

            month = row[target_list].split("/")[1]

            sort_filepath = sort_filepath.replace("%"+target_list+"_MONTH%",month)

    for target_list in row:

        if "%"+target_list+"%" in sort_filepath:

            sort_filepath = sort_filepath.replace("%"+target_list+"%",deserialize(row[target_list])).strip()
    
    return sort_filepath

def deserialize(tag):

    if tag != "":
        for target_list in ["\\","/",":","*","?",'"',"<",">","|"]:
            tag = tag.replace(target_list,"")
            pass
    else:
        tag = "%BLANK%"
    return tag
    
importCSV(app.settings["search_output"])