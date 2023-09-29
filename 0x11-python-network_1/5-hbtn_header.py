#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays the
value of the variable X-Request-Id in the response header.

Usage: ./5-hbtn_header.py <URL>
"""
import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: ./5-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    req = requests.get(url)

    # Check if 'X-Request-Id' header is present in the response
    if 'X-Request-Id' in req.headers:
        print(req.headers['X-Request-Id'])
    else:
        print("The 'X-Request-Id' header is not present in the response.")
