import app
import config
import library.json
import library.download
import library.parser
import library.file

export_dictionary=[]

source="musicnotes"

for url in library.json.import_json("S:\\Midi-Library\\parsed\\pages\\"+source+".json"):

    filename=url

    if source=="freemidi":

        filename = url.replace("https://freemidi.org/artist-","")

        artist_id = filename.split("-")[0]

        filename = filename.replace(artist_id+"-","")
    
    else:
        pass

    export_dictionary.append({
        "sources":[
            {
                "import":url,
                "export":"S:\\Website Projects\\live\\"+source+"\\"+filename+".html"
            }
        ]
          
    })



library.json.export_json("S:\\Midi-Library\\"+source+"\\export.json",library.parser.remove_duplicates_from_dictionary(export_dictionary))
library.file.execute("S:\\Midi-Library\\"+source+"\\export.json")
# library.download.download_html("S:\\Midi-Library\\"+source+"\\export.json")