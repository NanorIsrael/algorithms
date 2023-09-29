
def find_peak(my_list):
	""" Defines the function find peak"""
	if len(my_list) == 0:
		return None
	left = 0
	right =  len(my_list) - 1
    
	while left < right:
		mid = left + (right - left) // 2

		if my_list[mid] > my_list[mid + 1]:
			right = mid;
		else:
			left = mid + 1
	return my_list[left]

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
