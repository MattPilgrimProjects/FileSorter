import app
import library

export_location = app.settings["sources"]["track_list"]["json"]
create_directory_location = app.settings["api"][0]["output"]["localpath"]

library.comment.returnMessage("Begin")

for schema in library.json.import_json(export_location):

    recursive_directory = app.parser.find_and_replace_array(schema['url'],{
            ".html":"\\",
            "/":"\\",
            
        })
    
    if library.file.file_does_not_exists(create_directory_location+recursive_directory):
        library.directory.create_recursive_directory(create_directory_location+recursive_directory)
        library.comment.returnMessage("Directories added:" + create_directory_location+recursive_directory)
    else:
        pass


    pass

library.comment.returnMessage("Completed")