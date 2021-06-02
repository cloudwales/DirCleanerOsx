#!/usr/local/bin python3

import os
import shutil
from pathlib import Path

# The path for listing items
path = '/Users/chrisbowen/Downloads/'

# The list of items
files = os.listdir(path)

def check_folder_exists(folder):
    if Path(path + folder).is_dir():
        return True
    else:
        return False


# Loop to print each filename separately
for filename in files:
    if ".zip" in filename:
        if check_folder_exists("zip"):
            shutil.move(path + filename, path + "zip/")
        else:
            os.makedirs(path + "zip/")
    elif ".jpg" in filename:
        if check_folder_exists("images"):
            shutil.move(path + filename, path + "images/")
        else:
            os.makedirs(path + "images/")
    elif ".iso" in filename:
        if check_folder_exists("iso_images"):
            shutil.move(path + filename, path + "iso_images/")
        else:
            os.makedirs(path + "iso_images/")
    elif ".csv" in filename:
        if check_folder_exists("csv_files"):
            shutil.move(path + filename, path + "csv_files/")
        else:
            os.makedirs(path + "csv_files/")
    elif ".dmg" in filename:
        if check_folder_exists("programs"):
            shutil.move(path + filename, path + "programs/")
        else:
            os.makedirs(path + "programs/")
    elif ".json" in filename:
        if check_folder_exists("json_files"):
            shutil.move(path + filename, path + "json_files/")
        else:
            os.makedirs(path + "json_files/")
    elif ".sql" in filename:
        if check_folder_exists("sql_files"):
            shutil.move(path + filename, path + "sql_files/")
        else:
            os.makedirs(path + "sql_files/")


