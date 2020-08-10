import tb
import os
import csv

tb.returnMessage("Scanning drives")

scanFiles=tb.scanFilesRecursively()

if scanFiles["totalNumberOfFiles"]==0:
    tb.returnMessage("No data found")
    quit()

tb.returnMessage(str(scanFiles["totalNumberOfFiles"])+" files found")
tb.returnMessage("Exporting data")


row={}

FileInfomation = tb.returnFileInformation()

a=0

out = open('api.csv', 'w', newline='', encoding='utf8') 
writer = csv.DictWriter(out, FileInfomation['returnCSVHead'])
writer.writeheader()
for filename in scanFiles["filelist"]:

    a = a+1

    for column_name in FileInfomation['countColumn']:

        column_title = FileInfomation['returnList'][column_name]
   
        row[column_title]=tb.getDetailsOf(filename,column_name)

        writer.writerow(row)
        
    print(tb.get_current_date()+" => " + str(a) +"/" + str(scanFiles["totalNumberOfFiles"]),end="\r")

tb.returnMessage("Process complete")