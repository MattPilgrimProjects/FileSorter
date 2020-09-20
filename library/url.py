import urllib.request
import ssl

def returnURLContent(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    response = urllib.request.urlopen(url)
    return response.read()