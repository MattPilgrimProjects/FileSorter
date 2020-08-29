import json
import glob
import subprocess
import os.path
import shutil
import os
import re
import os.path
from datetime import datetime
import csv
import win32com.client
import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import urllib.request
import re
import bs4 as bs
import csv
import difflib

#Install under pywin32


def importCSVData(filename):
    returnFile=[]
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            returnFile.append(row) 
        return returnFile

def scanFilesRecursively():

    totalNumberOfFiles=0
    filelist=[]

    for filename in returnFullFileList():

        try:
            filename
            pass
        except (UnicodeEncodeError,AttributeError):
            returnMessage("File error: " + filename)
            pass
        else:
            totalNumberOfFiles=totalNumberOfFiles+1
            filelist.append(filename)
            pass

    return {
        "filelist":filelist,
        "totalNumberOfFiles":totalNumberOfFiles
    }

def returnMessage(text):
    return print(get_current_date() +" => "+ text)

def returnUpdateMessage(text):
    return print(get_current_date() +" => "+ text,end="\r")

def returnFileInformation():
    numberOfColumns=-1
    returnCSVHead=[]
    returnList={}
    countColumn=[]
    mylist = returnAllTagsFromSettings()
        
    for headerTitle in returnCSVHeader():

        numberOfColumns = numberOfColumns+1

        if headerTitle =="FILE_EXTENSION" or headerTitle=="PATH" or headerTitle=="NAME":
            returnCSVHead.append(headerTitle)
            returnList[numberOfColumns]=headerTitle
            countColumn.append(numberOfColumns)


        if headerTitle in mylist:
            returnCSVHead.append(headerTitle)
            returnList[numberOfColumns]=headerTitle
            countColumn.append(numberOfColumns)

        pass

    return {
        "returnCSVHead":returnCSVHead,
        "countColumn":countColumn,
        "returnList":returnList
    }


def returnAllTagsFromSettings():
    array=[]
    scanLibrary= import_file("settings.json")["Library"]

    for info in scanLibrary:

        test = scanLibrary[info]["sort_filepath"]

        for item in test.split("%"):


            if re.match("[A-Z_]",item) and ":" not in item:
                item = item.replace("_YEAR","")
                item = item.replace("_MONTH","")
                item = item.replace("_DAY","")
                array.append(item)
    return list(dict.fromkeys(array))

def getDetailsOf(filename,header):

    sh=returnwin32com() 

    try:
        ns = sh.NameSpace(os.path.dirname(filename))
        AFile = ns.ParseName(os.path.basename(filename))
        ns.GetDetailsOf(AFile, header)
        value = ns.GetDetailsOf(AFile, header)
        return valueDecode(value)
        
    except(AttributeError):
        pass

    

def valueDecode(value):
    value = value.encode("ascii", "ignore")
            
    value = value.decode()

    return value


def returnwin32com():
    return win32com.client.gencache.EnsureDispatch('Shell.Application',0)

def importCSV(filename):
    with open(filename, mode='r') as csv_file:
        csv.DictReader(csv_file)
    return csv_file


def date_format_1(tag,sort_filepath,file_data):
    split = file_data["%MEDIA_CREATE_DATE%"].split(":")

    if "%"+tag+"_YEAR%" in sort_filepath: year = split[0]
    if "%"+tag+"_MONTH%" in sort_filepath: month = split[1]

    return {
        "%"+tag+"_YEAR%":year,
        "%"+tag+"_MONTH%":month
    }

def parseResult(filename):
    return returnErrorHandlingExifTool(filename)
    
def returnErrorHandlingExifTool(filename):
    try:
        return returnMetaData(filename)
    except:
        return False

def import_file(filename):
    jsonFile = open(filename, 'r')
    config = json.load(jsonFile)
    jsonFile.close()
    return config

def import_json(filename):
    jsonFile = open(filename, 'r')
    config = json.load(jsonFile)
    jsonFile.close()
    return config

def returnLibraryList():
    scanLibrary= import_file("settings.json")["Library"]
    array=[]
    for LibraryTitle in scanLibrary:
        array.append(LibraryTitle)

    return array

def returnFullFileExtensionList():
    config = import_file("settings.json")
    array=[]
    for LibraryTitle in config["Library"]:

        array.extend(config["Library"][LibraryTitle]["file_extensions"])
        
    return array

