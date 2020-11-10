import app
import library.file
import library.json
import library.comment

track_list = app.settings["sources"]["track_list"]["json"]
create_keyword_list = app.settings['keyword_list_export']['compressed']
output_location = app.settings["api"][0]["parsed_data"]["json"]


def artist_by_keyword(keyword):

    array=[]

    for schema in library.json.import_json(track_list):

        if keyword in schema["track"]:
            array.append(schema)
        else:
            pass
    
    library.comment.returnMessage("Adding: "+output_location+keyword+".json")
    return library.json.export_json(output_location+keyword+".json",array)

for keyword in library.json.import_json(create_keyword_list):

    if library.file.file_exists(output_location+keyword+".json"):
        pass
    else:
        artist_by_keyword(keyword)

