#!/usr/bin/env python3
""" More involved type annotations """

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')
Res = Union[Any, None]
Def = Union[Any, None]


def safely_get_value(dct: Mapping, key: Any,
                     default: Def = None) -> Res:
    """ Return value of key if it exists, otherwise return default """
    if key in dct:
        return dct[key]
    else:
        return default
