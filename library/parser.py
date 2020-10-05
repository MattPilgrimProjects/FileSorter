import httplib2
import bs4 as bs
from bs4 import BeautifulSoup, SoupStrainer
import requests
import random

def parseLinksFromHTML(file,attribute):
    http = httplib2.Http()
    status, response = http.request(file)
    return bs.BeautifulSoup(response, 'html.parser',parseOnlyThese=SoupStrainer(attribute))


def request_data_from_url(url):
    return requests.get(url, allow_redirects=False)

def return_random_array_value(array):
    return random.choice(array)

def remove_duplicates_from_array(array):
    array = list(dict.fromkeys(array))
    return array 