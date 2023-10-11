#!/usr/bin/env python3
"""Module holds safe_first_element method"""

from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Duck-typed annotations"""
    if lst:
        return lst[0]
    else:
        return None
