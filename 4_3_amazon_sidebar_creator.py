import app
import library.scan
import library.parser
import library.json
import library.file

import sys

def change_to_url(value):
    return library.parser.find_and_replace_array(value.lower(),{
        " ":"-",
        '"':'',
        "'":"",
        "/":"-",
        ":":"",
        "?":"",
        "(":"",
        ")":"",
        "lÃ¸vÃ«":"",
        "---":"-",
        "&":"and",
        ".":"",
        ",":""
    })

def create_filename(csv_row):

    return csv_row[1:].replace("/","-")+".json"

for data in library.json.import_json("Z:\\amazon\\api.json"):

    url = change_to_url(data["artist"]+"-"+data["album"])+".json"

    if data["href"] and library.file.file_does_not_exists("Z:\\amazon\\processed\\"+url):

        library.json.export_json("Z:\\amazon\\processed\\"+url,[data])






for filename in library.scan.scan_file_recursively("S:\\Website Projects\\MusicKeyFinder\\resources\\api\\*\\*\\profile.json"):

    filename = library.parser.global_return_path(filename) 
    
    array=[]  

    for data in library.json.import_json("Z:\\spotify\\album_list\\"+filename["sources"]):

        album_path = filename["artist"]+"-"+change_to_url(data["album"])     

        if library.file.file_exists("Z:\\amazon\\processed\\"+album_path+".json"):
            
            for album_data in library.json.import_json("Z:\\amazon\\processed\\"+album_path+".json"):
                array.append({
                    "album":album_data["album"],
                    "href":album_data["href"],
                    "album_artwork":album_data["album_artwork"]
                })


    library.json.export_json("Z:\\amazon\\sidebar\\"+filename["sources"],array)
     

 