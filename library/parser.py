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


def match_percentage(array_1,array_2):

    match=0

    for note in array_1:

        if note in array_2: match = match+1

    return match/len(array_1)*100


def find_and_replace_array(string,array):

    for key,value in array.items():

        return_data = string.replace(key,value)

        pass

    return return_data
    