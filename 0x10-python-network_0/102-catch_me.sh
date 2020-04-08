#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that causes the server to respond
curl -s -X PUT -L -d "user_id=98" "0.0.0.0:5000/catch_me" -H 'origin:HolbertonSchool'
