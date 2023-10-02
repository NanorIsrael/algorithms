#!/usr/bin/python3

import urllib.request
import urllib.parse
import sys
url = sys.argv[1]
data = {}
data['email'] = sys.argv[2]

try:
	parsed_data = urllib.parse.urlencode(data).encode('ascii')
    with urllib.request.urlopen(url, parsed_data) as response:
        content = response.read()
        print("Body response:")
        # print("\t- utf8 content:", help(content))
        print("\t- utf8 content:", content.decode('utf8'))
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
