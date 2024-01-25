#!/usr/bin/python3

import re
from collections import defaultdict

def process_log_line(line):
	# Define a regular expression pattern to match the required format
	pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+) - \[([^]]+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$')
	
	# Attempt to match the pattern
	match = pattern.match(line)
	
	# If the line doesn't match the required format, return None
	if not match:
		return None
	
	# Extract relevant information from the match object
	ip_address, date, status_code, file_size = match.groups()
	
	# Convert file_size to an integer
	file_size += int(file_size)
	
	# Return a dictionary with the extracted information
	return {'ip_address': ip_address, 'date': date, 'status_code': int(status_code), 'file_size': file_size}

def compute_metrics(log_lines, file_size):
	# Initialize metrics
	total_requests = 0
	successful_requests = 0
	total_file_size = 0
	
	# Create a defaultdict to store file size counts for each IP address
	file_size_counts = defaultdict(int)
	
	# Process each log line and update metrics
	for line in log_lines:
		log_entry = process_log_line(line)
		
		if log_entry:
			total_requests += 1
			total_file_size = log_entry['file_size']
			
			if log_entry['status_code'] == 200:
				successful_requests += 1
			
			# Update file size count for the IP address
			file_size_counts[log_entry['ip_address']] += log_entry['file_size']
	
	# Compute average file size per IP address
	average_file_size_per_ip = {ip: file_size_counts[ip] / total_requests for ip in file_size_counts}
	
	# Return computed metrics
	return {
		'total_requests': total_requests,
		'successful_requests': successful_requests,
		'total_file_size': total_file_size,
		'average_file_size_per_ip': average_file_size_per_ip
	}

if __name__ == "__main__":
	# Read stdin line by line
	# [print(line.strip() ) for line in iter(input, '')]
	max_lines = 10
	lines = []
	file_size = 0
	for line in iter(input, ''):
		while len(lines) < max_lines:
			lines.append(line.strip())
			

			# Compute metrics
		print(lines)
		metrics = compute_metrics(lines, file_size)
			
			# # Print the computed metrics
		print("File size:", metrics['total_file_size'])
		print("Total Requests:", metrics['total_requests'])
		print("Successful Requests:", metrics['successful_requests'])
		print("Average File Size per IP:")
		for ip, average_size in metrics['average_file_size_per_ip'].items():
			print(f"  {ip}: {average_size:.2f}")
		lines = []