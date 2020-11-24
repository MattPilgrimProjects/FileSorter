import app
import library.scan
import library.parser
import library.file
import library.json
import library.csv
import library.directory

import sys

def export_data(filename):

    data = library.json.import_json(filename)

    library.comment.returnUpdateMessage("Processing " + filename)

    json_data = []

    if data["tracks"]["items"]:
        artist = data["tracks"]["items"][0]["artists"][0]["name"]

        for schema in data["tracks"]["items"]:

            if schema["album"]["images"]:
                album_cover = schema["album"]["images"][0]["url"]
            else:
                album_cover = ""

            if artist == schema["album"]["artists"][0]["name"]:

                json_data.append({
                    "artist": schema["album"]["artists"][0]["name"],
                    "album": schema["album"]["name"],
                    "album_artwork": album_cover,
                    "url": "https://www.amazon.co.uk/s?k="+schema["album"]["artists"][0]["name"]+"+"+schema["album"]["name"],
                    "path":filename
                })
    return json_data
###



### 

for filename in library.scan.scan_file_recursively("S:\\Website Projects\\api\\*\\*\\profile.json"):

    remove_directory = library.parser.find_and_replace_array(filename,{
        "S:\\Website Projects\\api\\":"",
        "\\profile":""
    })

    new_file = remove_directory.replace("\\","-")

    album_list = "Z:\\amazon\\album_list\\"+new_file
    raw_data = "Z:\\spotify\\raw_data\\"+new_file

    if library.file.file_exists(album_list):      
        pass
    else:  
        
        export = export_data(raw_data)

        library.json.export_json(album_list,library.parser.compress_dictionary(export))


####

return_list=[]

# for data in library.scan.import_json_from_directory_recursively("Z:\\amazon\\album_list\\*.json"):

#     print(data)

#     sys.exit()

    # filepath = filename.replace("Z:\\amazon\\album_list\\","")

    # print(filepath)

#     for data in library.json.import_json(filename):

#         if library.file.file_exists("Z:\\amazon\\processed\\"+filepath):
#             pass
#         else:

#             return_list.append({
#                 "filepath":filepath,
#                 "artist":data["artist"],
#                 "album":data["album"],
#                 "url":data["url"]
#             })


# library.csv.export_csv("Z:\\amazon\\raw_data.csv",["filepath","artist","album","url"],return_list)

##

# for data in library.csv.import_csv("Z:\\amazon\\checked.csv"):

#     if library.file.file_exists("Z:\\amazon\\processed\\"+data[0]) or data[4]=="click" or data[0]=="filepath":
#         pass
#     else:
#         library.json.export_json("Z:\\amazon\\processed\\"+data[0],{
#             "artist":data[1],
#             "track":data[2],
#             "href":data[4]
#         })
#         pass