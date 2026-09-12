def is_disarium(n):
    sum_of_digits = 0
    for index, digit in enumerate(str(n), start=1):
        sum_of_digits += int(digit) ** index
    return sum_of_digits == n
print(is_disarium(564))