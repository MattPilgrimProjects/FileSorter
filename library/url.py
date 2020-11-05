import urllib.request
import ssl
import requests

def returnURLContent(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    response = urllib.request.urlopen(url)
    return response.read()

def spotify_web_api(params,auth):

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': auth,
    }

    response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)

    return response.json()