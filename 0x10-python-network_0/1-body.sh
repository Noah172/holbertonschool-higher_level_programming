#!/bin/bash
# script that takes in a URL and displays the body of the response
curl -sLX GET "$1"
