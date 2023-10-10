#!/usr/bin/env python3
"""This module holds measure_runtime method"""

import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Returns total runtime"""
    starttime = time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension()
                         )
    runtime = time() - starttime
    return runtime
