#!/usr/bin/env python3
"""A github org client test suite"""

import unittest
from typing import Dict
from unittest.mock import MagicMock, Mock, PropertyMock, patch

from client import GithubOrgClient
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """A GithubOrgClient test suite"""

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, expected: Dict, mock_get_json: MagicMock
                 ) -> None:
        """Test GithubOrgClient.org"""
        mock_get_json.return_value = MagicMock(return_value=expected)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), expected)
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self) -> None:
        """Test _public_repos_url"""
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
        ) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/users/google/repos"
            }
            self.assertEqual(GithubOrgClient("google")._public_repos_url,
                             "https://api.github.com/users/google/repos"
                             )
