def sort_by_bits(numbers):
    new_num = []
    for i in range(len(numbers)):
        a = bin(numbers[i])[2:]
        print(a)
        as = int(a, 2)
        numbers.remove(as)
        for r in range(len(new_num)):
            if a.count('1')> new_num[r].count('1'):
                new_num.insert(r, a)
    for ii in range(len(new_num)):
        new_num[ii] = int(new_num[ii], 2)
    return new_num
print(sort_by_bits([7, 6, 15, 8]))