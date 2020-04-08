#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument
curl -s -X "$1" POST -H "Content-Type: application/json" -d @"$2"
