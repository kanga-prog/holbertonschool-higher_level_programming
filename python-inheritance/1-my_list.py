#!/usr/bin/python3

"""
ce module contient une class heritage d'une autre class nomé list.

"""
class MyList(list):
    """
    A class that inherits from the built-in list class.
    
    This class provides a method to print the list in sorted order without
    modifying the original list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the original list.
        
        The list is sorted using the built-in sorted() function, which returns
        a new list, leaving the original list unchanged.
        """
        print(sorted(self))
