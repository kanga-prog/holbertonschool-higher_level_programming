#!/usr/bin/python3

def kanga(num):
    return num * 4

def multiply_list_map(my_list=[], number=0):
    return list(map(kanga, my_list))
