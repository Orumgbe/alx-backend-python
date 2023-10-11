#!/usr/bin/env python3
"""Module holds sum_list method"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns sum of elements in the list"""
    val = 0.00
    for n in input_list:
        val += n
    return val
