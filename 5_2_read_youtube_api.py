import app
import library.scan
import library.json
import library.file
import library.comment

def export_data(filename,return_filename):
    library.comment.returnMessage("Processing "+ filename)

    json_data=[]  

    for schema in data["items"]:

        

        try:
            schema["id"]["videoId"]
        except:
            videoId=""
        else:
            videoId="https://www.youtube.com/watch?v="+schema["id"]["videoId"]         
  


        json_data.append({
                "title":schema["snippet"]["title"],
                "id":videoId
  
        })


        pass


    library.json.export_json(app.settings["youtube"]["track_list"]+return_filename,json_data[0])
    

for filename in library.scan.scan_file_recursively(app.settings["youtube"]["export"]+"*.json"):

    data = library.json.import_json(filename)

    return_filename = filename.replace(app.settings["youtube"]["export"],"")

    if library.file.file_exists(app.settings["youtube"]["track_list"]+return_filename):
        pass
    else:
        export_data(filename,return_filename)

        


    

    pass