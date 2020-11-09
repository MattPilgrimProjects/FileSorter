import app
import library.json
import library.scan
import library.parser
import library.file
import library.comment
import library.cron
import library.directory
import library.url

export_location = app.settings["sources"]["track_list"]["json"]

def return_artists_from_database():
    array=[]
    for row in library.json.import_json(export_location):
        array.append(row["artist"])
    
    return library.parser.remove_duplicates_from_array(array)

def database_match_artist(perfect_filepath,high_filepath,medium_filepath,alphabet):
    for row in library.json.import_json("S:\\Midi-Library\\artist\\freemidi\\"+alphabet+".json"):

            for return_artist in return_artists_from_database():

                low_percentage_match = library.parser.low_match_percentage(row["artist"],return_artist)
                high_percentage_match = library.parser.high_match_percentage(row["artist"],return_artist)   
    
                if low_percentage_match == 100.0 and high_percentage_match == 100.0:

                    perfect_match_array.append({
                        "artist":return_artist,
                        "raw_artist":row["artist"],
                        "url":row["url"],
                        "high":high_percentage_match,
                        "low":low_percentage_match
                    })
                elif high_percentage_match >= 90 and high_percentage_match != 100.0:
                    
                    high_match_array.append({
                        "artist":return_artist,
                        "raw_artist":row["artist"],
                        "url":row["url"],
                        "high":high_percentage_match,
                        "low":low_percentage_match
                    })

                elif high_percentage_match >= 80 and low_percentage_match >= 50:
                    medium_match_array.append({
                        "artist":return_artist,
                        "raw_artist":row["artist"],
                        "url":row["url"],
                        "high":high_percentage_match,
                        "low":low_percentage_match
                    })
                else:
                    pass
          
           
    library.json.export_json("Z:\\artist\\freemidi\\processed\\"+alphabet+"_perfect_match.json",perfect_match_array)
    library.json.export_json("Z:\\artist\\freemidi\\processed\\"+alphabet+"_high_match.json",high_match_array)
    library.json.export_json("Z:\\artist\\freemidi\\processed\\"+alphabet+"_medium_match.json",medium_match_array)
    library.comment.returnMessage(alphabet+" updated")  

    return None   

##########################################################################################################################

for alphabet in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:

    perfect_match_array=[]
    high_match_array=[]
    medium_match_array=[]

    perfect_filepath= "Z:\\artist\\freemidi\\processed\\"+alphabet+"_perfect_match.json"
    high_filepath = "Z:\\artist\\freemidi\\processed\\"+alphabet+"_high_match.json"
    medium_filepath = "Z:\\artist\\freemidi\\processed\\"+alphabet+"_medium_match.json"

    if library.file.file_exists(perfect_filepath) and library.file.file_exists(high_filepath) and library.file.file_exists(medium_filepath):
        pass
    else: 
        database_match_artist(perfect_filepath,high_filepath,medium_filepath,alphabet)
        

############################################################################################################################

for filename in library.scan.scan_file_recursively("Z:\\artist\\freemidi\\processed\\*.json"):

    alphabet = filename.replace("Z:\\artist\\freemidi\\processed\\","").split("_")[0]
    
    for row in library.json.import_json(filename):

        library.directory.create_recursive_directory("S:\\Website Projects\\live\\freemidi\\artist\\"+alphabet)

        html = "S:\\Website Projects\\live\\freemidi\\artist\\"+alphabet+"\\"+row["url"]+".html"

        if library.file.file_exists(html):
            pass
        else:
            library.cron.delay(1)
            library.url.download_html_content("https://freemidi.org/"+row["url"],html)

############################################################################################################################

