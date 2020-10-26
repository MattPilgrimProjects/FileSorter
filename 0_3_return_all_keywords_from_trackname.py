import app
import library

export_location = app.settings["sources"]["track_list"]["json"]
create_directory_location = app.settings["api"][0]["output"]["localpath"]
create_keyword_list = app.settings['keyword_list_export']['compressed']

library.comment.returnMessage("Begin")

return_keywords_uncompressed = []

for schema in library.json.import_json(export_location):

    return_keywords_uncompressed.extend(schema['track'].split(" "))

library.json.export_json(create_keyword_list,library.parser.remove_duplicates_from_array(return_keywords_uncompressed))
library.comment.returnMessage("Completed:"+create_keyword_list)