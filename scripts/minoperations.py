#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
	"""Returns the minimum number of operations"""
	if not isinstance(n, int) or n <= 1:
		return 0

	# Find prime factorization of n
	factors = []
	for i in range(2, int(n**0.5) + 1):
		while n % i == 0:
			factors.append(i)
			n //= i
	print(n)
	if n > 1:
		factors.append(n)

	# Calculate minimum number of operations based on prime factors
	min_ops = sum(factors)

	return min_ops


print("--------->", minOperations(9))