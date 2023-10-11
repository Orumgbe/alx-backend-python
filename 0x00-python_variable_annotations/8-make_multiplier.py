#!/usr/bin/env python3
"""Module holds make_multiplier method"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies the argument with 'multiplier'"""
    def multiply(num):
        """inner function, multiplies num with muliplier in outer func"""
        return num * multiplier
    return multiply 
