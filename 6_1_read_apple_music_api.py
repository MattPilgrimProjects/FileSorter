import app
import library.csv
import library.parser
import library.json

for csv_row in library.csv.import_csv(app.settings["apple_music"]["import"]):

    if csv_row[3]:

        library.json.export_json(
            app.settings["apple_music"]["track_list"]+library.parser.create_filename(csv_row[2]),{
                "href":csv_row[3]
            }
        )

   