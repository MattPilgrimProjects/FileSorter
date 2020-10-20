import library.tb
import library.directory
import pathlib
import os
import library.file
import shutil
import library.comment

# scanFiles=library.tb.scanFilesRecursively()

i=0

for filename in scanFiles['filelist']:

    file_extension = pathlib.Path(filename).suffix

    file_extension = file_extension.replace(".","")

    directory = "E:\\Unsorted\\SET_8\\"+file_extension+"\\"

    new_location =directory+os.path.basename(filename)

    if library.file.file_exists(new_location):
        pass
    elif file_extension in ["php","js","css","html"]:
        pass
    else:
        library.directory.create_recursive_diretory(directory)
        try:
            move = library.file.move_file(filename,new_location)
        except PermissionError:
            pass
        except FileNotFoundError:
            pass
        except shutil.Error:
            pass
        else:
            pass
    i = i+1
    library.comment.returnUpdateMessage("Total Process: "+str(i)+"/"+str(scanFiles["totalNumberOfFiles"]))