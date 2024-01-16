#!/usr/bin/env python3
# rand.py

import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[int, None, None]:
	"""will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10"""
	for i in range(0, 10):
		i = random.uniform(0, 10)
		yield i
		await asyncio.sleep(1)

# async def main():
# 	res = [i async for i in makerandom()]
# 	print(res)

# if __name__ == "__main__":
# 	random.seed(444)
# 	r1 = asyncio.run(main())
# 	print()
# 	print(f"r1: {r1}")

# if __name__ == '__main__':
#     event_loop = asyncio.get_event_loop()
#     try:
#         event_loop.run_until_complete(main())
#     finally:
#         event_loop.close()

# async def print_yielded_values():
#     result = []
#     async for i in async_generator():
#         result.append(i)
#     print(result)

# asyncio.run(print_yielded_values())
