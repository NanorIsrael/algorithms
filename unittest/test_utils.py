#!/usr/bin/env python3
"""Test for utilities.py.
"""
import unittest
from parameterized import parameterized, param
from utils import access_nested_map, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
	"""Test for test access nested map.
	"""
	@parameterized.expand([
		({"a": 1}, ("a", ), 1),
		({"a": {"b": 2}}, ("a", ), {"b": 2}),
		({"a": {"b": 2}}, ("a", "b"), 2)
	])
	def test_access_nested_map(self, nested_map, path, expected):
		"""Test for test access nested map.
		"""
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
		"""Test for test access nested map.
		"""
		with self.assertRaises(KeyError) as context:
			access_nested_map(nested_map, path)
		self.assertEqual(str(context.exception), f"'{expected_message}'")

	@parameterized.expand([
		(("http://example.com",), {"payload": True}),
		(("http://holberton.io",), {"payload": False})
	])
	@patch('utils.get_json')
	def test_get_json(self, test_url, test_payload, mock_get_json):
		"""Test for test access nested map.
		"""
		mock_get_json.return_value = test_payload
		result = mock_get_json(test_url)
		self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
	"""Test for test access nested map.
	"""
    def test_memoize(self):
		"""Test for test _memoize function.
		"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            thing = TestClass()
            thing.a_property()
            thing.a_property()
            mock_method.assert_called_once()



if __name__ == '__main__':
	unittest.main()
