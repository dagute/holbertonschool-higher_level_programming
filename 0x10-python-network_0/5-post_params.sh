#!/bin/bash
# takes in a URL, sends a POST request to the passed URL
curl -s -d "$1" -X POST "email=hr@holbertonschool.com&subject=I will always be here for PLD"
