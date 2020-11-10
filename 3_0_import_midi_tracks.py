import app

import library.scan
import library.file
import library.comment
import library.cron
import library.url

for row in library.scan.import_json_from_directory_recursively("S:\\Midi-Library\\tracks\\freemidi\\*\\*\\*.json"):

    filename = row["url"].replace("https://freemidi.org/getter-","")
    
    original_location = "S:\\Midi-Library\\raw_midi\\freemidi\\"+filename+".mid"
    
    new_location = "S:\\Midi-Library\\raw_midi\\freemidi\\processed\\getter-"+filename+".mid"

    if library.file.file_exists("S:\\Midi-Library\\raw_midi\\freemidi\\"+filename+".mid"):

        library.file.move_file(original_location,new_location)
        library.comment.returnMessage(new_location)
    else:
        library.url.download_html_content(row["url"],new_location)
        pass