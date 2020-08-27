import library.tb
import library.json

tb = library.tb

json = library.json

data = tb.import_file("C:\\inetpub\\wwwroot\\api\\freemidi.json")


def returnTrackInformationWithoutID(data):

    track_array=[]

    track=""

    for track in data:

        track = track.replace("/download3-","")

        track_array.append(track)

    return track_array

def returnArtistInformationWithoutID(data): 

    artist_array=[]

    for artist in data:

        artist = artist.replace("/artist-","")

        artist = artist.split("-")

        artist.pop(0)

        s="-"
        artist = s.join(artist)

        artist_array.append(artist)

    return artist_array


data_array=[]

for artist in returnArtistInformationWithoutID(data["artists"]):

    for track in returnTrackInformationWithoutID(data['tracks']):

        if tb.matchRadio(track,artist) > 0.6:

            track_title = track.replace("-"+artist,"")

            id = track.split("-")

            data_array.append({
                "raw_data":track,
                "track_id":id[0],
                "match_ratio":tb.matchRadio(track,artist),
                "artist_uri":artist.strip("-"),
                "track_uri":track_title.strip("-").replace(id[0]+"-","")
            })

tb.export_json("C:\\inetpub\\wwwroot\\api\\ai.json",data_array)
   

    

   

        
