import httplib2
import bs4 as bs
from bs4 import BeautifulSoup, SoupStrainer
import requests
import random
import re
import numpy
from difflib import SequenceMatcher

def parseLinksFromHTML(file,attribute):
    http = httplib2.Http()
    status, response = http.request(file)
    return bs.BeautifulSoup(response, 'html.parser',parse_only=SoupStrainer(attribute))


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

def create_filename(csv_row):

    return csv_row[1:].replace("/","-")+".json"



def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def match_array_length(value,range_value):
    for i in range(range_value):

        print(i)

        pass

    return value


def low_match_percentage(string_1,string_2):

    array_1 = string_1.split()
    array_2 = string_2.split()

    match=0
    overall=0

    high_value = return_highest_value_by_array(array_1,array_2)
 
    for i in high_value:

        if i in array_1 or i.title() in array_1:
            match=match+1
            overall=overall+1
        else:
            overall=overall+1
            match=match
   
    return match/len(high_value)*100


def split_by_character(string):
    character_array=[]

    for character in string:
        character_array.append(character)
    
    return character_array


def return_highest_value(value_1,value_2):

    if len(value_1) <= len(value_2):
        return len(value_2)
    
    if len(value_1) >= len(value_2):
        return len(value_1)

def return_highest_value_by_array(value_1,value_2):

    if len(value_1) <= len(value_2):
        return value_2
    
    if len(value_1) >= len(value_2):
        return value_1

def match_string_length(value,range_value):

    match_up=[]

    for i in range(range_value):
        try:
            value[i]
        except:
            match_up.append("-")
            pass
        else:
            match_up.append(value[i])
            pass

    return "".join(match_up)



def high_match_percentage(string_1,string_2):

    array_1 = split_by_character(string_1)
    array_2 = split_by_character(string_2)


    if array_1=="" or array_2=="":
        pass
    else:
        range_value = return_highest_value(array_1,array_2)

        match=0
    
        example_1 = match_string_length(array_1,range_value)
        example_2 = match_string_length(array_2,range_value)
    
        for i in range(range_value):        

            if example_1[i] == example_2[i] or example_1[i] == example_2[i].title():
                match=match+1
            else:
                match=match

        return match/range_value*100