import app
import library.cron
import library.comment
import time
import library

def download_html_content(search_url,save_location):

    library.comment.returnMessage("Processing => "+search_url)  

    contents = library.url.returnURLContent(search_url)

    library.file.createFile(save_location,contents)

    library.comment.returnMessage("Download Content => "+save_location)   

    return None


compressed_keyword_array = library.json.import_json(app.settings['keyword_list_export']['compressed'])



for keyword in compressed_keyword_array:

        for schema in app.settings["stage"]:

            if library.file.file_exists(schema["href_save_location"]+keyword+".html"):
                pass
            else:
                time.sleep(3)
                download_html_content(schema["search_url"]+keyword,schema["href_save_location"]+keyword+".html")



