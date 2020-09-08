import os
import shutil

def move_file_content(file_to_move,move_location):
    return shutil.move(file_to_move, move_location)
