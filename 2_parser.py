from app import setup
from app import app_setup
import library.tb
import library.json

tb = library.tb

filelist = tb.returnAllFilesByExtension(app_setup(1)['storage']['local_path_csv_processed'],".csv")

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

tb.export_json(app_setup(1)['storage']['search_results'],data)
