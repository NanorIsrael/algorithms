from math import factorial


def paired_brackects(num):
	return factorial(2 * num) // (factorial(num + 1) * factorial(num))



print(paired_brackects(1))
print(paired_brackects(2))
print(paired_brackects(3))
print(paired_brackects(4))