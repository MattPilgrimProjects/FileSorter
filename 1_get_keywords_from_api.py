import app

import library.json
import library.comment

library.comment.returnMessage("Begin Search")

array=[]

for data in library.json.import_json("Z:\\db.json"):

    url = data["url"]

    url = url.split("-")

    for url in url:

        url = url.replace("/","-")

    
    if "-" in url:
        pass
    else:
        array.append(url)
    pass

library.json.export_json(app.settings["keyword_list_export"]["uncompressed"],array)

compressed = list(dict.fromkeys(array))


library.json.export_json(app.settings["keyword_list_export"]["compressed"],compressed)

library.comment.returnMessage("Completed")



