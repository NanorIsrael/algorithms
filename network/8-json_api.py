#!/usr/bin/env python3

""" script that fetches https://alx-intranet.hbtn.io/status """
import requests
import sys

if __name__ == "__main__":
	headers = {}
	username = sys.argv[1]
	headers['X-GitHub-Api-Version'] = "2022-11-28"
	headers['Accept'] = "application/vnd.github+json"
	headers['Authorization'] = f"Bearer {sys.argv[2]}"

	res = requests.get(f'https://api.github.com/users/{username}', headers)
	content = res.json()
	if res.status_code == 200 and content:
		print(content['id'])
	else:
		print('None')
