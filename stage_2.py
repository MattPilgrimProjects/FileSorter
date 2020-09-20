import app
import library.file
import library.csv
import library.directory
import library.parser
import library.comment

keyword = app.setup["keyword"]

stage = app.setup['stage']

for schema in stage:

    move_to = schema["processed_href"]["move_to"]+keyword+".csv"

    href_file = schema["href_save_location"]+keyword+".html"

    localhost = schema["localhost"]+keyword+".html"

    search_attribute = schema["processed_href"]["search_attribute"]

    match_array = schema["processed_href"]["match"]


    row={}

    writer = library.csv.createCSVHeader(move_to,["href"])


    for link in library.parser.parseLinksFromHTML(localhost,search_attribute):

        for match in match_array:

            
            if match in str(link):
                row['href'] = link
                writer.writerow(row)
            
            pass

    library.comment.returnMessage(move_to)


          