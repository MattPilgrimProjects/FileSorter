import httplib2
import bs4 as bs
from bs4 import BeautifulSoup, SoupStrainer
import requests
import random
import re
import numpy

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

        string = string.replace(key,value)

        pass

    return string
    

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def regex(data,schema):

    trim = schema["processed_href"]["trim"]

    data = data.split(trim, 1)[0]

    if schema["processed_href"]["match"] in data:
        return_data = data
    else:
        return_data = ""
        pass


    for remove in schema["processed_href"]["remove"]:

        return_data = return_data.replace(remove,"")

    
    return return_data


def sanitize(value):

    return re.findall("[-)(a-zA-Z0-9 =>.$£':;?&,é]+", value)[0]

def filename_sanitize(value):
    return re.findall("[a-zA-Z0-9]+", value)



def distinct(array):
    
    a = numpy.array(array)
    unique, counts = numpy.unique(a, return_counts=True) 

    test =  dict(zip(unique, counts))

    return_array_2={}

    for key,value in test.items():

        return_array_2[key]=str(value)

    return return_array_2

