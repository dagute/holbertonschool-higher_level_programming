#!/usr/bin/python3
"""Load, add, save"""
import os.path
import sys

arg = sys.argv[1:]

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


my_list = []

if os.path.exists("./add_item.json"):
    my_list = load_from_json_file("add_item.json")

save_to_json_file(my_list + arg, "add_item.json")
