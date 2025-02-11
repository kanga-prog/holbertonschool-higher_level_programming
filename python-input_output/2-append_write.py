#/usr/bin/python

def append_write(filename="", text=""):
    # Open the file in append mode ('a') with UTF-8 encoding, create it if it doesn't exist
    with open(filename, 'a', encoding='utf-8') as file:
        # Write the given text to the file
        file.write(text)
        # Return the number of characters added
        return len(text)
