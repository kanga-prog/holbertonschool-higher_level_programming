#!/usr/bin/python3

def read_file(filename="my_file_0.txt"):
    """
    Reads the first two lines of a text file (UTF-8) and prints them to stdout.

    Args:
        filename (str): The path to the file to be read. Defaults to "my_file_0.txt".
    
    The function uses the `with` statement to open the file in read mode, ensuring
    that the file is properly closed after being read. It reads the first two lines
    of the file and prints them to standard output (stdout).
    
    Example:
        If the content of the file `my_file_0.txt` is:
        "We offer a truly innovative approach to education: focus on building reliable applications..."
        
        Calling `read_file("my_file_0.txt")` would print:
        We offer a truly innovative approach to education: 
        focus on building reliable applications...
    """
    with open(filename, "r", encoding="utf-8") as file:
        # Lire et afficher les deux premières lignes avec une boucle
        for _ in range(2):
            ligne = file.readline().strip()  # Lire une ligne et enlever les espaces/sauts de ligne
            if ligne:  # Si la ligne n'est pas vide, l'afficher
                print(ligne)
