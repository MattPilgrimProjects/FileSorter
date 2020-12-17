import app
import controller
import library.download

midi_library_database_file = app.settings["midi_library_database_file"]
unprocessed_database_file = app.settings["midi_library_database_file"]
processed_database_file = app.settings["main_database_file"]

###

library.comment.returnMessage("Start")

controller.processed_database(
    unprocessed_database_file,
    processed_database_file
)

library.download.download_midi(
    midi_library_database_file
)

library.comment.returnMessage("Completed")