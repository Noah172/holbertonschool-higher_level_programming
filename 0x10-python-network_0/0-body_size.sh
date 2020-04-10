#!/usr/bin/env bash
# script that takes in a URL and displays the size 
# of the body of the response
curl -s -I "$1" | grep Content-Length | cut --delimiter " " -f2
