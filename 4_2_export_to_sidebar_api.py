import app
import library.file
import library.json
import library.directory

for schema in library.json.import_json(app.settings["www"]):



    api_output = app.settings["live_api"]+schema['url']

    album_list = app.settings["spotify"]["album_list"]+library.parser.create_filename(schema["url"])

    if library.file.file_exists(api_output+"/sidebar.json"):
        pass
    else:
        if library.file.file_exists(album_list):
            library.json.export_json(api_output+"/sidebar.json",library.json.import_json(album_list))
            print("---")
        else:
            pass
    

