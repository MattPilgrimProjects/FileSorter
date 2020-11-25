import app
import library.file
import library.csv
import library.json
import library.cron
import library.url
import library.comment
import library.scan

import sys

for filename in library.scan.scan_file_recursively("S:\\Website Projects\\MusicKeyFinder\\resources\\api\\*\\*\\profile.json"):

    api = library.parser.global_return_path(filename) 

    for key,data in library.json.import_json(filename).items():
        if key=="artist": artist = data
        if key=="track" :  track= data
    

    if library.file.file_exists("Z:\\youtube\\raw_data\\"+api["sources"]):
        library.comment.returnMessage("Already added")
    else:
        params = (
                ('q', artist+" "+track),
                ('part', 'snippet'),
                ('key', app.settings["youtube"]["api"])
            )
        library.cron.delay(1)
        library.comment.returnMessage("Processing "+"Z:\\youtube\\raw_data\\"+api["sources"])
        content = library.url.youtube_web_api(params,app.settings["youtube"]["auth"])
        library.json.export_json("Z:\\youtube\\raw_data\\"+api["sources"],content)
        library.comment.returnMessage("Added "+"Z:\\youtube\\raw_data\\"+api["sources"])
