import app

import library.cron

def parse_xml_data():

    root = app.xml.importXML(app.settings["xml_catalog"]["xml_file"])

    array=[]

    return_keyword = app.random_keyword()

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

                    if return_keyword in artist_name_tag or return_keyword in song_title_tag:
                    
                        array.append({
                            "artist":artist_name_tag,
                            "track":song_title_tag,
                            "url": url
                        })

    if app.file.file_exists(app.settings["raw_api_keywords"]+return_keyword+".json"):
        return app.comment.returnMessage("Already added")
    else:    
        app.json.export_json(app.settings["raw_api_keywords"]+return_keyword+".json",array)
        return app.comment.returnMessage(app.settings["raw_api_keywords"]+return_keyword+".json")

library.cron.schedule_handler(5,parse_xml_data)