#!/usr/bin/python3
"""
Module for reading the contents of a file and printing it to stdout.

This module provides a function `read_file` that opens a file, reads its content,
and prints the content to the standard output.

It is designed to handle text files encoded in UTF-8.
"""


def read_file(filename=""):
    
    """
    Reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): The path to the file to be read. Defaults to "" (empty string).
    
    The function uses the `with` statement to open the file in read mode, ensuring
    that the file is properly closed after being read. It reads the content of the
    file and prints it to standard output (stdout).
    
    Example:
        If the content of the file `my_file_0.txt` is:
        "We offer a truly innovative approach to education: focus on building reliable applications..."
        
        Calling `read_file("my_file_0.txt")` would print:
        We offer a truly innovative approach to education: focus on building reliable applications...
    """
    # Spécifie le chemin relatif vers le fichier qui est dans tests/
    with open("tests/my_file_0.txt", "r", encoding="utf-8") as file:
        print(file.read(), end='')
