from app import setup
import library.tb
import library.json

tb = library.tb



key = "hell"

url=setup['url_list']['freemidi']+key

local_path_temporary = setup['local_paths']['temporary_storage']+key+".html"

local_uri_temporary = setup['local_paths']['website']+key+".html"

local_path_csv_processed = setup['local_paths']['processed']+key+".csv"

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

    








