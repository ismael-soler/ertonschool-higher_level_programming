#!/usr/bin/python3
""" add all arguments to Python list """
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
filename = "add_item.json"
listObject = []

if os.path.exists(filename):
    listObject = load_from_json_file(filename)

for element in args:
    listObject.append(element)
save_to_json_file(listObject, filename)
