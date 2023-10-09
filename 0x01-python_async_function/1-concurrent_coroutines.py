#!/usr/bin/env python3
"""This module holds the wait_n method"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list in order of time taken for task completion"""
    wait_time = []
    asc_order = []
    for calls in range(n):
        wait_time.append(wait_random(max_delay))
    for fastest in asyncio.as_completed(wait_time):
        asc_order.append(await fastest)
    return asc_order
