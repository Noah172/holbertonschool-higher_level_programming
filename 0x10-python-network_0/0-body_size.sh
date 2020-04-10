#!/bin/bash
# script that displays the size of the body
curl -s -I "$1" | grep Content-Length | cut --delimiter " " -f2
