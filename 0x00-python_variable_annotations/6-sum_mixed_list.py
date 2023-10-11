#!/usr/bin/env python3
"""Module holds sum_list method"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns sum of elements in the list"""
    val = 0.00
    for n in mxd_lst:
        val += n
    return val
