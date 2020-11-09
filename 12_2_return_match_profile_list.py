import app
import library.scan
import library.parser
import library.json
import library.comment
import library.file

export_location = app.settings["sources"]["track_list"]["json"]

def return_tracks_from_database():
    array=[]
    for row in library.json.import_json(export_location):
        array.append(row["track"])
    
    return library.parser.remove_duplicates_from_array(array)

def convert_to_json(filename,output_filepath):
    part_5=[]

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

    output_filepath = filename_raw.replace("S:\\Website Projects\\live\\freemidi\\artist\\","Z:\\tracks\\freemidi\\").replace(".html",".json")

    return library.json.export_json(output_filepath,part_5)

    
#################################################################################################################################################

for filename_raw in library.scan.scan_file_recursively("S:\\Website Projects\\live\\freemidi\\artist\\*\\*.html"):

    filename = filename_raw.replace("S:\\Website Projects\\","http://localhost/")

    output_filepath = filename_raw.replace("S:\\Website Projects\\live\\freemidi\\artist\\","Z:\\tracks\\freemidi\\").replace(".html",".json")

    if library.file.file_exists(output_filepath):
        library.comment.returnMessage("File already Exists: "+output_filepath)
        pass
    else:
        convert_to_json(filename,output_filepath)
        library.comment.returnMessage("Adding file: "+output_filepath)

