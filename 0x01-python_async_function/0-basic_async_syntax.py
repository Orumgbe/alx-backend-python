#!/usr/bin/env python3
"""This module contains wait_random method"""

import asyncio
from random import random


async def wait_random(max_delay: int = 10) -> float:
    """Async coroutine, waits random delay time and return delay time"""
    wait_time = random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
