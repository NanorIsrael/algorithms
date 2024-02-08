def digit_from_right(s, digit_no):
	if digit_no >= len(s):
		return 0
	char = s[len(s) - 1 - digit_no]
	return int(char)


def add(num1, num2):
	s = ""
	carry = 0

	max_size = max(len(num1), len(num2))

	for i in range(0, max_size, 1):
		digit1 = digit_from_right(num1, i)
		digit2 = digit_from_right(num2, i)

		sum = digit1 + digit2 + carry
		digit_sum = sum % 10
		carry = 1 if sum >= 10 else 0

		s = str(digit_sum) + s
	
	if carry > 0:
		s = carry + s
	return s


n1 = '9879873459058080284082789709'
n2 = '8241342424989'

print(add(n1, n2))