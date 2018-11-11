import pickle
import os
from os.path import isfile

file_name = "saved_game_krestiki_noliki.txt"


# save field data to file
def dump_to_file(field):
    try:
        with open(file_name, 'wb') as f:
            pickle.dump(field, f)
        result = True
    except:
        result = False
    return result


# load field data from file
def load_from_file():
    field = []
    try:
        with open(file_name, 'rb') as f:
            field = pickle.load(f)
        return field
    except:
        return field


# remove file with data
def remove_file():
    try:
        if os.path.isfile(file_name):  # check, if file exists in directory
            os.remove(file_name)
        return True
    except:
        print("File was not removed!")
        return False
