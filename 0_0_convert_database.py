import app
import library.xml
import library.json
import library.comment

# Import the latest XML file from source location and convert to json. To be completed daily

database_filename = app.settings["karaokeversion"]["source"]
database_output   = app.settings["karaokeversion"]["output"]

############################################################################################

library.comment.returnMessage("Start")

return_music_content = library.xml.xml_to_dictionary(database_filename)

library.json.export_json(
    database_output,
    return_music_content
    )

library.comment.returnMessage("Output location: "+database_output)
