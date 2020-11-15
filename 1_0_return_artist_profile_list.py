import app
import library.url
import library.parser
import library.cron
import library.file
import library.scan
import library.directory

###################################################################################

def get_artist_list(alphabet):

    if library.file.file_exists(app.artist_download_path+alphabet+".html"):
        pass
    else:
        library.url.download_html_content(app.directory_import_path+alphabet,app.artist_download_path+alphabet+".html")

def extract_artist_id(alphabet):

    data = library.parser.parseLinksFromHTML(app.artist_localhost_path+alphabet+".html","a")

    part_2=[]

    for row in data:
        row = str(row)

        if "artist-" in row:
            return_value = row.replace('<a href="',"").replace("</a>","").split('">')

            part_2.append({
                "url":return_value[0],
                "artist":return_value[1]
            })
    return part_2

def export_results_to_json(alphabet):
    if library.file.file_does_not_exists(app.artist_library_path+alphabet+".json"):

        return library.json.export_json(app.artist_library_path+alphabet+".json",extract_artist_id(alphabet))


for alphabet in ["0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:

    library.directory.create_recursive_directory(app.artist_download_path+alphabet)

    library.directory.create_recursive_directory(app.track_library_path+alphabet)

    get_artist_list(alphabet)

    export_results_to_json(alphabet)