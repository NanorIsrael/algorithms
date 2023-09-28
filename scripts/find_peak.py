
def find_peak(my_list):
	if len(my_list) == 0:
		return None

	peak_val = my_list[0]
	for val in my_list:
		if val > peak_val:
			peak_val = val
	return peak_val

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
