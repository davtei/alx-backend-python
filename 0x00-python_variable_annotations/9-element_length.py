#!/usr/bin/env python3

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return list of tuples, each containing a sequence and its length """
    return [(i, len(i)) for i in lst]
