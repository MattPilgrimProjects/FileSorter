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

def matchRatio(artist,track):

    track_split = track.split("-")
    artist_split = artist.split("-")
    count=[]
    overall=[]

    for artist_split_value in artist_split:

        if artist_split_value in track_split:
            count.append("|")
            overall.append("|")
        else:
            overall.append("|")
    
    return len(count)/len(overall) * 100
 
  

data_array=[]
live_data=[]

for track in returnTrackInformationWithoutID(data['tracks']):

    id = track.split("-")

    artist_match=""

    for artist in returnArtistInformationWithoutID(data["artists"]):

        
        if matchRatio(artist,track) == 100.0:

            artist_match = artist
        
            
    track_title = track.replace("-"+artist_match,"")

    if artist_match == "":
        track_uri=""
        track_uri_live=""

    else:
        track_uri=track_title.strip("-").replace(id[0]+"-","")
        track_uri_live = track_title.strip("-").replace(id[0]+"-","")

    
    track_uri_live = track_uri_live.replace("-"," ")

 
    tb.create_recursive_diretory(r"C:\\inetpub\\wwwroot\\api\\live\library\\"+artist_match)
    tb.create_recursive_diretory(r"C:\\inetpub\\wwwroot\\api\\dev\library\\"+artist_match)

    library.json.export_json(
        r"C:\\inetpub\\wwwroot\\api\\dev\library\\"+artist_match+"\\"+track_uri+".json",
        {

        })

    library.json.export_json(
        r"C:\\inetpub\\wwwroot\\api\\live\library\\"+artist_match+"\\"+track_uri+".json",
        {
            "artist_name":artist_match.replace("-"," ").title(),
            "track_title":track_uri_live.replace("-"," ").title(),
        })
    
    data_array.append({
        "raw_data":track,
        "track_id":id[0],
        "artist":artist_match,
        "track_uri":track_uri,
        "path":"/"+artist_match+"/"+track_uri
        })
    pass

tb.export_json("C:\\inetpub\\wwwroot\\api\\ai.json",data_array)




quit()

   

    

   

        
