#!/usr/bin/env python3
"""Module holds to_kv method"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes two arguments and returns a tuple"""
    return k, v**2
