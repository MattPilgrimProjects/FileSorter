import app

app.comment.returnMessage("Begin Search")

array=[]

for data in app.json.import_json(app.settings["database"]):

    url = data["url"]

    url = url.split("-")

    for url in url:

        url = url.replace("/","-")

    if "-" in url:
        pass
    else:
        array.append(url)
    pass

app.json.export_json(app.settings["keyword_list_export"]["compressed"],app.parser.remove_duplicates_from_array(array))

app.comment.returnMessage("Completed")