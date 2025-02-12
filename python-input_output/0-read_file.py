#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to 'tests/my_file_0.txt'.
                         If no filename is provided, it will read 'tests/my_file_0.txt'.

    Returns:
        None: This function does not return any value; it only prints the contents of the file.

    Usage:
        read_file()  # Reads 'tests/my_file_0.txt' and prints its contents to stdout.
        read_file("other_file.txt")  # Reads 'other_file.txt' and prints its contents to stdout.
    """
    with open('tests/my_file_0.txt', 'r',encoding='utf-8') as file:
        print(file.read(), end="")