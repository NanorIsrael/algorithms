#!/usr/bin/env python3

""" script that fetches https://alx-intranet.hbtn.io/status """
import requests
import sys

body = {}
body['email'] = sys.argv[2]
res = requests.post('https://alx-intranet.hbtn.io/', data=body)
content = res
print(content.text)
# print("\t- type:", type(content.text))
# print("\t- content:", content.text)