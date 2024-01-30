#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
	# def __init__(self):
	# 	self.super()
	def put(self, key, item):
		if key is None or item is None:
			return
		else:
			self.self.cache_data[key] = item
	
	def get(self, key):
		if key is None:
			return None
		else:
			return self.cache_data.get(key)
			
