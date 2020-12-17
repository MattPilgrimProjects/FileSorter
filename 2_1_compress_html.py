import config
import library.convert

################################

library.comment.returnMessage("Start")

for data_extractor_config in config.data_extractor:

    ### Export uncompressed data (or dev mode)
    library.convert.convert_html_to_json(data_extractor_config)

library.comment.returnMessage("Completed")
