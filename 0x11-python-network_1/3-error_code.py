#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the body of the response
"""
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as w:
            r = w.read().decode('utf-8')
            print(r)
    except urllib.error.HTTPError as err:
        print("Error code:", err.code)
