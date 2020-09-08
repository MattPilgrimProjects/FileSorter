from app import setup
import library.tb
import library.json

tb = library.tb

filelist = tb.returnAllFilesByExtension(setup['local_paths']['processed'],".csv")

artists=[]

tracks=[]

for filename in filelist:

    for data in tb.importCSVData(filename):

        filepath = data[0]

        if "/artist" in filepath and "/artists" not in filepath:
            
            artists.append(filepath)

        if "/download3" in filepath:

            tracks.append(filepath)

   
data={
    "artists":tb.removeDuplicates(artists),
    "tracks":tb.removeDuplicates(tracks)
}

tb.export_json(setup['json_local_midi_library']['freemidi'],data)
