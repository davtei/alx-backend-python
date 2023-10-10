#!/usr/bin/env python3
""" The basics async syntax """

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Wait for a random delay between 0 and max_delay """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
