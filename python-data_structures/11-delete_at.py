#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the list unchanged    
    # Use slicing to delete the item at idx and return the modified list
    return my_list[:idx] + my_list[idx+1:]
