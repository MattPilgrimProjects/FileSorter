import urllib.request
import ssl
import requests
import library.file
import library.comment
import library.parser
import library.cron
import sys


def import_midi(filename, url):

    if library.file.file_exists(filename):
        library.comment.returnMessage("Midi file already exists " + filename)
    else:
        library.cron.delay(5)
        r = requests.get(url, allow_redirects=True)

        library.comment.returnMessage("Downloading Midi Content "+filename)
        return open(filename, 'wb').write(r.content)


def import_html(filename, url):
    if library.file.file_exists(filename):
        library.comment.returnMessage("HTML file already exists " + filename)
    else:
        library.cron.delay(5)
        r = requests.get(url, allow_redirects=True)
        library.comment.returnMessage("Downloading HTML Content "+filename)
        return open(filename, 'wb').write(r.content)


def check_for_status_code_error(response):
    if response.status_code == 200:
        return response.json()
    if response.status_code == 404:
        return response.status_code

    print("Import Error " + str(response.status_code))
    sys.exit()


def returnURLContent(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    response = urllib.request.urlopen(url)

    return response.read()


def spotify_web_api(web, params, auth):

    # library.cron.delay(1)

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': auth,
    }

    response = requests.get(web, headers=headers, params=params)

    return check_for_status_code_error(response)


def import_youtube(params, auth):

    library.cron.delay(1)
    content = youtube_web_api(params, auth)

    if content.status_code == 200:
        return content.json()
    else:
        library.comment.returnMessage("---")
        library.comment.returnMessage("---")
        library.comment.returnMessage(str(content.json()["error"]["code"])+": "+content.json()["error"]["message"])

        sys.exit()




def youtube_web_api(params, auth):

    params = (
        ('q', params["q"]),
        ('part', params["part"]),
        ('key', params["key"])
    )


    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': auth
    }

    return requests.get('https://youtube.googleapis.com/youtube/v3/search', headers=headers, params=params)



def download_html_content(search_url,save_location):

    library.cron.delay(2)

    library.comment.returnMessage("Processing => "+search_url)

    try: 
        returnURLContent(search_url)
    except:
        library.file.createFile(save_location,b"<html></html>")
        library.comment.returnMessage("No Content Available: " + save_location)
        library.comment.returnMessage("---")
    else:

        contents = returnURLContent(search_url)

        library.file.createFile(save_location,contents)

        library.comment.returnMessage("Download Content => "+save_location)   
    
        library.comment.returnMessage("---")

    return None

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

def last_fm_api(data,param,save_location):

    url = www+"&"+"&".join(params(data,param))

    library.cron.delay(1)

    try: 
        returnURLContent(url)
    except:
        library.comment.returnMessage("Error => "+url)
    else:

        contents = returnURLContent(url)

        library.file.createFile(save_location,contents)

        library.comment.returnMessage("Download Content => "+save_location)   


    return None
    