def returnCSVHeader():
    return [
            "NAME",
            "SIZE",
            "ITEM_TYPE",
            "DATE_MODIFIED",
            "DATE_CREATED",
            "DATE_ACCESSED",
            "ATTRIBUTES",
            "OFFLINE_STATUS",
            "AVAILABILITY",
            "PERCEIVED_TYPE",
            "OWNER",
            "KIND",
            "DATE_TAKEN",
            "CONTRIBUTING_ARTISTS",
            "ALBUM",
            "YEAR",
            "GENRE",
            "CONDUCTORS",
            "TAGS",
            "RATING",
            "AUTHORS",
            "TITLE",
            "SUBJECT",
            "CATEGORIES",
            "COMMENTS",
            "COPYRIGHT",
            "#",
            "LENGTH",
            "BIT_RATE",
            "PROTECTED",
            "CAMERA_MODEL",
            "DIMENSIONS",
            "CAMERA_MAKER",
            "COMPANY",
            "FILE_DESCRIPTION",
            "MASTERS_KEYWORDS",
            "MASTERS_KEYWORDS",
            "",
            "",
            "",
            "",
            "",
            "PROGRAM_NAME",
            "DURATION",
            "IS_ONLINE",
            "IS_RECURRING",
            "LOCATION",
            "OPTIONAL_ATTENDEE_ADDRESSES",
            "OPTIONAL_ATTENDEES",
            "ORGANIZER_ADDRESS",
            "ORGANIZER_NAME",
            "REMINDER_TIME",
            "REQUIRED_ATTENDEE_ADDRESSES",
            "REQUIRED_ATTENDEES",
            "RESOURCES",
            "MEETING_STATUS",
            "FREE/BUSY_STATUS",
            "TOTAL_SIZE",
            "ACCOUNT_NAME",
            "",
            "TASK_STATUS",
            "COMPUTER",
            "ANNIVERSARY",
            "ASSISTANT'S_NAME",
            "ASSISTANT'S_PHONE",
            "BIRTHDAY",
            "BUSINESS_ADDRESS",
            "BUSINESS_CITY",
            "BUSINESS_COUNTRY/REGION",
            "BUSINESS_P.O._BOX",
            "BUSINESS_POSTAL_CODE",
            "BUSINESS_STATE_OR_PROVINCE",
            "BUSINESS_STREET",
            "BUSINESS_FAX",
            "BUSINESS_HOME_PAGE",
            "BUSINESS_PHONE",
            "CALLBACK_NUMBER",
            "CAR_PHONE",
            "CHILDREN",
            "COMPANY_MAIN_PHONE",
            "DEPARTMENT",
            "E-MAIL_ADDRESS",
            "E-MAIL2",
            "E-MAIL3",
            "E-MAIL_LIST",
            "E-MAIL_DISPLAY_NAME",
            "FILE_AS",
            "FIRST_NAME",
            "FULL_NAME",
            "GENDER",
            "GIVEN_NAME",
            "HOBBIES",
            "HOME_ADDRESS",
            "HOME_CITY",
            "HOME_COUNTRY/REGION",
            "HOME_P.O._BOX",
            "HOME_POSTAL_CODE",
            "HOME_STATE_OR_PROVINCE",
            "HOME_STREET",
            "HOME_FAX",
            "HOME_PHONE",
            "IM_ADDRESSES",
            "INITIALS",
            "JOB_TITLE",
            "LABEL",
            "LAST_NAME",
            "MAILING_ADDRESS",
            "MIDDLE_NAME",
            "CELL_PHONE",
            "NICKNAME",
            "OFFICE_LOCATION",
            "OTHER_ADDRESS",
            "OTHER_CITY",
            "OTHER_COUNTRY/REGION",
            "OTHER_P.O._BOX",
            "OTHER_POSTAL_CODE",
            "OTHER_STATE_OR_PROVINCE",
            "OTHER_STREET",
            "PAGER",
            "PERSONAL_TITLE",
            "CITY",
            "COUNTRY/REGION",
            "P.O._BOX",
            "POSTAL_CODE",
            "STATE_OR_PROVINCE",
            "STREET",
            "PRIMARY_E-MAIL",
            "PRIMARY_PHONE",
            "PROFESSION",
            "SPOUSE/PARTNER",
            "SUFFIX",
            "TTY/TTD_PHONE",
            "TELEX",
            "WEBPAGE",
            "CONTENT_STATUS",
            "CONTENT_TYPE",
            "DATE_ACQUIRED",
            "DATE_ARCHIVED",
            "DATE_COMPLETED",
            "DEVICE_CATEGORY",
            "CONNECTED",
            "DISCOVERY_METHOD",
            "FRIENDLY_NAME",
            "LOCAL_COMPUTER",
            "MANUFACTURER",
            "MODEL",
            "PAIRED",
            "CLASSIFICATION",
            "STATUS",
            "STATUS",
            "CLIENT_ID",
            "CONTRIBUTORS",
            "CONTENT_CREATED",
            "LAST_PRINTED",
            "DATE_LAST_SAVED",
            "DIVISION",
            "DOCUMENT_ID",
            "PAGES",
            "SLIDES",
            "TOTAL_EDITING_TIME",
            "WORD_COUNT",
            "DUE_DATE",
            "END_DATE",
            "FILE_COUNT",
            "FILE_EXTENSION",
            "FILENAME",
            "FILE_VERSION",
            "FLAG_COLOR",
            "FLAG_STATUS",
            "SPACE_FREE",
            "",
            "",
            "GROUP",
            "SHARING_TYPE",
            "BIT_DEPTH",
            "HORIZONTAL_RESOLUTION",
            "WIDTH",
            "VERTICAL_RESOLUTION",
            "HEIGHT",
            "IMPORTANCE",
            "IS_ATTACHMENT",
            "IS_DELETED",
            "ENCRYPTION_STATUS",
            "HAS_FLAG",
            "IS_COMPLETED",
            "INCOMPLETE",
            "READ_STATUS",
            "SHARED",
            "CREATORS",
            "DATE",
            "FOLDER_NAME",
            "FOLDER_PATH",
            "FOLDER",
            "PARTICIPANTS",
            "PATH",
            "BY_LOCATION",
            "TYPE",
            "CONTACT_NAMES",
            "ENTRY_TYPE",
            "LANGUAGE",
            "DATE_VISITED",
            "DESCRIPTION",
            "LINK_STATUS",
            "LINK_TARGET",
            "URL",
            "",
            "",
            "",
            "MEDIA_CREATED",
            "DATE_RELEASED",
            "ENCODED_BY",
            "EPISODE_NUMBER",
            "PRODUCERS",
            "PUBLISHER",
            "SEASON_NUMBER",
            "SUBTITLE",
            "USER_WEB_URL",
            "WRITERS",
            "",
            "ATTACHMENTS",
            "BCC_ADDRESSES",
            "BCC",
            "CC_ADDRESSES",
            "CC",
            "CONVERSATION_ID",
            "DATE_RECEIVED",
            "DATE_SENT",
            "FROM_ADDRESSES",
            "FROM",
            "HAS_ATTACHMENTS",
            "SENDER_ADDRESS",
            "SENDER_NAME",
            "STORE",
            "TO_ADDRESSES",
            "TO_DO_TITLE",
            "TO",
            "MILEAGE",
            "ALBUM_ARTIST",
            "SORT_ALBUM_ARTIST",
            "ALBUM_ID",
            "SORT_ALBUM",
            "SORT_CONTRIBUTING_ARTISTS",
            "BEATS-PER-MINUTE",
            "COMPOSERS",
            "SORT_COMPOSER",
            "DISC",
            "INITIAL_KEY",
            "PART_OF_A_COMPILATION",
            "MOOD",
            "PART_OF_SET",
            "PERIOD",
            "COLOR",
            "PARENTAL_RATING",
            "PARENTAL_RATING_REASON",
            "SPACE_USED",
            "EXIF_VERSION",
            "EVENT",
            "EXPOSURE_BIAS",
            "EXPOSURE_PROGRAM",
            "EXPOSURE_TIME",
            "F-STOP",
            "FLASH_MODE",
            "FOCAL_LENGTH",
            "35MM_FOCAL_LENGTH",
            "ISO_SPEED",
            "LENS_MAKER",
            "LENS_MODEL",
            "LIGHT_SOURCE",
            "MAX_APERTURE",
            "METERING_MODE",
            "ORIENTATION",
            "PEOPLE",
            "PROGRAM_MODE",
            "SATURATION",
            "SUBJECT_DISTANCE",
            "WHITE_BALANCE",
            "PRIORITY",
            "PROJECT",
            "CHANNEL_NUMBER",
            "EPISODE_NAME",
            "CLOSED_CAPTIONING",
            "RERUN",
            "SAP",
            "BROADCAST_DATE",
            "PROGRAM_DESCRIPTION",
            "RECORDING_TIME",
            "STATION_CALL_SIGN",
            "STATION_NAME",
            "SUMMARY",
            "SNIPPETS",
            "AUTO_SUMMARY",
            "RELEVANCE",
            "FILE_OWNERSHIP",
            "SENSITIVITY",
            "SHARED_WITH",
            "SHARING_STATUS",
            "",
            "PRODUCT_NAME",
            "PRODUCT_VERSION",
            "SUPPORT_LINK",
            "SOURCE",
            "START_DATE",
            "SHARING",
            "AVAILABILITY_STATUS",
            "STATUS",
            "BILLING_INFORMATION",
            "COMPLETE",
            "TASK_OWNER",
            "SORT_TITLE",
            "TOTAL_FILE_SIZE",
            "LEGAL_TRADEMARKS",
            "VIDEO_COMPRESSION",
            "DIRECTORS",
            "DATA_RATE",
            "FRAME_HEIGHT",
            "FRAME_RATE",
            "FRAME_WIDTH",
            "SPHERICAL",
            "STEREO",
            "VIDEO_ORIENTATION",
            "TOTAL_BITRATE"
    ]

