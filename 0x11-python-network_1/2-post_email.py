#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of the respose"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    d = parse.urlencode({"email": argv[2]}).encode()
    r = request.Request(argv[1], d)
    with request.urlopen(r) as response:
        print(response.read().decode("utf8"))
