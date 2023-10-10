#!/usr/bin/env python3
""" Module holds measure_time method """
import asyncio
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns (total runtime) / (n) for wait_n method"""
    start = time()
    asyncio.run(wait_n(n, max_delay))
    return (time() - start) / n
