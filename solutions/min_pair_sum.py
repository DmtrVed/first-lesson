def min_pair_sum(numbers):
    otvet = 0
    for i in range(len(numbers)//2):
        otvet+= min(numbers)*max(numbers)
        numbers.remove(max(numbers))
        numbers.remove(min(numbers))
    return otvet
print(min_pair_sum([12, 6, 10, 26, 3, 24]))