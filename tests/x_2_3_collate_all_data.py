import app
import library.scan
import library.json

def collate_all_data():

    full_array=[]
    list_of_artists=0

    for setting in app.settings['stage']:

        for filename in library.scan.scan_file_recursively(setting['raw_artist_match']+"*.json"):

            for json_content in library.json.import_json(filename):

                list_of_artists=list_of_artists+1

                full_array.append(json_content)

    library.comment.returnMessage(str(list_of_artists)+" tracks on the live site")
    return full_array


writer = app.csv.createCSVHeader(app.settings["dev_database"],["artist","track","stats","track_id","source","url","match"])
for row in collate_all_data():

    writer.writerow(row)
    pass



library.json.export_json(app.settings['live_database'],collate_all_data())
library.comment.returnMessage(app.settings['live_database'])
