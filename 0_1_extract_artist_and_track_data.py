import app
import library.parser
import library.comment
import library.csv

converted_database = app.settings["karaokeversion"]["output"]

export_location = app.settings["karaokeversion"]["compressed"]

def songs(artist):

    return return_handler(artist,artist["songs"]["song"])

def return_handler(artist,song):

    url = library.parser.find_and_replace_array(song['url'],{
            "http://www.karaoke-version.com/mp3-backingtrack":"",
            ".html":"",
        })

    return {
        "artist": artist["name"],
        "track": song['name'],
        "url": url
    }

def songs_array(artist):

    array=[]

    for song in artist['songs']['song']:

        array.append(return_handler(artist,song))
       
    return array

def output_handler(data):
    return{
                "artist":data["artist"],
                "track":data["track"],
                "url":data["url"],
                "filename_artist":data["url"].split("/")[1],
                "filename_track":data["url"].split("/")[2],
    }

array=[]

for artist in library.json.import_json(converted_database)["artists"]["artist"]:

    try:
        artist["songs"]["song"]["name"]
    except TypeError:
        for data in songs_array(artist):
            array.append(output_handler(data))
            pass
    else:
        array.append(output_handler(songs(artist)))
    pass

library.json.export_json(export_location,array)
library.comment.returnMessage("Completed: "+export_location)

