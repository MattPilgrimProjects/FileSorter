import app
import library.url
import library.file

track_database = app.settings["track_database"]

print(track_database)

def return_artist_list():
    artist_list=[]
    
    for data in library.json.import_json(track_database):

        artist_list.append({
            "artist":data["artist"],
            "filename":data["filename_artist"]

        })

    return library.json.export_json("S:\\Midi-Library\\mididb\\artist.json",library.parser.remove_duplicates_from_dictionary(artist_list))


for schema in library.json.import_json("S:\\Midi-Library\\mididb\\artist.json"):

    if library.file.file_exists("S:\\Website Projects\\live\\mididb\\"+schema["filename"]+".html"):
        pass
    else:
        library.url.download_html_content("https://www.mididb.com/search.asp?q="+schema["artist"],"S:\\Website Projects\\live\\mididb\\"+schema["filename"]+".html")


