import app
import library.url
import library.json
import library.comment
import library.cron
import library.scan


def import_handler(www,source):

    for artist in library.json.import_json("Z:\\sources\\artist_list.json"):

        # url = "https://www.midiworld.com/search/?q="+artist
        # location = "S:\\Website Projects\\live\\midiworld\\"+library.parser.change_to_url(artist)+".html"

        url = www+artist
        location = "S:\\Website Projects\\live\\"+source+"\\"+library.parser.change_to_url(artist)+".html"

        ##Main Search Content##
        if library.file.file_exists(location):
            pass
        else:
            library.url.download_html_content(url,location)

  

import_handler("https://freemidi.org/search?q=","freemidi")
import_handler("https://www.mididb.com/search.asp?q=","mididb")
import_handler("https://www.midiworld.com/search/?q=","midiworld")