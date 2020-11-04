import app
import library

array=[]

for schema in app.settings["stage"]:

    for filename in library.scan.scan_file_recursively(schema["keywords"]["output"]["csv"]+"*.csv"):

        for row in library.csv.importCSVData(filename):

            if row[0]!="href":
                array.append(row[0])
            pass

        pass

library.json.export_json(app.settings["sources"]["midi_list"]["json"],library.parser.remove_duplicates_from_array(array))

csv_array=[]

for target_list in library.parser.remove_duplicates_from_array(array):

    csv_array.append({"href":target_list})

    pass

library.csv.export_csv(app.settings["sources"]["midi_list"]["csv"],["href"],csv_array)

