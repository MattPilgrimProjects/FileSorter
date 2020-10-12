import app

import schedule
import time

def parse_xml_data():

    root = app.xml.importXML(app.settings["xml_catalog"]["xml_file"])

    array=[]

    return_keyword = app.parser.return_random_array_value(app.json.import_json(app.settings["keyword_list_export"]["compressed"]))

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
    if app.file.file_exists("Z:\\raw_api_keywords\\"+return_keyword+".json"):
        app.comment.returnMessage("Already added")
    else:
        app.comment.returnMessage("Z:\\raw_api_keywords\\"+return_keyword+".json")
        app.json.export_json("Z:\\raw_api_keywords\\"+return_keyword+".json",array)

    return "Done"

schedule.every(10).seconds.do(parse_xml_data)

while 1:
    schedule.run_pending()
    time.sleep(1)