def max_gap(numbers):
    numbers.sort()
    mx = 0
    for i in range(len(numbers)):
        if (numbers[i+1]-numbers[i])>=mx:
            mx = numbers[i+1]-numbers[i]
    return numbers
print(max_gap([13, 10, 5, 2, 9]))