def returnAllFilesByExtension(singleScanLocations,file_extension):
    array=[]
    for filename in glob.iglob( singleScanLocations + '/**/*'+file_extension, recursive=True):
            array.append(filename)
            pass
    return array


def returnFullGlobList():
    array=[]

    for singleScanLocations in import_file("settings.json")["Search_Location"]:

        for filename in glob.iglob( singleScanLocations + '/**/*.*', recursive=True):
            array.append(filename)
        pass
    pass

    return array

def returnFullFileList():
 
    array=[]

    for file_extension in returnFullFileExtensionList():
        
        for singleScanLocations in import_file("settings.json")["Search_Location"]:

            for filename in glob.iglob( singleScanLocations + '/**/*' + file_extension , recursive=True):
                array.append(filename)
            pass
        pass

    return array


def addExifTool(input_file):

   
    process = subprocess.Popen(["exiftool.exe",input_file],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,universal_newlines=True)

    return process.stdout

def validate(date_text):
    return date_text.split(":")

def basename(filename):
    return os.path.basename(filename)

def is_jsonable(x):
    try:
        json.dumps(x)
        return True
    except (TypeError, OverflowError):
        return False

def returnMetaData(input_file):

    filename = input_file.replace("\\","/")


    info={}

    for output in addExifTool(filename):


        line = output.split(":",1)
        
 
        key = "%"+line[0].strip().replace(" ","_")+"%"

        key = key.upper()
        

        value = line[1].strip()

  
        info["%FILE_EXTENSION%"]= get_file_extension(filename)
        
        info[key]=value

    return info
        

