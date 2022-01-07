#/bin/bash
# script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -sL -H "Content-type:application/json"  -d @"$2" -X POST "$1"
