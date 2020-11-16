import app
import library.parser
import library.comment
import library.csv

converted_database = app.settings["api"][0]["output"]["json"]

export_location = app.settings["sources"]["track_list"]["json"]

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

array=[]

for artist in library.json.import_json(converted_database)["artists"]["artist"]:

    try:
        artist["songs"]["song"]["name"]
    except TypeError:
        for function_result in songs_array(artist):
            array.append(function_result)
            pass
    else:
        array.append(songs(artist))
    pass

library.json.export_json(export_location,array)

library.comment.returnMessage("Completed: "+export_location)


