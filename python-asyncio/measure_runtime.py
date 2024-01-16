#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio
import time
from async_comprehension import async_comprehension

async def measure_runtime():
	"""Measure the runtime"""
	s = time.perf_counter()
	res = await asyncio.gather(*(async_comprehension() for i in range(4)))
	elapsed = time.perf_counter() - s
	return elapsed

async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)
