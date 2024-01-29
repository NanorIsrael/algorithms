#!/usr/bin/env python3
"""
Main file
"""
from typing import Union

def index_range(page:int = None, page_size: int = None) -> tuple:
	if page and page_size:
		if page > 1:
			start = (page * page_size) - page_size
			return (start, page * page_size)
		else:
			return (0, page_size)
	else:
		return (0, 0)


# res = index_range(1, 7)
# print(type(res))
# print(res)

# res = index_range(page=3, page_size=15)
# print(type(res))
# print(res)