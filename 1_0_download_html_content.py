import app
import library.cron
import library.comment
import time

def download_html_content(keyword,schema):

    library.comment.returnMessage("Processing => "+keyword + " - " +schema["title"])  

    search_url = schema['search_url'] + keyword

    href_save_location = schema['href_save_location']

    href_save_file = href_save_location+keyword+".html"

    library.directory.create_recursive_directory(href_save_location)

    library.directory.create_recursive_directory(schema["processed_href"]["move_to"])

    contents = library.url.returnURLContent(search_url)

    library.file.createFile(href_save_file,contents)

    library.comment.returnMessage("Download Content => "+href_save_file)   

    return None


compressed_keyword_array = library.json.import_json(app.settings['keyword_list_export']['compressed'])

for schema in app.settings["stage"]:

    for keyword in compressed_keyword_array:

        if library.file.file_does_not_exists(schema["href_save_location"]+keyword+".html"):
            

            time.sleep(41.6)
            download_html_content(keyword,schema)
            

        pass

    

