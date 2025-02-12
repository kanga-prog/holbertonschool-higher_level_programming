#!/usr/bin/python3
import json

def load_from_json_file(filename):
    """
    Creates an object from a "JSON file".

    Args:
        filename (str): The name of the file to load the JSON object from.

    Returns:
        object: The Python object representing the JSON content.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
