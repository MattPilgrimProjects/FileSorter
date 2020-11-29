import app
import library.url
import library.json
import library.comment
import library.cron
import library.scan


def import_handler(www,source):

    for data in library.json.import_json("Z:\\sources\\track_list.json"):

        artist=data["filename_artist"]

        url = www+artist
        location = "S:\\Website Projects\\live\\"+source+"\\"+artist+".html"

        ##Main Search Content##
        if library.file.file_exists(location):
            library.comment.returnMessage("Already Added: "+location)
            library.comment.returnMessage("---")
            pass
        else:
            library.url.download_html_content(url,location)

  

import_handler("https://freemidi.org/search?q=","freemidi_search")
import_handler("https://www.mididb.com/search.asp?q=","mididb")
import_handler("https://www.midiworld.com/search/?q=","midiworld")