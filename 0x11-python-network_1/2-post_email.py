#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.

Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import urllib.parse
import urllib.request
# Check if the script is called with the correct number of arguments
if len(sys.argv) != 3:
    print("Usage: ./2-post_email.py <URL> <email>")
    sys.exit(1)

# Extract the URL and email from command line arguments
url = sys.argv[1]
email = sys.argv[2]

# Create a dictionary with the email parameter
data = {'email': email}

# Encode the data to be sent in the POST request
data = urllib.parse.urlencode(data).encode('utf-8')

# Create a POST request with the provided URL and data
request = urllib.request.Request(url, data=data, method='POST')

# Perform the POST request and handle the response
with urllib.request.urlopen(request) as response:
    body = response.read().decode('utf-8')
    print("Your email is:", email)
    print(body)
