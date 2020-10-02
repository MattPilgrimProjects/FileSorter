from app import setup
from app import app_setup
import library.tb
import library.json
import library.parser

tb = library.tb

key = "don"

url=app_setup(1)['search']+key

local_path_temporary = app_setup(1)['storage']['local_path_storage']+key+".html"

local_uri_temporary = app_setup(1)['storage']['local_uri_temporary']+key+".html"

local_path_csv_processed =app_setup(1)['storage']['local_path_csv_processed']+key+".csv"


if tb.file_does_not_exists(local_path_temporary):

    contents = tb.returnURLContent(url)
    tb.createFile(local_path_temporary,contents)
else:
    tb.returnMessage("Keyword Already Added")


if tb.file_exists(local_path_temporary):

    row={}

    writer = tb.createCSVHeader(local_path_csv_processed,["href"])


    for link in library.parser.parseLinksFromHTML(local_uri_temporary,app_setup(1)["search_attributes"]):

        if app_setup(1)['config']['start'] in str(link) and app_setup(1)['config']['end'] in str(link):
            row['href'] = link
            writer.writerow(row)
        else:
            pass
        
        
        
