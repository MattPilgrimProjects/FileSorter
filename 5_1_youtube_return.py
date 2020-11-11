import app
import library.file
import library.csv
import library.json
import library.cron
import library.url
import library.comment

def create_filename(csv_row):

    return csv_row[1:].replace("/","-")+".json"

for csv_row in library.csv.import_csv("S:\\Midi-Library\\reporting\\live_api.csv"):
    
    

    if csv_row[0]!="artist":

        artist = csv_row[0] 
        track = csv_row[1]

        filename = app.settings["youtube"]["export"]+create_filename(csv_row[2])

        

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















# artist = "Slipknot"
# track= "Wait And Bleed"

# filename="youtube.json"

# params = (
#     ('q', artist+" "+track),
#     ('part', 'snippet'),
#     ('key', app.settings["youtube"]["api"])
# )
            
# library.cron.delay(1)
# content = library.url.youtube_web_api(params,app.settings["youtube"]["auth"])
# library.json.export_json(filename,content)

# library.comment.returnMessage("Added "+filename)

