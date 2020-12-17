import library.url
import library.json
import library.comment
import library.cron
import library.scan
import library.parser

import sys

################################

def start_handler(line, config):

    line_count = line.split(config)

    if len(line_count) != 0:
        return line_count[1]
    else:
        return line

def end_handler(line, config):

    return line.split(config)[0]

def config_handler(line, config):

    if "start" in config and config["start"]:
        line = start_handler(line, config["start"])

    if "end" in config and config["end"]:
        line = end_handler(line, config["end"])

    line = library.parser.find_and_replace_array(
        line, config["find_and_replace"])

    if "split" in config:
        track_id = line.split("-")
        line = track_id[0]+"-"+track_id[1]

    return line

def uncompressed_filter(processed,config):

    export_list =[]
    for line in processed:


        if "match" in config and config["match"] in line:
            export_list.append(config_handler(line, config))
        else:
            pass

    return export_list

def uncompressed_data(import_path,config):

    parse = config["filter"]
    split = config["filter_tags"]
    url = library.parser.parseLinksFromHTML(import_path, parse)

    processed = url.split(split)

    export_list=[] 

    for title,data in config["data"].items():

        export_list.append({title:uncompressed_filter(processed,data)})
    
    return export_list

def convert_html_to_json(config):

    source = config["source"]

    import_filepath = config["import_filepath"]
    export_filepath = config["export_filepath"]
 
    library.comment.returnMessage("Importing web content from "+source)

    for filename in library.scan.scan_file_recursively(import_filepath+"*.html"):

        localhost = filename.replace(import_filepath,"http://localhost/live/"+source+"/")

        export_path = library.parser.find_and_replace_array(filename,{
            import_filepath:export_filepath,
            ".html":".json"
        })

        if library.file.file_exists(export_path):
            pass
        else:
            library.json.export_json(export_path,uncompressed_data(localhost,config))
    
    return "Complete"