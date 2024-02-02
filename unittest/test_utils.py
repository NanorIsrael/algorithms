#!/usr/bin/env python3
"""Test for utilities.py.
"""
import unittest
from parameterized import parameterized, param
from utils import access_nested_map
# from nose.tools import assert_equal


class TestAccessNestedMap(unittest.TestCase):
	@parameterized.expand([
			({"a": 1}, ("a", ), 1),
			({"a": {"b": 2}}, ("a", ), {"b": 2}),
			({"a": {"b": 2}}, ("a", "b"), 2)
	])
	def test_access_nested_map(self, nested_map, path, expected):
		assert access_nested_map(nested_map, path) == expected

	@parameterized.expand([
			({}, ("a", ), "a"),
			({"a": 1}, ("a", "b"), "b")
	])
	def test_access_nested_map_exception(
		self, nested_map,
		path,
		expected_message
	):
		with self.assertRaises(KeyError) as context:
			access_nested_map(nested_map, path)
		self.assertEqual(str(context.exception), f"'{expected_message}'")


if __name__ == '__main__':
	unittest.main()