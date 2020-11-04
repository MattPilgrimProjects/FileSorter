import app
import library


multi_line=[]

for schema in app.settings["stage"]:

    for filename in library.scan.scan_file_recursively(schema["track_to_midi"]["output"]["csv"]+"*.csv"):
            for csv_row in library.csv.import_csv(filename):
                single_line=csv_row[1]+"=>"+csv_row[2]+"=>"+csv_row[5].replace(".html","")
                multi_line.append(single_line)




#Final Export 
export_list=[]
for csv_row in library.parser.remove_duplicates_from_array(multi_line):
    
    row = csv_row.split("=>")

    if row[0]!="artist":

        library.directory.create_recursive_directory(app.settings["live_api"]+row[2])

        export_list.append({
            "artist":row[0],
            "track":row[1],
            "url_artist":row[2].split("/")[1],
            "url_track":row[2].split("/")[2],
            "url":row[2]
        })
    else:
        pass

library.csv.export_csv("dev.csv",["artist","track","url_artist","url_track","url"],export_list)
library.json.export_json(app.settings["www"],export_list)
library.file.execute("dev.csv")

