def square_digits(n):
    str_n = str(n)
    result = int(''.join(str(int(digit) ** 2) for digit in str_n))
    return result
