#!/usr/bin/env bash
# script that takes in a URL and displays the body of the response
curl -s -L -X GET "$1"
