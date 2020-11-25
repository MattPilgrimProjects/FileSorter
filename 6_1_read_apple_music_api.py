import app
import library.csv
import library.parser
import library.json
import library.file
import library.scan

import sys

array=[]

def href(file_title):
    if library.file.file_exists("Z:\\apple_music\\track_list\\"+file_title):
        href = library.json.import_json("Z:\\apple_music\\track_list\\"+file_title)
    else:
        href=""
    return href


for filename in library.scan.scan_file_recursively("S:\\Website Projects\\MusicKeyFinder\\resources\\api\\*\\*\\profile.json"):

    api = library.parser.global_return_path(filename) 

    for key,data in library.json.import_json(filename).items():
        if key=="artist": artist = data
        if key=="track" :  track= data

    array.append({
        "artist":artist,
        "track":track,
        "src":"https://music.apple.com/gb/search?term="+artist+" "+track,
        "href":href(api["sources"])
    })

library.json.export_json("Z:\\apple_music\\api.json",array)
