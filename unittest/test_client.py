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
	def setUp(self):
		self.expected_url = "https://api.github.com/orgs/{}"
		self.expected_result = {
			"repos_url": "example_repos_url",
			"license": {
				"key": "1233"
			}
		}


	@parameterized.expand([
		("google",),
		("abc",),
	])
	@patch("client.get_json")
	def test_org(self, org_name, mock_get_json):		
		# Mock the get_json function to return a known payload
		mock_get_json.return_value = self.expected_result

		# Create an instance of GithubOrgClient
		github_org_client = GithubOrgClient(org_name)

		# Call the org method
		result = github_org_client.org
		result = github_org_client.org
		result = github_org_client.org

		# Assert that get_json is called with the expected argument
		mock_get_json.assert_called_once_with(self.expected_url.format(org_name))

		# Assert that the result matches the expected value
		self.assertEqual(result, self.expected_result)

	def test_public_repos_url(self):
		with patch(
			'client.GithubOrgClient.org',
			PropertyMock(return_value=self.expected_result)
			):
			mocked_client = GithubOrgClient('google')
			result = mocked_client._public_repos_url
			result = mocked_client._public_repos_url
			result = mocked_client._public_repos_url
			self.assertEqual(result, self.expected_result['repos_url'])

	@patch('client.get_json')
	def test_public_repos(self, mock_get_json):
		with patch(
			'client.GithubOrgClient._public_repos_url',
			return_value = [
                {'name': 'repo_0'},
                {'name': 'repo_1'},
                {'name': 'repo_2'}
            ]
		):
			mock_get_json.return_value = [
                {'name': 'repo_0'},
                {'name': 'repo_1'},
                {'name': 'repo_2'}
        	]
			mocked_client = GithubOrgClient('google')
			result = mocked_client.public_repos()
			assert len(result) > 0

			mock_get_json.assert_called_once()
			self.assertEqual(result, ['repo_0', 'repo_1', 'repo_2'])


if __name__ == "__main__":
	unittest.main()
