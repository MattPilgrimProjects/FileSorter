import app
import library.download

for source in app.settings["sources"]:

    ### Settings ###
    midi_download_location = "S:\\Midi-Library\\"+source+"\\midi\\"
    midi_database = "S:\\Midi-Library\\"+source+"\\midi-library\\perfect.json" 

    ### Output ###
    library.download.download_midi(midi_database,midi_download_location)
