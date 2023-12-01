#!/usr/bin/env python3
"""A github org client test suite"""

import unittest
from typing import Dict
from unittest.mock import MagicMock, patch

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
