import app
import library.scan
import library.csv
import library.directory
import library.parser
import library.file
import library.comment

def check_file_match(track_id):

    source=[]

    for schema in app.settings["stage"]:

        if library.file.file_exists(schema["midi_body_structure"]+track_id+".json"):
                boolean="true"
        else:
                boolean="false"

        source.append({schema["title"] : boolean})

        pass

    return source

#########################################################

multi_line=[]
artist_array=[]

full_source_list=[]

library.comment.returnMessage("Start")

for schema in app.settings["stage"]:

    for filename in library.scan.scan_file_recursively(schema["track_to_midi"]["output"]["csv"]+"*.csv"):

        for csv_row in library.csv.import_csv(filename):

            track_id=csv_row[3]

            if library.file.file_exists(app.settings["midi_body_structure"]+csv_row[0]+"\\"+track_id+".json"):
                source_match="true"
            else:
                source_match="false"

            artist_array.append(csv_row[1]+"=>"+csv_row[2]+"=>"+csv_row[5].replace(".html",""))
            multi_line.append(csv_row[1]+"=>"+csv_row[2]+"=>"+csv_row[5].replace(".html","")+"=>"+csv_row[0]+"=>"+source_match)
           
      
dev=[]   

for artist in library.parser.remove_duplicates_from_array(artist_array):

    for line in multi_line:

        sources=[]

        if artist in line:
            sources.append(line.replace(artist,""))
        else:
            sources=""
            pass
     
        if sources =="":
            pass
        else:
            midiworld="false"
            freemidi="false"

            if "=>midiworld" in sources[0]:
                midiworld = sources[0].replace("=>midiworld=>","")
            if "=>freemidi" in sources[0]:
                freemidi = sources[0].replace("=>freemidi=>","") 
   
    csv_return=artist+"=>"+midiworld+"=>"+freemidi
    array_return =csv_return.split("=>")

    dev.append({
        "artist":array_return[0],
        "track":array_return[1],
        "url":array_return[2],
        "midiworld":array_return[3],
        "freemidi":array_return[4]

    })
           
    pass
    
pass
           
library.csv.export_csv(app.settings["reporting"]["source_compile"],["artist","track","url","midiworld","freemidi"],dev)

library.comment.returnMessage("Finished")
