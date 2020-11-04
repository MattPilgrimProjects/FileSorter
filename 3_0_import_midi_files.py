import app
import library

import time

def import_midi_files(url,midi_location):

    library.comment.returnMessage("Processing: "+url)

    midi = library.parser.request_data_from_url(url)
    library.file.createFile(midi_location,midi.content)

    return app.comment.returnMessage("Track Added: "+midi_location)



for stage in app.settings["stage"]:

    track_to_midi_directory = stage["track_to_midi"]["output"]["csv"]

    for filename in library.scan.scan_file_recursively(track_to_midi_directory+"*.csv"):

        for csv_row in library.csv.importCSVData(filename):

            if csv_row[0] !="source":

                midi_location = app.settings["sources"]["midi_location"]+csv_row[0]+"\\"+csv_row[3]+".mid"

                if library.file.file_exists(midi_location):
                    pass
                else:
                    time.sleep(5.3)
                    url = stage["download_url"]+csv_row[3]
                    import_midi_files(url,midi_location)
                    pass
            else:
                pass
                
      
    
    pass



