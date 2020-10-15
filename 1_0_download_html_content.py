import app

import library.cron

def keyword_random():

    for setting in app.setup['stage']:
        for filename in app.scan.scan_file_recursively(setting["href_save_location"]+"*.html"):

            keyword_already_added = app.parser.find_and_replace_array(filename,{
                setting["href_save_location"]:"",
                ".html":""
            })

        updated_keyword_array=[]

        for keyword in library.json.import_json(app.settings['keyword_list_export']['compressed']):

            if keyword in keyword_already_added:
                pass
            else:
                updated_keyword_array.append(keyword)
            
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


library.cron.schedule_handler(5,download_html_content)


