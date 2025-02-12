#!/usr/bin/python3

import json

def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Args:
        my_str (str): A string representing a JSON object.

    Returns:
        object: The Python object represented by the JSON string.
    
    Example:
        s = '{"name": "John", "age": 30}'
        obj = from_json_string(s)
        print(obj)  # Output: {'name': 'John', 'age': 30}
    """
    return json.loads(my_str)
