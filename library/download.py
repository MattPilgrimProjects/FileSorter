import library.json
import library.url
import library.comment


def download_midi(midi_database):  

    i=0
    overall = len(library.json.import_json(midi_database))

    for data in library.json.import_json(midi_database):

        library.url.import_midi(data["export"],data["import"])

        i=i+1
        library.comment.returnMessage(str(i)+"/"+str(overall))
        library.comment.returnMessage("---")


def download_html(html_database):

    i=0
    overall = len(library.json.import_json(html_database))

    for data in library.json.import_json(html_database):

        for schema in data["sources"]:
              
            library.url.import_html(schema["export"],schema["import"])

        i=i+1
        library.comment.returnMessage(str(i)+"/"+str(overall))
        library.comment.returnMessage("---")
    

def download_youtube(api_database):
    i=0
    overall = len(library.json.import_json(api_database))

    for data in library.json.import_json(api_database):

        library.url.import_youtube(data["sources"]["params"],data["sources"]["auth"],data["sources"]["export"])
        i=i+1
        library.comment.returnMessage(str(i)+"/"+str(overall))
        library.comment.returnMessage("---")
