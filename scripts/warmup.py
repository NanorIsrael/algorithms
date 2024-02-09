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

