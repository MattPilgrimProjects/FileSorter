import app
import library.file
import library.csv
import library.directory
import library.parser
import library.comment
import library.scan


stage = app.setup['stage']

for schema in stage:

    file_array = library.scan.scan_file_recursively(schema["href_save_location"]+"*.html")

    for filename in file_array:
        
        keyword = filename.replace(schema["href_save_location"],"").replace(".html","")

        move_to = schema["processed_href"]["move_to"]+keyword+".csv"

        href_file = schema["href_save_location"]+keyword+".html"

        localhost = schema["localhost"]+keyword+".html"

        search_attribute = schema["processed_href"]["search_attribute"]

        match_array = schema["processed_href"]["match"]


        row={}

        if library.file.file_does_not_exists(move_to):

            writer = library.csv.createCSVHeader(move_to,["href"])


            for link in library.parser.parseLinksFromHTML(localhost,search_attribute):

                for match in match_array:
    
                    if match in str(link):
                        row['href'] = link
                        writer.writerow(row)
                        
                    pass

            
            library.comment.returnMessage(move_to)


    pass






          