import os
import pickle
from src.decorators.colorize_message import print_error


def load_data(storage_file):
    if os.path.exists(storage_file):
        try:
            with open(storage_file, "rb") as file:
                return pickle.load(file)
        except EOFError:
            print_error("File is empty.")
            return []
    return []


def save_data(data, storage_file):
    with open(storage_file, "wb") as file:
        pickle.dump(data, file)
