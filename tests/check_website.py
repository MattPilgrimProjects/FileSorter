import requests
import requests
import urllib.parse

f = open("api.txt","r")

content = f.read()

# print()


# https://www.karaoke-version.com/api/songfile/

www="https://www.karaoke-version.com/api/songfile/?query="+urllib.parse.quote(content)
print(www)

request = requests.get(www)
if request.status_code == 200:
    print('Web site exists')
    print("8858")
    # print (request.content)
else:
    print('Web site does not exist') 

# https://www.karaoke-version.com/backing-track-piano/
# https://www.karaoke-version.com/bass-backing-track/
# https://www.karaoke-version.com/drums-backing-track/
# https://www.karaoke-version.com/guitar-backing-track/
# https://www.karaoke-version.com/backing-track-piano/
# https://www.karaoke-version.com/mp3-backingtrack/
# https://www.karaoke-version.com/karaoke/
