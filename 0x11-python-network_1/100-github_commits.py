#!/usr/bin/python3
"""
takes your Github credentials (username and password) and
uses the Github API to display your id
"""
from requests import get
from sys import argv


if __name__ == "__main__":

    gc = get("https://api.github.com/repos/{}/{}/commits".
               format(argv[2], argv[1])).json()

    x = 0
    for arg in gc:
        x += 1
        sha = arg.get("sha")
        name = arg.get("commit").get("author").get("name")
        print("{}: {}".format(sha, name))
        if x > 9:
            break
