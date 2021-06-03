#!/usr/local/bin python3

import os
import shutil
from pathlib import Path

x = input('What folder do you want to clean? ')

# The path for listing items
path = '/Users/chrisbowen/' + x + '/'


# To be implemented. Run through the dict
file_types = {'.zip': 'Zip Files', '.jpg': 'Images', '.png': 'Images', '.iso': 'ISO Images', \
                '.csv': 'CSV Files', '.dmg': 'Program Downloads', '.json': 'JSON Files', \
                '.sql': 'SQL Files'}

# The list of items
files = os.listdir(path)


def check_folder_exists(folder_name):
    if Path(path + folder_name).is_dir():
        return True
    else:
        os.makedirs(path + folder_name)
        return True


def move_files(folder_name, file_name):
    if check_folder_exists(folder_name):
        shutil.move(path + filename, path + folder_name)


# Loop to print each filename separately
for filename in files:

    if ".zip" in filename:
        folder_name = "Zip Files"
        move_files(folder_name, filename)

    elif ".jpg" in filename:
        folder_name = "Images"
        move_files(folder_name, filename)

    elif ".jpeg" in filename:
        folder_name = "Images"
        move_files(folder_name, filename)

    elif ".png" in filename:
        folder_name = "Images"
        move_files(folder_name, filename)

    elif ".gpx" in filename:
        folder_name = "GPX Files"
        move_files(folder_name, filename)

    elif ".pdf" in filename:
        folder_name = "PDF Files"
        move_files(folder_name, filename)

    elif ".iso" in filename:
        folder_name = "ISO images"
        move_files(folder_name, filename)

    elif ".csv" in filename:
        folder_name = "CSV Files"
        move_files(folder_name, filename)

    elif ".numbers" in filename:
        folder_name = "Numbers Files"
        move_files(folder_name, filename)

    elif ".xml" in filename:
        folder_name = "XML Files"
        move_files(folder_name, filename)

    elif ".dmg" in filename:
        folder_name = "Program Downloads"
        move_files(folder_name, filename)

    elif ".json" in filename:
        folder_name = "JSON Files"
        move_files(folder_name, filename)

    elif ".sql" in filename:
        folder_name = "SQL Files"
        move_files(folder_name, filename)

    elif ".sqlite3" in filename:
        folder_name = "SQL Files"
        move_files(folder_name, filename)

print("Completed...")
