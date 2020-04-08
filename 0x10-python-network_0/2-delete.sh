#!/bin/bash
# that sends a DELETE request to the URL passed as the first argument
curl -s -X "$1" DELETE
