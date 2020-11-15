import app
import library.file
import library.csv
import library.json
import library.cron
import library.url
import library.comment

def create_filename(csv_row):

    return csv_row[1:].replace("/","-")+".json"

for csv_row in library.json.import_json("S:\\Midi-Library\\sources\\track_list.json"):
    
    

        artist = csv_row["artist"] 
        track = csv_row["track"]

        filename = app.settings["youtube"]["export"]+create_filename(csv_row["url"])

        

        if library.file.file_exists(filename):
            library.comment.returnMessage("Already added")
        else:
            
            params = (
                ('q', artist+" "+track),
                ('part', 'snippet'),
                ('key', app.settings["youtube"]["api"])
            )
            library.cron.delay(1)
            library.comment.returnMessage("Processing "+filename)
            content = library.url.youtube_web_api(params,app.settings["youtube"]["auth"])
            library.json.export_json(filename,content)
            library.comment.returnMessage("Added "+filename)

