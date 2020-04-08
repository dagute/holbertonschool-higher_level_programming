#!/bin/bash
# sends a request to a URL passed as an argument
curl -sL -I "$1" -o /dev/null -w '%{http_code}'
