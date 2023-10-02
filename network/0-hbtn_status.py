#!/usr/bin/python3

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode('utf8'))
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
