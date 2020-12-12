import app
import config
import library.json
import library.download
import library.parser

export_dictionary=[]

for url in library.json.import_json("S:\\Midi-Library\\parsed\\pages\\freemidi.json"):

    filename = url.replace("https://freemidi.org/artist-","")

    artist_id = filename.split("-")[0]

    filename = filename.replace(artist_id+"-","")

    export_dictionary.append({
        "sources":[
            {
                "import":url,
                "export":"S:\\Website Projects\\live\\freemidi\\"+filename+".html"
            }
        ]
          
    })



library.json.export_json("S:\\Midi-Library\\freemidi\\export.json",library.parser.remove_duplicates_from_dictionary(export_dictionary))
library.download.download_html("S:\\Midi-Library\\freemidi\\export.json")