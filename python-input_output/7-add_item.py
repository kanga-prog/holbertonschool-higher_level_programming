#!/usr/bin/python3
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Define the filename where the list will be saved
filename = 'add_item.json'

# Try to load the existing list from the file
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

# Add all arguments (excluding the script name itself) to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)

