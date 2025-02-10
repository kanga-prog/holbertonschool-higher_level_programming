# Python - Input/Output

## Author
Guillaume

## Overview
This project covers the basics of input/output operations in Python, focusing on working with files, JSON serialization/deserialization, and basic Python data structures. You'll learn how to read, write, and append data to files, manage JSON objects, and handle command-line arguments.

---

## Learning Objectives

By the end of this project, you should be able to:

- Understand and explain the fundamentals of file operations in Python (reading, writing, appending).
- Use the `with` statement to ensure files are properly handled and closed.
- Work with JSON to serialize and deserialize Python objects.
- Handle command-line parameters in Python scripts.
- Understand how Python class instances can be serialized into JSON.

---

## Requirements

- **Python version**: 3.8.5
- **Editors**: Allowed editors: vi, vim, emacs
- **Style**: Code should adhere to PEP 8 (pycodestyle 2.7.*)
- **File format**: All files should end with a newline.

### Specific rules:
- Each Python file should begin with `#!/usr/bin/python3`.
- Each Python script must be executable.
- Your tests must be inside a folder named `tests` and be `.txt` files.
- Test scripts should be executed using `python3 -m doctest ./tests/*`.
- Document every class and function properly.

---

## Tasks

### 0. Read file
Write a function `read_file(filename="")` that reads a text file (UTF-8) and prints its contents.

### 1. Write to a file
Write a function `write_file(filename="", text="")` that writes a string to a text file (UTF-8) and returns the number of characters written.

### 2. Append to a file
Write a function `append_write(filename="", text="")` that appends a string at the end of a text file (UTF-8) and returns the number of characters added.

### 3. To JSON string
Write a function `to_json_string(my_obj)` that returns the JSON representation of an object (string).

### 4. From JSON string to Object
Write a function `from_json_string(my_str)` that returns an object (Python data structure) represented by a JSON string.

### 5. Save Object to a file
Write a function `save_to_json_file(my_obj, filename)` that writes an object to a text file, using a JSON representation.

### 6. Create object from a JSON file
Write a function `load_from_json_file(filename)` that creates an object from a JSON file.

### 7. Load, add, save
Write a script that adds all arguments to a Python list and then saves them to a file named `add_item.json`.

### 8. Class to JSON
Write a function `class_to_json(obj)` that returns the dictionary description with simple data structures for JSON serialization of an object.

### 9. Student to JSON
Write a class `Student` that defines a student by `first_name`, `last_name`, and `age`. Implement a method `to_json(self)` that retrieves a dictionary representation of a Student instance.

### 10. Student to JSON with filter
Extend the `Student` class from task 9 by adding a method `to_json(self, attrs=None)` that only retrieves the attributes contained in the `attrs` list (if provided).

### 11. Student to disk and reload
Write a class `Student` that defines a student with attributes `first_name`, `last_name`, and `age`, and includes the `to_json` method from task 10. Implement functionality to save the student object to disk and reload it from disk.

---

## Repo Structure

```plaintext
holbertonschool-higher_level_programming/
 ├── python-input_output/
 │    ├── 0-read_file.py
 │    ├── 1-write_file.py
 │    ├── 2-append_write.py
 │    ├── 3-to_json_string.py
 │    ├── 4-from_json_string.py
 │    ├── 5-save_to_json_file.py
 │    ├── 6-load_from_json_file.py
 │    ├── 7-add_item.py
 │    ├── 8-class_to_json.py
 │    ├── 9-student.py
 │    ├── 10-student.py
 │    ├── 11-student_to_disk_reload.py
 │    └── tests/
 │        └── *.txt
 └── README.md
```

---

## Contributing

Feel free to clone this repository and contribute by opening pull requests. You are encouraged to work together on test cases and ensure all edge cases are

## Resources
- [Dive Into Python 3: Chapter 11. Files](https://diveintopython3.problemsolving.io/)
- [Automate the Boring Stuff with Python: Chapters 8 & 14](https://automatetheboringstuff.com/)
- [JSON Encoder/Decoder](https://docs.python.org/3/library/json.html)
- [Python sys package](https://docs.python.org/3/library/sys.html)