import app
import library.scan
import library.json
import library.file
import library.comment

def export_data(filename,return_filename):
    library.comment.returnMessage("Processing "+ filename)

    json_data=[]  

    for schema in data["tracks"]["items"]:


        if schema["album"]["images"]:
            album_cover = schema["album"]["images"][0]["url"]
        else:
            album_cover = ""


        json_data.append({
                "artist":schema["album"]["artists"][0]["name"],
                "album_artwork":album_cover,
                "album":schema["album"]["name"],
                "check_url":"https://www.amazon.co.uk/s?k="+schema["album"]["artists"][0]["name"]+"+"+schema["album"]["name"],
                "url":""
        })


        pass


    library.json.export_json(app.settings["spotify"]["album_list"]+return_filename,json_data)
    

for filename in library.scan.scan_file_recursively(app.settings["spotify"]["export"]+"*.json"):

    data = library.json.import_json(filename)

    return_filename = filename.replace(app.settings["spotify"]["export"],"")

    if library.file.file_exists(app.settings["spotify"]["album_list"]+return_filename):
        pass
    else:
        export_data(filename,return_filename)

        


    

    pass