#!/usr/bin/env python3
"""get filtered logs"""
import logging
import re
import mysql.connector
from typing import List


pattern = r'(?<={}=).*?(?={})'
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')

def filter_datum(fields, redaction, message, separator) -> str:
	"""returns the log message obfuscated"""
	for field in fields:
		message = re.sub(pattern.format(field, separator), redaction, message)
	return message

class RedactingFormatter(logging.Formatter):
	""" Redacting Formatter class
		"""

	REDACTION = "***"
	FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
	SEPARATOR = ";"

	def __init__(self, fields: List[str]):
		super(RedactingFormatter, self).__init__(self.FORMAT)
		self.fields = fields

	def format(self, record: logging.LogRecord) -> str:		
		"""to filter values in incoming log records using filter_datum"""
		msg = super().format(record)
		return filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)


def get_logger() -> logging.Logger:
	"""returns a logging.Logger object"""
	logger = logging.getLogger("user_data")
	logger.setLevel(logging.INFO)
	stream_handler = logging.StreamHandler()
	formatter = RedactingFormatter(fields=PII_FIELDS)
	stream_handler.setFormatter(formatter)
	logger.addHandler(stream_handler)
	return logger

def get_db() -> mysql.connector.connection.MySQLConnection:
	from os import getenv
	try:
		# Establish a connection to the MySQL database
		connection = mysql.connector.connect(
			host=getenv('PERSONAL_DATA_DB_HOST'),
			user=getenv('PERSONAL_DATA_DB_USERNAME'),
			password=getenv('PERSONAL_DATA_DB_PASSWORD'),
			database=getenv('PERSONAL_DATA_DB_NAME'),
			port=3306
		)
		return connection
	except mysql.connector.Error as err:
		print(f"Error: {err}")
		return None


# fields = ["password", "date_of_birth"]
# messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

# for message in messages:
# 	print(filter_datum(fields, 'xxx', message, ';'))