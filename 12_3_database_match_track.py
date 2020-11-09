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

def return_tracks_from_database():
    array=[]
    for row in library.json.import_json(export_location):
        array.append(row["track"])
    
    return library.parser.remove_duplicates_from_array(array)


def output_handler(return_track,row,high_percentage_match,low_percentage_match):
    return{
            "track":return_track,
            "raw_track":row["track"],
            "url":row["download_url"],
            "high":high_percentage_match,
            "low":low_percentage_match
    }

##########################################################################################################################

for filename in library.scan.scan_file_recursively("S:\\Midi-Library\\tracks\\freemidi\\*\\artist-*.json"):

    create_artist_directory = filename.replace(".json","\\").replace(filename,"S:\\Midi-Library\\tracks\\freemidi")

    library.directory.create_recursive_directory(create_artist_directory)
    
    perfect_match_array=[]
    high_match_array=[]
    medium_match_array=[]

    for row in library.json.import_json(filename):
        

        for return_track in return_tracks_from_database():

            low_percentage_match = library.parser.low_match_percentage(row["track"],return_track)
            high_percentage_match = library.parser.high_match_percentage(row["track"],return_track)  

            if high_percentage_match == 100.0 and low_percentage_match==100.0:

                    perfect_match_array.append(output_handler(return_track,row,high_percentage_match,low_percentage_match))

            elif high_percentage_match >= 90:
                    
                    high_match_array.append(output_handler(return_track,row,high_percentage_match,low_percentage_match))

            elif high_percentage_match >= 80:

                    medium_match_array.append(output_handler(return_track,row,high_percentage_match,low_percentage_match))
            else:
                pass
      
    library.json.export_json(create_artist_directory+"perfect.json",perfect_match_array)
    library.json.export_json(create_artist_directory+"high.json",high_match_array)
    library.json.export_json(create_artist_directory+"medium.json",medium_match_array)
    library.comment.returnMessage("Completed: " + create_artist_directory)

############################################################################################################################

# for filename in library.scan.scan_file_recursively("Z:\\artist\\freemidi\\processed\\*.json"):

#     alphabet = filename.replace("Z:\\artist\\freemidi\\processed\\","").split("_")[0]
    
#     for row in library.json.import_json(filename):

#         library.directory.create_recursive_directory("S:\\Website Projects\\live\\freemidi\\artist\\"+alphabet)

#         html = "S:\\Website Projects\\live\\freemidi\\artist\\"+alphabet+"\\"+row["url"]+".html"

#         if library.file.file_exists(html):
#             pass
#         else:
#             library.cron.delay(1)
#             library.url.download_html_content("https://freemidi.org/"+row["url"],html)

############################################################################################################################

