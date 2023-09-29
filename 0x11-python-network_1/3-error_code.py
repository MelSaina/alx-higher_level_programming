#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8).

Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
import urllib.request
import urllib.error
import sys

# Extract the URL from the command line argument
url = sys.argv[1]

try:
    # Send a GET request to the URL
    with urllib.request.urlopen(url) as response:
        # Read and decode the response body as UTF-8
        body = response.read().decode('utf-8')
        print(body)
except urllib.error.HTTPError as e:
    # Handle HTTP errors by printing the error code
    print("Error code:", e.code)
