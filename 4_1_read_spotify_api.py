import app
import library.scan
import library.json
import library.file
import library.comment

def export_data_single(filename,return_filename):
    library.comment.returnMessage("Processing "+ filename)

    json_data=[]  

    for schema in data["tracks"]["items"]:

        json_data.append({
                "href":schema["external_urls"]["spotify"]+"?highlight="+schema["uri"]
        })


        pass
    
    try:
        json_data[0]
    except:
        output={}
    else:
        output = json_data[0]

    library.json.export_json(app.settings["spotify"]["track_list"]+return_filename,output)

def export_data(filename,return_filename):
    library.comment.returnMessage("Processing "+ filename)

    json_data=[]  

    if  data["tracks"]["items"]:
        artist = data["tracks"]["items"][0]["artists"][0]["name"]

        for schema in data["tracks"]["items"]:
                

            if schema["album"]["images"]:
                album_cover = schema["album"]["images"][0]["url"]
            else:
                album_cover = ""

            if artist == schema["album"]["artists"][0]["name"]:
           
                json_data.append({
                            "artist":schema["album"]["artists"][0]["name"],
                            "album_artwork":album_cover,
                            "album":schema["album"]["name"],
                            "check_url":"https://www.amazon.co.uk/s?k="+schema["album"]["artists"][0]["name"]+"+"+schema["album"]["name"],
                            "url":""
                })
       
    return library.json.export_json(app.settings["spotify"]["album_list"]+return_filename,json_data)
    

for filename in library.scan.scan_file_recursively(app.settings["spotify"]["export"]+"*.json"):

    data = library.json.import_json(filename)

    return_filename = filename.replace(app.settings["spotify"]["export"],"")

    if library.file.file_exists(app.settings["spotify"]["track_list"]+return_filename):
        pass
    else:
        export_data_single(filename,return_filename)

    if library.file.file_exists(app.settings["spotify"]["album_list"]+return_filename):
        pass
    else:
        export_data(filename,return_filename)
        

        


    

    pass