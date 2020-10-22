import app

import xmltodict

with open("S:\\Midi-Library\\karaokeversion_catalog_en_GBP0.xml") as fd:
    doc = xmltodict.parse(fd.read())

export_json = doc["artists"]["artist"]

app.json.export_json("test.json",export_json)

def songs(artist):
    print("---")
    print(artist["name"])
    print(artist["songs"]["song"]["name"])
    print(artist["songs"]["song"]["url"])
    for value in artist["songs"]["song"]["files"]["file"]:
        print(value["@track_type"])
        pass
    return None



for artist in export_json:


    try:
        artist["songs"]["song"]["name"]
    except TypeError:
        print("---")
    else:
        songs(artist)

      



 


