#!/usr/bin/env python3
"""Module holds element_length method"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns list of tuples for values in lst"""
    return [(i, len(i)) for i in lst]
