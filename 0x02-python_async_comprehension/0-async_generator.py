#!/usr/bin/env python3
"""This module contains async_generator method"""

import asyncio
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Coroutine loops 10 times and yields a random number (0 to 10)"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random() * 10
