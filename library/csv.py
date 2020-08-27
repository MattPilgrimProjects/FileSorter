import csv

def create_csv_header(filename,csv_header):
    out = open(filename, 'w', newline='', encoding='utf8') 
    writer = csv.DictWriter(out, csv_header)
    writer.writeheader()
    return writer