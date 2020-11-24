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
        "/":"",
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


def do_not_use_after_first_use():
    raw=[]

    for filename in library.scan.scan_file_recursively("S:\\Website Projects\\api\\*\\*\\profile.json"):

        remove_directory = library.parser.find_and_replace_array(filename,{
                "S:\\Website Projects\\api\\":"",
                "\\profile":""
        })

        new_file = remove_directory.replace("\\","-")

        raw_data = "Z:\\spotify\\album_list\\"+new_file

        if library.file.file_exists(raw_data):

            array=[]

            for data in library.json.import_json(raw_data):

                array.append({
                        "artist": data["artist"],
                        "album":data["album"],
                        "src": "https://www.amazon.co.uk/s?k="+data["artist"]+" "+data["album"]+"&i=popular",
                        "href":"",
                        "album_artwork":data["album_artwork"],
                })
                   

            raw.extend(array)
        else:
            pass
        
    library.json.export_json("Z:\\amazon\\api.json",library.parser.remove_duplicates_from_dictionary(raw))

# do_not_use_after_first_use()

for data in library.json.import_json("Z:\\amazon\\api.json"):

    url = change_to_url(data["artist"]+"-"+data["album"])+".json"

    if data["href"] and library.file.file_does_not_exists("Z:\\amazon\\processed\\"+url):
        
        library.json.export_json("Z:\\amazon\\processed\\"+url,[data])

   