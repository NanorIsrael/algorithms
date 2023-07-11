#!/usr/bin/python3
# def magic_string():
#     c = getattr(magic_string, 'c', 0) + 1
#     setattr(magic_string, 'c', c); return 'BestSchool' * c

#!/usr/bin/python3
def magic_string(H=[]):
    H += ["BestSchool"]
    return (", ".join(H))


for _ in range(10):
    print(magic_string())