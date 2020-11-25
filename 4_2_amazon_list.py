import app
import library.scan
import library.parser
import library.file
import library.json
import library.csv
import library.directory

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


def href_return(filepath):

    if library.file.file_exists("Z:\\amazon\\processed\\"+filepath):
        href = library.json.import_json("Z:\\amazon\\processed\\"+filepath)[0]["href"]
    else:
        href=""

    return href

def do_not_use_after_first_use():
    raw=[]

    for schema in library.scan.import_json_from_directory_recursively(app.settings["sources"]["track_list"]["json"]):

        url = schema["url"].split("/")[1]+"-"+schema["url"].split("/")[2]
        path = schema["url"].split("/")[1]+"/"+schema["url"].split("/")[2]
    
        spotify_data = "Z:/spotify/album_list/"+url+".json"

        api_return = "S:/Website Projects/MusicKeyFinder/resources/api/"+path+"/profile.json"

        if library.file.file_exists(api_return) and library.file.file_exists(spotify_data):

            array=[]

            for data in library.json.import_json(spotify_data):
                
                array.append({
                        "artist": data["artist"],
                        "album":data["album"],
                        "src": "https://www.amazon.co.uk/s?k="+data["artist"]+" "+data["album"]+"&i=popular",
                        "href":href_return(schema["url"].split("/")[1]+"-"+change_to_url(data["album"])+".json"),
                        "album_artwork":data["album_artwork"]
                })


            raw.extend(array)

            
        else:
            pass

    library.json.export_json("Z:\\amazon\\api.json",library.parser.remove_duplicates_from_dictionary(raw))

do_not_use_after_first_use()
