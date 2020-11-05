import app
import library.xml
import library.json

# Import the latest XML file from source location and convert to json. To be completed daily

database_filename = app.settings["api"][0]["source"]
database_output   = app.settings["api"][0]["output"]["json"]

return_music_content = library.xml.xml_to_dictionary(database_filename)

library.json.export_json(
    database_output,
    return_music_content
    )