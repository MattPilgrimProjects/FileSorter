import library.tb

tb = library.tb

key = "love"

url="https://freemidi.org/search?q="+key

local_path_temporary = "C:\\inetpub\\wwwroot\\api\\temporary\\"+key+".html"

local_uri_temporary = "http://localhost/api/temporary/"+key+".html"

local_path_csv_processed = "C:\\inetpub\\wwwroot\\api\\processed\\"+key+".csv"

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

    








