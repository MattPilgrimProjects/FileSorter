import httplib2
import bs4 as bs
from bs4 import BeautifulSoup, SoupStrainer
import requests

def parseLinksFromHTML(file,attribute):
    http = httplib2.Http()
    status, response = http.request(file)
    return bs.BeautifulSoup(response, 'html.parser',parseOnlyThese=SoupStrainer(attribute))


def request_data_from_url(url):
    return requests.get(url, allow_redirects=False)