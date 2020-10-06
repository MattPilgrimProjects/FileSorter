import app


root = app.xml.importXML(app.settings['return_xml_catalog'])

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

                url = url.text.replace("http://www.karaoke-version.com/mp3-backingtrack","").replace(".html","")

               
            
                array.append({
                    "artist":artist_name_tag.replace("-"," "),
                    "track":song_title_tag,
                    "url": url
                })

app.json.export_json(app.settings["database"],array)