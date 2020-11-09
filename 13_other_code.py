  
# Part 3 - Match artist with database

def match_artist_with_database(part_2):
    part_3 =[]
    for artist_data in part_2:

        part_3.append(artist_data["url"])

    return part_3

part_3 = match_artist_with_database(part_2)

#Part 4 - download all artist content

def download_all_artist_content(alphabet,part_3):
    
    for url in part_3:
        if library.file.file_exists("S:\\Website Projects\\live\\freemidi\\artist\\"+alphabet+"\\"+url+".html"):
            pass
        else:
            library.cron.delay(5)
            library.url.download_html_content("https://freemidi.org/"+url,"S:\\Website Projects\\live\\freemidi\\artist\\"+alphabet+"\\"+url+".html")
        
download_all_artist_content(alphabet,part_3)

#Part 5 - Extract track id from artist pages

def extrack_track_id_from_artist_pages(alphabet):

    part_5=[]

    for filename in library.scan.scan_file_recursively("S:\\Website Projects\\live\\freemidi\\artist\\"+alphabet+"\\*.html"):

        filename = filename.replace("S:\\Website Projects\\","http://localhost/")

        for header in library.parser.parseLinksFromHTML(filename,"h1"):
            header = str(header)
            artist = header.replace('<h1><span style="font-size:32px;background-color:rgba(255,255,255,.85);padding:5px;overflow:hidden"> ',"").replace(' Midi<span id="bandinfo" style="display:none">band info</span></span></h1>',"")
    
        for row in library.parser.parseLinksFromHTML(filename,"a"):

            row = str(row)

            if "download3" in row:
                
                filename = row.replace("\n","").replace('<a href="download3-','').replace('" itemprop="url">','').replace("</a>","").split("-")[0]
                track=row.split(">")[1].replace("\n","").replace("</a","")

                part_5.append({
                    "artist":artist,
                    "track":track,
                    "download_url":"https://freemidi.org/getter-"+filename
                })
    
    return library.json.export_json("S:\\Midi-Library\\artist\\freemidi\\"+alphabet+".json",part_5)

        
extrack_track_id_from_artist_pages(alphabet)    
