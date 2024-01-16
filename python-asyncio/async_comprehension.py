#!/usr/bin/env python3
"""Basic Async Syntax"""
import asyncio
from index import async_generator


async def async_comprehension():
	"""will loop 10 times, each time asynchronously wait 1 second,
	then yield a random number between 0 and 10 """
	result = [i async for i in async_generator()]
	return result



# async def main():
#     print(await async_comprehension())

# asyncio.run(main())