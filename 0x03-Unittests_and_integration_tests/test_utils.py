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
