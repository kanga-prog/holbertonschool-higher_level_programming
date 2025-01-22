#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # Utilise une compréhension de dictionnaire
    return {key: value * 2 for key, value in a_dictionary.items()}
