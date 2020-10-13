import app

import library.cron

def download_html_content():
    keyword = app.random_keyword()

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

library.cron.schedule_handler(2,download_html_content)