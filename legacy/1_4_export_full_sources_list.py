import app
import library.scan
import library.csv
import library.directory
import library.parser
import library.file
import library.comment

#########################################################

full_source_list=[]

library.comment.returnMessage("Start")

for schema in app.settings["stage"]:

    for filename in library.scan.scan_file_recursively(schema["track_to_midi"]["output"]["csv"]+"*.csv"):

        for csv_row in library.csv.import_csv(filename):

            if csv_row[0] =="source":
                pass
            else:
                full_source_list.append("=>".join(csv_row))

results_array=[]
for row in library.parser.remove_duplicates_from_array(full_source_list):
    csv_row = row.split("=>")
    results_array.append({
            "source":csv_row[0],
            "artist":csv_row[1],
            "track":csv_row[2],
            "track_id":csv_row[3],
            "url":csv_row[5].replace(".html",""),
            "stat":csv_row[6]
    })

library.json.export_json(app.settings["sources"]["midi_list_tidy"]["json"],results_array)  
library.csv.export_csv("source.csv",["source","artist","track","track_id","url","stat"],results_array)         
