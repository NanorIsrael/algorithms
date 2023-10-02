#!/usr/bin/python3

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(url) as response:
        content = response
        print("Body response:")
        # print("\t- utf8 content:", help(content))
        print("\t- utf8 content:", content.getheader('X-Request-Id'))
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
