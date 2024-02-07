#!/usr/bin/env python3
"""get filtered logs"""
import logging
import re


def filter_datum(fields, redaction, message, separator):
	for field in fields:
		message = re.sub(
		r'(?<={}=).*?(?={})'.format(field, separator),
		redaction,
		message)
	return message




fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
	print(filter_datum(fields, 'xxx', message, ';'))