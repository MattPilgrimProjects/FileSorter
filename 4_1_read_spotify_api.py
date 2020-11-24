import app
import library.scan
import library.json
import library.file
import library.comment
import library.csv

def export_data_single(filename, return_filename):
    library.comment.returnMessage("Processing " + filename)

    json_data = []

    for schema in data["tracks"]["items"]:

        json_data.append({
            "href": schema["external_urls"]["spotify"]+"?highlight="+schema["uri"]
        })

        pass

    try:
        json_data[0]
    except:
        output = {}
    else:
        output = json_data[0]

    library.json.export_json(
        app.settings["spotify"]["track_list"]+return_filename, output)


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
                    "url": "https://www.amazon.co.uk/s?k="+schema["album"]["artists"][0]["name"]+"+"+schema["album"]["name"]
                })
    return json_data


for filename in library.scan.scan_file_recursively(app.settings["spotify"]["export"]+"*.json"):

    return_filename = filename.replace(
        app.settings["spotify"]["export"], "")

    if library.file.file_exists(app.settings["spotify"]["album_list"]+return_filename):
        pass
    else:
        export = export_data(filename)

        library.json.export_json(app.settings["spotify"]["album_list"]+return_filename, library.parser.compress_dictionary(export))

    

library.comment.returnMessage("---------")

for filename in library.scan.scan_file_recursively(app.settings["spotify"]["album_list"]+"*.json"):

    print(filename)


# raw=[]

# for data in library.scan.import_json_from_directory_recursively():

    

#     raw.append({
#         "artist":data["artist"],
#         "album":data["album"],
#         "url":data["url"]
#     })

# library.csv.export_csv("Z:\\spotify\\result.csv",["artist","album","url"],library.parser.remove_duplicates_from_dictionary(raw))





# library.comment.returnMessage("Completed")
