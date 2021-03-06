#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as w:
        h = w.read()
        print("Body response:")
        print("\t- type: {}".format(type(h)))
        print("\t- content: {}".format(h))
        print("\t- utf8 content: {}".format(h.decode('utf-8')))
