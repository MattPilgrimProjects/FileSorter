import app
import library.url
import library.json

source_path = app.settings["last_fm"]["source"]
track_list = app.settings["karaokeversion"]["compressed"]

handler_url = app.settings["last_fm"]["url"]
handler_params= app.settings["last_fm"]["params"]

##############################################################################################

def params(data, params):
    param_return = []

    for key, value in params.items():

        if value == "%ARTIST%":
            value = value.replace(
                value, data["filename_artist"].replace("-", "%20"))
        if value == "%TRACK%":
            value = value.replace(
                value, data["filename_track"].replace("-", "%20"))

        param_return.append(key+"="+value)

    return param_return


def import_handler(www,param):

    for data in library.json.import_json(track_list):

        url = www+"&"+"&".join(params(data, param))

        location = source_path + data["filename_artist"]+"-"+data["filename_track"]+".json"

        ##Main Search Content##
        if library.file.file_exists(location):
            pass
        else:
            library.url.last_fm_api(url, location)



library.comment.returnMessage("Start")
import_handler(handler_url,handler_params)
library.comment.returnMessage("Finished")
