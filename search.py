import tb
import os
import csv

         
info={}
i=0
a=0
filelist=[]
list2=[]
array=tb.returnCSVHeader()

returnList={}
countColumn=[]
returnCSVHead=[]
mylist = tb.returnAllTagsFromSettings()

x=-1
for headerTitle in tb.returnCSVHeader():
    x = x+1

    if headerTitle =="FILE_EXTENSION" or headerTitle=="PATH" or headerTitle=="NAME":
        returnCSVHead.append(headerTitle)
        returnList[x]=headerTitle
        countColumn.append(x)


    if headerTitle in mylist:
        returnCSVHead.append(headerTitle)
        returnList[x]=headerTitle
        countColumn.append(x)

    pass

print(returnList)
print(countColumn)

print(tb.get_current_date() + " => Scanning drives")

for filename in tb.returnFullGlobList():

    try:
        filename
        pass
    except UnicodeEncodeError:
        print("file error: " + filename)
        pass
    else:
        i=i+1
        filelist.append(filename)
        pass

print(tb.get_current_date() + " => "+str(i)+" files found")   
print(tb.get_current_date() + " => Exporting data")  

row={}



out = open('api.csv', 'w', newline='', encoding='utf8') 
writer = csv.DictWriter(out, returnCSVHead)
writer.writeheader()
for filename in filelist:

    a = a+1

    for column_name in countColumn:

        row[returnList[column_name]]=tb.getDetailsOf(filename,column_name)

    writer.writerow(row)
    print(tb.get_current_date()+" => " + str(a) +"/" + str(i),end="\r")

    pass

print(tb.get_current_date() + " => Process complete")

