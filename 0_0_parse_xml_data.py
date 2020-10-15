import app

import library.cron

def parse_xml_data():

    root = app.xml.importXML(app.settings["xml_catalog"]["xml_file"])

    return_keyword = app.random_keyword()

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

    if app.file.file_exists(app.settings["raw_api_keywords"]+return_keyword+".json"):
       app.comment.returnMessage("Already added")
    else:    
        app.json.export_json(app.settings["raw_api_keywords"]+return_keyword+".json",array)
        app.comment.returnMessage(app.settings["raw_api_keywords"]+return_keyword+".json")

    return array

writer = app.csv.createCSVHeader("S:\\Midi-Library\\db.csv",["artist","track","url"])
for data in parse_xml_data():
    writer.writerow(data)
    pass


library.cron.schedule_handler(1,parse_xml_data)
