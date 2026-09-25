def is_power_of_two(n):
    a = bin(n)[2:]
    if a.count('1') == 1:
        return True
    else:
        return False