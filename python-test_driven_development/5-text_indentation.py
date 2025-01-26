#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after each\
          of the characters: '.', '?', and ':'.

    Parameters:
    text (str): The input string to be processed.

    Raises:
    TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in ['.', '?', ':']:
            print(text[:i + 1].strip())
            print()  # print the first new line
            text = text[i + 1:].lstrip()
            i = 0  # reset i to start checking the new segment
        else:
            i += 1
    # Print the remaining part of the text (after the last punctuation mark)
    if text:
        print(text.strip())
