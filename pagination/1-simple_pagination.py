import csv
import math
from typing import List
from simple_helper_function import index_range

class Server:
	"""Server class to paginate a database of popular baby names.
	"""
	DATA_FILE = "Popular_Baby_Names.csv"

	def __init__(self):
		self.__dataset = None

	def dataset(self) -> List[List]:
		"""Cached dataset
		"""
		if self.__dataset is None:
			with open(self.DATA_FILE) as f:
				reader = csv.reader(f)
				dataset = [row for row in reader]
			self.__dataset = dataset[1:]

		return self.__dataset

	def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
			assert(page > 0)
			assert(page_size > 0)
			i_range = index_range(page, page_size)
			print(i_range)
			return [self.dataset()[idx] for idx in range(i_range[0], i_range[1])]

print(Server().get_page())