def export_json(filename,array):
    with open(filename, 'w') as json_file:
        json.dump(array, json_file,indent=4)  
        
    
def file_exists(filename):
    if os.path.exists(filename):
        return True
    else:
        return False

def copy_file(file,destination):

    file = os.path.abspath(file)

    destination = os.path.abspath(destination)

    return shutil.copy2(file,destination)

def file_does_not_exists(filename):
    if os.path.exists(filename):
        return False
    else:
        return True

def create_recursive_diretory(path):
    return os.makedirs(path, exist_ok=True)

def get_file_size(filename):
    return str(os.stat(filename).st_size) 

def isDirectory(filename):
    return os.path.isdir(filename)


def update_JSON(filename,filedata):
    output = import_file(filename)
    output.update(filedata)
    export_json(filename,output)

def get_file_extension(filename):
    return os.path.splitext(filename)[1][1:]


def get_current_date():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def get_basename(filename):
    splittext = os.path.basename(filename)
    return splittext


def createCSVHeader(filepath, header):
    out = open(filepath, 'w', newline='', encoding='utf8') 
    writer = csv.DictWriter(out,header)
    writer.writeheader()
    return writer
    
def infoTag(info):

    array = []

    print(info)

    for n in range(320):
        array.append(info[n])
    return array 


def returnURLContent(url):
    return urllib.request.urlopen(url).read()

def createFile(file,content):
    f = open(file, "wb")
    f.write(content)
    f.close()

def parseLinksFromHTML(file):
    http = httplib2.Http()
    status, response = http.request(file)
    return bs.BeautifulSoup(response, 'html.parser',parseOnlyThese=SoupStrainer('a'))

def removeDuplicates(array):
    return list(dict.fromkeys(array))

def matchRadio(argument_1,argument_2):
    return difflib.SequenceMatcher(None,argument_1,argument_2).ratio()

def matchRatio(argument_1,argument_2):
    return difflib.SequenceMatcher(None,argument_1,argument_2).ratio()

