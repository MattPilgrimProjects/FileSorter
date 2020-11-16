import urllib.request
import ssl
import requests
import library.file
import library.comment
import sys

def check_for_status_code_error(response):
    if response.status_code ==200:
        return response.json()
    else:
        print("Import Error" + str(response.status_code))
        return sys.exit()


def returnURLContent(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    response = urllib.request.urlopen(url)

    print(response.getcode())

    return response.read()

def spotify_web_api(params,auth):

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': auth,
    }

    response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)

    return check_for_status_code_error(response)

 

def youtube_web_api(params,auth):

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': auth
    }

    response = requests.get('https://youtube.googleapis.com/youtube/v3/search', headers=headers, params=params)

    return check_for_status_code_error(response)


def download_html_content(search_url,save_location):

    library.comment.returnMessage("Processing => "+search_url)

    contents = returnURLContent(search_url)

    library.file.createFile(save_location,contents)

    library.comment.returnMessage("Download Content => "+save_location)   
 
    library.comment.returnMessage("---")

    return None
    
