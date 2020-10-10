import app

csv = app.csv

app.comment.returnMessage("Scanning drives")

scanFiles=app.tb.scanFilesRecursively()

if scanFiles["totalNumberOfFiles"]==0:
    app.comment.returnMessage("No data found")
    quit()
else:
    app.comment.returnMessage(str(scanFiles["totalNumberOfFiles"])+" files found")
    app.comment.returnMessage("Exporting data")

row={}
 
FileInfomation = app.tb.returnFileInformation()

file_count=0

writer = csv.create_csv_header(app.settings["search_output"],FileInfomation['returnCSVHead'])

for filename in scanFiles["filelist"]:

    file_count = file_count+1

    for column_name in FileInfomation['countColumn']:

        column_title = FileInfomation['returnList'][column_name]
   
        row[column_title]=app.tb.getDetailsOf(filename,column_name)

    writer.writerow(row)
    
    app.comment.returnUpdateMessage(str(file_count) +"/" + str(scanFiles["totalNumberOfFiles"]))

app.comment.returnMessage("Process complete")