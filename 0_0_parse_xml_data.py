import app

root = app.xml.importXML(app.settings["xml_catalog"]["xml_file"])

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



                url = app.parser.find_and_replace_array(url.text,app.settings["xml_catalog"]["replace"])
                
                array.append({
                    "artist":artist_name_tag,
                    "track":song_title_tag,
                    "url": url
                })
app.comment.returnMessage(app.settings["database"])
app.json.export_json(app.settings["database"],array)