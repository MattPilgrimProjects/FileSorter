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

        return_content = library.json.import_json("Z:\\apple_music\\track_list\\"+file_title)["href"]

        if "album" in return_content:
            href = return_content
        else:
            href=""
    else:
        href=""
    return href


library.comment.returnMessage("Start")

for filename in library.scan.scan_file_recursively("S:\\Website Projects\\MusicKeyFinder\\resources\\api\\*\\*\\profile.json"):

    api = library.parser.global_return_path(filename) 

    for key,data in library.json.import_json(filename).items():
        if key=="artist": artist = data
        if key=="track" :  track= data

    for data in library.json.import_json("Z:\\apple_music\\api.json"):

        if data["artist"] == artist and data["track"] == track and data["href"] and library.file.file_does_not_exists("Z:\\apple_music\\track_list\\"+api["sources"]):
            library.json.export_json(
                "Z:\\apple_music\\track_list\\"+api["sources"],{
                 "href":data["href"]
                })

            print("Z:\\apple_music\\track_list\\"+api["sources"])
            print(data["href"])
            print("---")

 

##################################################################################################################################
library.comment.returnMessage("Part 1 Completed")

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

library.comment.returnMessage("Completed") 
