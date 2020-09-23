import app
import library.xml
import library.json

root = library.xml.importXML(app.settings['return_xml_catalog'])

array=[]

for artist in root.findall('./artist'):

    artist_name_tag = artist.find('name').text

    for songs in artist.iter('songs'):

        for song in songs.iter("song"): 
            

            for url in song.iter("url"):

                pass

            for song_title in song.iter('name'):

                song_title_tag = song_title.text

                pass
            
                array.append({
                    "artist":artist_name_tag,
                    "track":song_title_tag,
                    "url":url.text.replace("http://www.karaoke-version.com/mp3-backingtrack","").replace(".html","")  
                })

library.json.export_json("db.json",array)