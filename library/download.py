import library.json
import library.url
import library.comment


def download_midi(midi_database,midi_download_location):  

    i=0
    overall = len(library.json.import_json(midi_database))

    for data in library.json.import_json(midi_database):

        i=i+1
        library.url.import_midi(midi_download_location+data["filename"]+".mid",data["midi_filename"])
        library.comment.returnMessage(str(i)+"/"+str(overall))
        library.comment.returnMessage("---")