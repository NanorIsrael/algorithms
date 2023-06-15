#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if type(roman_string) != str:
        return 0
    sum_val = 0
    prev = 0
    roman_table = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
            "D": 500, "M": 1000
    }
    for k in reversed(roman_string):
        if k in roman_table:
            val = roman_table.get(k, 0)
            if val >= prev:
                sum_val += val
            else:
                sum_val -= val
        prev = val
    return sum_val
            
# def roman_to_int(roman_string):
#     if not isinstance(roman_string, str) or roman_string is None:
#         return 0

#     roman_table = {
#         'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
#     }

#     total = 0
#     prev_value = 0

#     for c in reversed(roman_string):
#         value = roman_table.get(c, 0)

#         if value >= prev_value:
#             total += value
#         else:
#             total -= value

#         prev_value = value

#     return total


roman_number = None
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = 1
print("{} = {}".format(roman_number, roman_to_int(roman_number)))


roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXIXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
