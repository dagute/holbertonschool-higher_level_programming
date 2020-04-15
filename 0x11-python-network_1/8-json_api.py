#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":
    """definition"""
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    if r.json() == {}:
        print("No result")
    else:
        try:
            print("[{}] {}".format(r.json()["id"], r.json()["name"]))
        except ValueError:
            print("Not a valid JSON")
