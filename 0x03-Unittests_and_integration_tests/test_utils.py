#!/usr/bin/env python3
"""Utils test module"""

import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
    ) -> None:
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_error(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
    ) -> None:
        """Test access_nested_map function"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
