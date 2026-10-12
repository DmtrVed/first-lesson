def sort_by_bits(numbers):
    return sorted(numbers, key=lambda x: (bin(x).count('1'), x))
