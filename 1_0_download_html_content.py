import app
import library.cron
import library.comment
def keyword_random():

    for setting in app.setup['stage']:

        already_downloaded = 0

        for filename in app.scan.scan_file_recursively(setting["href_save_location"]+"*.html"):

            already_downloaded = already_downloaded+1

            keyword_already_added = app.parser.find_and_replace_array(filename,{
                setting["href_save_location"]:"",
                ".html":""
            })

        updated_keyword_array=[]
        
        added=0
        not_added=0

        for keyword in library.json.import_json(app.settings['keyword_list_export']['compressed']):

            if keyword in keyword_already_added:
                added=added+1
                pass
            else:
                not_added = not_added+1
                updated_keyword_array.append(keyword)

    overall = not_added-already_downloaded

    library.comment.returnMessage(str(already_downloaded)+"/"+str(overall))

    return updated_keyword_array

def download_html_content():
    keyword = app.parser.return_random_array_value(keyword_random())

    for schema in app.setup['stage']:

        search_url = schema['search_url'] + keyword

        href_save_location = schema['href_save_location']

        href_save_file = href_save_location+keyword+".html"

        app.directory.create_recursive_diretory(href_save_location)

        app.directory.create_recursive_diretory(schema["processed_href"]["move_to"])

        if app.file.file_does_not_exists(href_save_file):

            contents = app.url.returnURLContent(search_url)

            app.file.createFile(href_save_file,contents)

            app.comment.returnMessage("Download Content => "+href_save_file)
        
        else:

            app.comment.returnMessage("File Already Exists => " + href_save_file)



library.cron.schedule_handler(10,download_html_content)

