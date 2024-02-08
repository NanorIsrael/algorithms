#!/usr/bin/env python3
"""Test for utilities.py.
"""
import unittest
import utils
import client
from unittest.mock import patch, PropertyMock
from client import get_json, GithubOrgClient
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
	"""Test for TestGithubOrgClient.
	"""

	@parameterized.expand([
		("google",),
		("abc",),
	])
	@patch("client.get_json")
	def test_org(self, org_name, mock_get_json):
		assert client.get_json is mock_get_json
		expected_url = f"https://api.github.com/orgs/{org_name}"
		expected_result = {"repos_url": "example_repos_url"}

		# Mock the get_json function to return a known payload
		mock_get_json.return_value = expected_result

		# Create an instance of GithubOrgClient
		github_org_client = GithubOrgClient(org_name)

		# Call the org method
		result = github_org_client.org
		result = github_org_client.org
		result = github_org_client.org

		# Assert that get_json is called with the expected argument
		mock_get_json.assert_called_once_with(expected_url)

		# Assert that the result matches the expected value
		self.assertEqual(result, expected_result)

	
if __name__ == "__main__":
	unittest.main()
