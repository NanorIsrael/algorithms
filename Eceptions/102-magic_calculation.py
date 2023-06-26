#!/usr/bin/python3


def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += (a ** b) / i
        except:
            result = b + a

    return result


if __name__ == "__main__":
    import dis
    dis.dis(magic_calculation)

result = magic_calculation(18, 3)
print(result)