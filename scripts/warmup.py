import math


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

def is_seperator(c):
	return c in [" ", "\t", "\n", "\r", ",", ";", "?", "!", "."]
	


def count_words(txt):
	sum_of_words = 0
	prev_char = None

	for char in txt:
		if not is_seperator(char) and (prev_char is None or is_seperator(prev_char)):
			sum_of_words += 1
		prev_char = char
		
	return sum_of_words

print(count_words("The boy is a good programmer hello!."))
print(count_words(""))
print(count_words("hello!!!!!!."))


def capitalize(s):
	return s[0].upper() + s[1:]

print(capitalize(" yolo"))
print(" yolo".capitalize())

def words_in_a_text(txt):
	words_array = []
	start_word = -1
	for i in range(0, len(txt), 1):
		c = txt[i] if i < len(txt) else " "
		if not is_seperator(txt[i]) and start_word < 0:
			start_word = i
		
		if is_seperator(txt[i]) and start_word >= 0:
			word = txt[start_word:i]
			words_array.append(word)
			start_word = -1
	return words_array

print(words_in_a_text("The boy is a good programmer hello!."))

# Implement the Caesar cypher

def encrypt(msg: str, key: int) -> str:
	enc_msg = ''
	for char in msg:
		code = ord(char)
		if code >= 65 and code <= (65 + 26 -1):
			code -= 65
			code = (code + key) % 26
			code += 65
		enc_msg += chr(code)
	return enc_msg

print(encrypt('Hello World!', 5))

# bubble sort

def bubble_sort(ar):
	issortable = True
	length = len(ar)

	i = 0;
	while issortable:
		issortable = False
		length -= 1
		for i in range(0, length):
			temp = ar[i]
			if temp > ar[i + 1]:
				ar[i] = ar[i + 1]
				ar[i + 1] = temp
				issortable = True

		i += 1
	return ar


print(bubble_sort([3, 5, 2,4, 7, 8]))

# Create a function that will convert a string 
# containing a binary number into a number
def binary_to_decimal(sbinary):
	return int(sbinary, 2)


print(binary_to_decimal('111'))

# Find the maximum number in a jagged 
# array of numbers or array of numbers
def max_jaggered_array(ar):
	max_el = 0
	for el in ar:
		if isinstance(el, list):
			el = max_jaggered_array(el)
		if el > max_el:
			max_el = el
	return max_el

print(max_jaggered_array([2, [34], [409, [56, 6]]]))


def multDigit(s_num, digit):
	carry = 0
	p = ''

	for i in range(len(s_num) - 1, -1 , -1):
		num_digit = int(s_num[i])
		prod = digit * num_digit + carry
		prod_digit = prod % 10
		carry = math.floor(prod / 10)
		p = str(prod_digit) + p

	if carry > 0:
		p = p + carry

	return p

print(multDigit('123', 2))


def multi(snum1, snum2):
	partialResults = []
	for i in range(len(snum2) - 1, -1, -1):
		digit = int(snum2[i])
		partialResult = multDigit(snum1, digit)
		partialResult +=  "0" * len(partialResults)
		partialResults.append(partialResult)  
	sum = ""
	for num in partialResults:
		sum = add(sum, num)
	return sum
print(multi('123', '111'))
