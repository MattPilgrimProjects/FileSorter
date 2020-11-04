import app
import library


def manual_check_handler(csv_row):

    if csv_row[4]=="check_url":
        return {
            "source":"",
            "check_url":"",
            "original_url":"",
            "stats":""
        }
    else: 
        return {
            "source":csv_row[0],
            "check_url":csv_row[4],
            "original_url":csv_row[5],
            "stats":csv_row[6]
        }

      


array=[]
manual_check=[]
for schema in app.settings["stage"]:
    directory = schema["track_to_midi"]["output"]["csv"]

    for filename in library.scan.scan_file_recursively(directory+"*.csv"):

        for csv_row in library.csv.importCSVData(filename):

                array.append({
                    "source":csv_row[0],
                    "artist":csv_row[1],
                    "track":csv_row[2],
                    "track_id":csv_row[3],
                    "url":csv_row[4],
                    "stat":csv_row[6]
                })

         
              
library.json.export_json(app.settings["sources"]["midi_list_tidy"]["json"],array)
# library.csv.export_csv("S:\\Desktop\\manual_review.csv",["source","check_url","original_url","stats"],manual_check)
