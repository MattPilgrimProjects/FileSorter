import library.json
import library.url
import library.comment


def download_midi(midi_database):  

    i=0
    overall = len(library.json.import_json(midi_database))

    for data in library.json.import_json(midi_database):

        try:
            schema
        except:
            pass
        else:
            for schema in data["sources"]:
                library.url.import_midi(schema["export"],schema["import"])

        i=i+1
        library.comment.returnMessage(str(i)+"/"+str(overall))
        library.comment.returnMessage("---")


def download_html(html_database):

    i=0
    overall = len(library.json.import_json(html_database))

    for data in library.json.import_json(html_database):

        try:
            schema
        except:
            pass
        else:
            for schema in data["sources"]:
                library.url.import_html(schema["export"],schema["import"])

        i=i+1
        library.comment.returnMessage(str(i)+"/"+str(overall))
        library.comment.returnMessage("---")
    