from app import setup
from app import app_setup
import library.tb
import library.json

tb = library.tb

key = "hell"

url=app_setup(1)['search']+key

local_path_temporary = app_setup(1)['storage']['local_path_temporary']+key+".html"

local_uri_temporary = app_setup(1)['storage']['local_uri_temporary']+key+".html"

local_path_csv_processed =app_setup(1)['storage']['local_path_csv_processed']+key+".csv"

if tb.file_does_not_exists(local_path_temporary):

    contents = tb.returnURLContent(url)
    tb.createFile(local_path_temporary,contents)


if tb.file_exists(local_path_temporary) and tb.file_does_not_exists(local_path_csv_processed):

    row={}

    writer = tb.createCSVHeader(local_path_csv_processed,["href"])

    for link in tb.parseLinksFromHTML(local_uri_temporary):
        if link.has_attr('href'):
            row['href'] = link['href']
            writer.writerow(row)
