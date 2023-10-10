#!/usr/bin/env python3
"""This module holds task_wait_n method"""

from typing import List
import asyncio
import random


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list in order of time taken for task completion"""
    wait_time = []
    asc_order = []
    for calls in range(n):
        wait_time.append(task_wait_random(max_delay))
    for fastest in asyncio.as_completed(wait_time):
        asc_order.append(await fastest)
    return asc_order
