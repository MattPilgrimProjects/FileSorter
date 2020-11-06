import app
import library.file
import library.csv
import library.json
import library.cron
import library.url
import library.comment

def create_filename(csv_row):

    return csv_row[1:].replace("/","-")+".json"

for csv_row in library.csv.import_csv("live_api.csv"):
    
    

    if csv_row[0]!="artist":

        artist = csv_row[0] 
        track = csv_row[1]

        filename = app.settings["spotify"]["export"]+create_filename(csv_row[2])

        library.comment.returnMessage("Processing "+filename)

        if library.file.file_exists(filename):
            library.comment.returnMessage("Already added")
        else:
            params = (
                ('q', artist+" "+track),
                ('type', 'track,artist'),
                ('limit', '20'),
                ('market','US'),
                ('include_external','audio')
            )
            library.cron.delay(1)
            content = library.url.spotify_web_api(params,app.settings["spotify"]["auth"])
            library.json.export_json(filename,content)

            library.comment.returnMessage("Added "+filename)


        