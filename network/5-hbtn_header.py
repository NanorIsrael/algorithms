#!/usr/bin/env python3
""" script that fetches https://alx-intranet.hbtn.io/status """
import requests

res = requests.get('https://alx-intranet.hbtn.io/status')
content = res
print("Body response:")
print("\t- type:", type(content.text))
print("\t- content:", content.text)
# print("\t- content:", content.status)
# print("\t- utf8 content:", content.decode('utf8'))
