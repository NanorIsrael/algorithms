import sys

# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# operator = input("Select operator: \n 1. +  2. - 3. x \n")

# if operator == "1":
#     print("The result is = {}".format(int(num1 ) + int(num2)) )
# if operator == "2":
#     print("The result is = {}".format(int(num2 ) - int(num1)) )
# if operator == "3":
#     print("The result is = {}".format(int(num2 ) * int(num1)) )
# else:
#     print("Hello Collins!")



# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")
# age = input("Enter age: ")

# print("\n\n\n \t\tReview you data.")
# print("\t -----------------------")
# print("first name: {}".format(first_name) )
# print("last name: {}".format(last_name) )
# print("age: {} years old".format(age) )

string = '{{[)()]}}'
stack = []
for bracket in string:
	if bracket in ['{', '[', '(']:
		stack.append(bracket)
	else:
		last_el = stack[-1]
		if bracket == ']' and last_el == '[':
			print(f'contains a valid parenthesis {last_el}{bracket}')
		
		elif bracket == '}' and last_el == '{':
			print(f'contains a valid parenthesis {last_el}{bracket}')
		
		elif bracket == ')' and last_el == '(':
			print(f'contains a valid parenthesis {last_el}{bracket}')
		else:
			print('Do not contain a valid parenthesis')
