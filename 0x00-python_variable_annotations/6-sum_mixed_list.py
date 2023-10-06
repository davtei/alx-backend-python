#!/usr/bin/env python3
""" Complex types - mixed list """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Return sum of mixed list of integers and floats """
    total = 0.0
    for i in mxd_lst:
        if isinstance(i, (int, float)):
            total += i
    return total
