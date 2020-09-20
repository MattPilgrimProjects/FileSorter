import app
import library.directory
import library.comment
import library.url
import library.file

keyword = app.setup["keyword"]

stage = app.setup['stage']

for schema in stage:

    search_url = schema['search_url'] + keyword
    href_save_location = schema['href_save_location']

    href_save_file = href_save_location+keyword+".html"

    library.directory.create_recursive_diretory(href_save_location)

    library.directory.create_recursive_diretory(schema["processed_href"]["move_to"])

    if library.file.file_does_not_exists(href_save_file):

        
        contents = library.url.returnURLContent(search_url)
        library.file.createFile(href_save_file,contents)

        library.comment.returnMessage("Download Content => "+href_save_file)

        pass

        
    else:

        library.comment.returnMessage("File Already Exists => " + href_save_file)

    pass
