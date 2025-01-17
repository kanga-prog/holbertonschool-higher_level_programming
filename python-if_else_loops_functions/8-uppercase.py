#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:  # Si c'est une minuscule
            char = chr(ord(char) - 32)  # Convertir en majuscule
        print("{}".format(char), end="")
    print()  # Ajouter un saut de ligne à la fin
