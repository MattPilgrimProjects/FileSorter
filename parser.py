import library.tb

tb = library.tb

filelist = tb.returnAllFilesByExtension("C:\\inetpub\\wwwroot\\api\\processed\\",".csv")

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

tb.export_json("C:\\inetpub\\wwwroot\\api\\freemidi.json",data)
