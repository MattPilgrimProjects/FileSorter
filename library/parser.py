import httplib2
import bs4 as bs
from bs4 import BeautifulSoup, SoupStrainer
import requests
import random
import re
import numpy
from difflib import SequenceMatcher
import sys

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

def convert_tuples_to_dictionary(tuples_data):
    return dict((x, y) for x, y in tuples_data)

def return_longer_list(list_1,list_2):
    if len(list_1) >= len(list_2):
        return list_1
    if len(list_1) <= len(list_2):
        return list_2

def return_shorter_list(list_1,list_2):
    if len(list_1) <= len(list_2):
        return list_1
    if len(list_1) >= len(list_2):
        return list_2

def match_percentage(array_1,array_2):

    match=0
    longer_list = return_longer_list(array_1,array_2)
    shorter_list = return_shorter_list(array_1,array_2)

    for note in array_1:

        if note in array_2: 
 
            match = match+1   

    return match/len(longer_list)*100
    # return str(match)+"/"+str(len(longer_list))


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

def return_low_value_by_array(value_1,value_2):
    if len(value_1) <= len(value_2):
        return value_1
    
    if len(value_1) >= len(value_2):
        return value_2

def low_match_percentage(string_1,string_2):

    array_1 = string_1.split("-")
    array_2 = string_2.split("-")

    match=0
    overall=0

    high_value = return_highest_value_by_array(array_1,array_2)
    low_value = return_low_value_by_array(array_1,array_2)


    for i in high_value:

        if i in low_value or i.title() in low_value:
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


def return_alphabet():
    return ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


def return_filename(filename,filepath,file_extension):

    return find_and_replace_array(filename,{
            filepath:"",
            file_extension:""
    })

def remove_integers(string):
    return ''.join([i for i in string if not i.isdigit()]) 

def remove_duplicates_from_dictionary(dictionary):

    array=[]

    for value in dictionary:
        array.append(str(value))

    result =remove_duplicates_from_array(array)

    return_array=[]
    for value in result:
        return_array.append(eval(value))

    return return_array


def album(target_list,dictionary,stack_value):

    artwork_array=[]

    for value in dictionary:

        if target_list["artist"] == value["artist"] and target_list["album"] == value["album"]:
            artwork_array.append(value[stack_value])
        
    return artwork_array

def compress_dictionary(dictionary):

    artwork=[]
    
    for target_list in dictionary:

        artwork.append({
            "artist":target_list["artist"],
            "album":target_list["album"],
            "album_artwork": album(target_list,dictionary,"album_artwork")[0],
           
       })

    return remove_duplicates_from_dictionary(artwork) 


def global_return_path(filename):
    filename_only = find_and_replace_array(filename,{
        "S:\\Website Projects\\MusicKeyFinder\\resources\\api\\":"",
        "\\profile.json":""
    })

    return {
        "artist":filename_only.split("\\")[0],
        "track":filename_only.split("\\")[1],
        "sources":filename_only.replace("\\","-")+".json",
        "path":filename_only.replace("\\","/")
    }
        
     

def change_to_url(value):
    return find_and_replace_array(value.lower(),{
        " ":"-",
        '"':'',
        "'":"",
        "/":"-",
        ":":"",
        "?":"",
        "(":"",
        ")":"",
        "lÃ¸vÃ«":"",
        "---":"-",
        "&":"and",
        ".":"",
        ",":"",
        "é":"e",
        "*":"_",
        ">":"-",
        "-|-":"-",
        "\\":""
    })
  