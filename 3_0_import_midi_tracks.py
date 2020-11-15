import app

import library.scan
import library.file
import library.comment
import library.cron
import library.url

import sys

source="freemidi"

for row in library.scan.import_json_from_directory_recursively(app.track_library_path+"\\*\\*\\*.json"):

    filename = row["url"].replace(app.track_import_path,"")

    new_location = "S:\\Midi-Library\\raw_midi\\"+source+"\\processed\\"+filename+".mid"

    if library.file.file_exists(new_location):
        pass
    else:
        library.cron.delay(5)
        library.file.import_midi_files(row['url'],new_location)
 
        pass