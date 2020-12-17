import config
import library.json

### DO NOT INCUDE ANY REFERENCE TO SOURCES IN THIS CONTROLLER ###
### ANY SOURCES REFERENCED NEED TO BE IN CONFIG ###

def processed_database(unprocessed_database,processed_database):
    export_data = []
    for data in library.json.import_json(unprocessed_database):

        return_data = config.source_compile(data)

        if return_data:
            export_data.append(return_data)

    return library.json.export_json(processed_database, export_data)
